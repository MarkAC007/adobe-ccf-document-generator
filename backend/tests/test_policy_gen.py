import json
import pytest
from pathlib import Path
from src.data_processor import DataProcessor
from src.policy_generator import PolicyGenerator

def test_access_management_policy_generation():
    """Test basic policy document generation"""
    # Setup paths
    raw_data_path = Path('data/raw')
    processed_data_path = Path('data/processed')
    output_path = Path('output/policies')
    test_config_path = Path('data/test_configs/access_mgmt_test.json')
    processed_controls_path = processed_data_path / 'controls_v2.json'
    processed_guidance_path = processed_data_path / 'control_guidance.json'
    
    # Ensure required files exist
    assert test_config_path.exists(), "Test configuration file not found"
    assert processed_controls_path.exists(), "Processed controls data not found. Run scripts/process_csv_data.py first"
    assert processed_guidance_path.exists(), "Processed guidance data not found. Run scripts/process_csv_data.py first"
    
    # Load test configuration
    with open(test_config_path) as f:
        config = json.load(f)
    
    # Verify processed data structure
    with open(processed_guidance_path) as f:
        guidance_data = json.load(f)
    assert "controls" in guidance_data, "Invalid guidance data structure"
    
    # Verify we have the expected controls
    control_ids = [c["ccf_id"] for c in guidance_data["controls"]]
    for expected_id in config["expected_controls"]:
        assert expected_id in control_ids, f"Missing control {expected_id} in guidance data"
    
    # Initialize components
    data_processor = DataProcessor(raw_data_path, processed_data_path)
    policy_generator = PolicyGenerator(data_processor)
    
    # Generate document
    document = policy_generator.generate_policy_document(config)
    
    # Basic assertions
    assert document is not None
    assert config["policy_standard"] in document
    assert "Implementation Requirements" in document
    assert "Framework References" in document
    
    # Save the document
    saved_path = policy_generator.save_policy_document(document, output_path)
    
    # Verify the file was saved
    assert saved_path.exists()
    assert saved_path.is_file()
    print(f"Policy document saved to: {saved_path}")
