import json
import pytest
from pathlib import Path
from src.data_processor import DataProcessor
from src.policy_generator import PolicyGenerator

def test_policy_structure_and_content():
    """Test policy structure including statements, implementation requirements, and framework mappings"""
    # Setup paths
    raw_data_path = Path('data/raw')
    processed_data_path = Path('data/processed')
    output_path = Path('output/policies')
    test_config_path = Path('data/test_configs/policy_content_test.json')
    processed_controls_path = processed_data_path / 'controls_v2.json'
    
    # Ensure required files exist
    assert test_config_path.exists(), "Test configuration file not found"
    assert processed_controls_path.exists(), "Processed controls data not found"
    
    # Load test configuration and controls data
    with open(test_config_path) as f:
        config = json.load(f)
    
    with open(processed_controls_path) as f:
        controls_data = json.load(f)
    
    # Initialize components
    data_processor = DataProcessor(raw_data_path, processed_data_path)
    policy_generator = PolicyGenerator(data_processor)
    
    # Generate document
    document = policy_generator.generate_policy_document(config)
    
    def verify_section_content(section_name, expected_content):
        """Helper function to verify section content"""
        section_marker = f"## {section_name}"
        assert section_marker in document, f"Missing {section_name} section"
        
        section_start = document.index(section_marker)
        next_section = document.find("##", section_start + 2)
        section_content = document[section_start:next_section if next_section != -1 else None]
        
        for control_id, content in expected_content.items():
            assert f"### {control_id}:" in section_content, f"Missing {control_id} in {section_name}"
            assert content in section_content, f"Missing content for {control_id} in {section_name}"
    
    # Test Policy Statements
    verify_section_content("Policy Statements", 
                         config["expected_content"]["policy_statements"])
    
    # Test Implementation Requirements
    verify_section_content("Implementation Requirements",
                         config["expected_content"]["implementation_requirements"])
    
    # Test control formatting
    for control_id in config["expected_controls"]:
        # Check Policy Statement format
        assert f"### {control_id}:" in document, f"Missing control {control_id} in policy statements"
        
        # Check Implementation Requirements format
        impl_section = "## Implementation Requirements"
        assert impl_section in document, "Missing Implementation Requirements section"
        assert f"### {control_id}" in document[document.index(impl_section):], \
            f"Missing implementation requirements for {control_id}"
    
    # Test framework mappings table
    framework_section = "## Framework References"
    assert framework_section in document, "Missing Framework References section"
    
    table_header = "| Control ID | Framework | Reference |"
    assert table_header in document, "Missing framework reference table header"
    
    # Verify framework mappings
    for control_id, framework_maps in config["expected_content"]["framework_mappings"].items():
        for framework, references in framework_maps.items():
            for reference in references:
                mapping_row = f"| {control_id} | {framework} | {reference} |"
                assert mapping_row in document, f"Missing framework mapping: {mapping_row}"
    
    # Save and verify the document
    saved_path = policy_generator.save_policy_document(document, output_path)
    assert saved_path.exists()
    
    # Verify saved content
    with open(saved_path) as f:
        saved_content = f.read()
        assert saved_content == document, "Saved content doesn't match generated document"
