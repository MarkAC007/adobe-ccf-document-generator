import json
import pytest
from pathlib import Path
from src.data_processor import DataProcessor
from src.policy_generator import PolicyGenerator

def test_policy_content_generation():
    """Test policy content including statements and framework mappings"""
    # Setup paths
    raw_data_path = Path('data/raw')
    processed_data_path = Path('data/processed')
    output_path = Path('output/policies')
    test_config_path = Path('data/test_configs/access_mgmt_content_test.json')
    processed_controls_path = processed_data_path / 'controls_v2.json'
    
    # Ensure required files exist
    assert test_config_path.exists(), "Test configuration file not found"
    assert processed_controls_path.exists(), "Processed controls data not found. Run scripts/process_csv_data.py first"
    
    # Verify processed data structure
    with open(processed_controls_path) as f:
        controls_data = json.load(f)
    assert "controls" in controls_data, "Invalid controls data structure"
    
    # Load test configuration
    with open(test_config_path) as f:
        config = json.load(f)
    
    # Initialize components
    data_processor = DataProcessor(raw_data_path, processed_data_path)
    policy_generator = PolicyGenerator(data_processor)
    
    # Generate document
    document = policy_generator.generate_policy_document(config)
    
    # Test policy statements
    for control_id, expected_statement in config["expected_content"]["policy_statements"].items():
        # Find the control description in processed data
        control = next((c for c in controls_data["controls"] if c["ccf_id"] == control_id), None)
        assert control is not None, f"Control {control_id} not found in processed data"
        assert expected_statement in control["control_description"], f"Expected statement not found in control description for {control_id}"
        assert expected_statement in document, f"Missing policy statement for {control_id}"
    
    # Test framework mappings
    for control_id, framework_maps in config["expected_content"]["framework_mappings"].items():
        control = next((c for c in controls_data["controls"] if c["ccf_id"] == control_id), None)
        assert control is not None, f"Control {control_id} not found in processed data"
        
        for framework, references in framework_maps.items():
            ref_field = f"{framework}_ref"
            assert ref_field in control, f"Framework reference field {ref_field} not found for {control_id}"
            
            # Get actual references from processed data
            actual_refs = control[ref_field]
            if actual_refs and not isinstance(actual_refs, list):
                actual_refs = [r.strip() for r in str(actual_refs).split('\n') if r.strip()]
            
            # Verify each expected reference exists
            for reference in references:
                assert any(reference in ref for ref in actual_refs), f"Reference {reference} not found for {control_id} in {framework}"
                assert reference in document, f"Missing framework reference {reference} for {control_id}"
    
    # Save and verify the document
    saved_path = policy_generator.save_policy_document(document, output_path)
    assert saved_path.exists()
    
    # Read saved document and verify table format
    with open(saved_path) as f:
        content = f.read()
    
    # Verify framework reference table structure
    assert "| Control ID | Framework | Reference |" in content
    assert "|------------|-----------|------------|" in content
    
    # Verify each control has framework mappings in table
    for control_id in config["expected_controls"]:
        framework_rows = [line for line in content.split('\n') 
                         if line.startswith(f"| {control_id} |")]
        assert len(framework_rows) > 0, f"No framework mappings found for {control_id}"
        
        # Verify framework mappings match the expected format
        for row in framework_rows:
            parts = [p.strip() for p in row.split('|') if p.strip()]
            assert len(parts) == 3, f"Invalid framework mapping format: {row}"
            assert parts[0] == control_id, f"Incorrect control ID in mapping: {row}"
            assert parts[1] in config["selected_frameworks"], f"Unknown framework in mapping: {row}"