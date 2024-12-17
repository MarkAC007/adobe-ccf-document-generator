# Document Generation Testing Concept
Version: 1.0

## Overview
This document outlines the testing approach for policy document generation, starting with Access Management Policy as a proof of concept.

## Project Structure
```
document_generator/
├── data/
│   ├── raw/                    # Original CSV files
│   │   ├── control_guidance.csv
│   │   ├── controls_v2.csv
│   │   └── erl.csv
│   ├── processed/              # Converted JSON files
│   │   ├── control_guidance.json
│   │   ├── controls_mapping.json
│   │   └── evidence_ref.json
│   └── test_configs/           # Test configuration files
│       └── access_mgmt_test.json
├── src/
│   ├── __init__.py
│   ├── data_processor.py       # Data conversion and query functions
│   ├── policy_generator.py     # Document generation logic
│   ├── templates.py            # Document templates
│   └── utils/
│       └── logger.py           # Logging configuration
├── tests/
│   ├── __init__.py
│   └── test_policy_gen.py      # Test cases
└── logs/
    └── debug.log              # Detailed logging output
```

## Data Structures

### 1. Processed JSON Formats

#### Control Guidance (control_guidance.json):
```json
{
  "controls": [
    {
      "ccf_id": "AM-01",
      "control_domain": "Asset Management",
      "control_name": "Inventory Management",
      "control_description": "Organization maintains an inventory...",
      "control_theme": "Process",
      "control_type": "Preventive",
      "policy_standard": "Asset Management Policy",
      "implementation_guidance": "1. Design and document...",
      "testing_procedure": "1. Inspect the policy...",
      "audit_artifacts": "E-AM-01\nE-AM-02\nE-AM-03"
    }
  ]
}
```

#### Framework Mappings (controls_mapping.json):
```json
{
  "AM-01": {
    "nist_cybersecurity": "ID.AM-2\nID.AM-1",
    "iso_27001": "A.8.1.1\nA.8.1.2",
    "pci_dss_v4": "12.5.1, 12.5.2"
  }
}
```

### 2. Test Configuration (access_mgmt_test.json):
```json
{
  "test_name": "Access Management Policy Generation",
  "policy_standard": "Access Management Policy",
  "selected_frameworks": [
    "nist_cybersecurity",
    "iso_27001",
    "pci_dss_v4"
  ],
  "test_parameters": {
    "include_implementation_guidance": true,
    "include_test_procedures": false,
    "debug_mode": true
  },
  "expected_controls": ["AM-01", "AM-02", "AM-03"]
}
```

## Module Specifications

### 1. Data Processor (data_processor.py)
```python
import pandas as pd
import json
import logging
from pathlib import Path

class DataProcessor:
    def __init__(self, raw_data_path: Path, processed_data_path: Path):
        self.raw_data_path = raw_data_path
        self.processed_data_path = processed_data_path
        self.setup_logging()

    def convert_csv_to_json(self):
        """Convert all CSV files to JSON format"""
        logging.debug("Starting CSV to JSON conversion")
        # Conversion logic here
        
    def get_controls_by_policy(self, policy_name: str) -> list:
        """Retrieve controls for specified policy"""
        logging.debug(f"Retrieving controls for policy: {policy_name}")
        # Control retrieval logic
        
    def get_framework_mappings(self, control_ids: list, frameworks: list) -> dict:
        """Get framework mappings for specified controls and frameworks"""
        logging.debug(f"Getting framework mappings for controls: {control_ids}")
        # Mapping retrieval logic
```

### 2. Policy Generator (policy_generator.py)
```python
from pathlib import Path
import logging
from .templates import PolicyTemplate

class PolicyGenerator:
    def __init__(self, data_processor):
        self.data_processor = data_processor
        self.template = PolicyTemplate()
        
    def generate_policy_document(self, config: dict) -> str:
        """Generate policy document based on configuration"""
        logging.debug(f"Generating policy document with config: {config}")
        # Document generation logic
```

### 3. Logger Configuration (utils/logger.py)
```python
import logging
import sys
from pathlib import Path

def setup_logging(log_path: Path):
    """Configure logging to both file and console"""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_path / 'debug.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
```

## Test Implementation

### 1. Basic Test Case (test_policy_gen.py)
```python
import json
import pytest
from pathlib import Path

def test_access_management_policy_generation():
    # Load test configuration
    with open('data/test_configs/access_mgmt_test.json') as f:
        config = json.load(f)
    
    # Initialize components
    data_processor = DataProcessor(
        Path('data/raw'),
        Path('data/processed')
    )
    policy_generator = PolicyGenerator(data_processor)
    
    # Generate document
    document = policy_generator.generate_policy_document(config)
    
    # Assertions
    assert "Access Management Policy" in document
    # Additional assertions for document structure and content
```

## Expected Output Format
```markdown
# Access Management Policy
Version: 1.0
Last Updated: 2024-12-14

## Purpose
This policy defines the requirements and responsibilities for managing access to organizational assets and information systems.

## Scope
This policy applies to all employees, contractors, and third parties who require access to organizational systems and data.

## Policy Statements

### Asset Management: Inventory Management
Organization maintains an inventory of information systems, which is reconciled on a periodic basis.

**Implementation Requirements:**
1. Design and document a process for maintaining an inventory...
2. Perform inventory reconciliation on a periodic basis...
3. Create and maintain periodic reconciliation documentation...

**Framework References:**
- NIST Cybersecurity Framework: ID.AM-2, ID.AM-1
- ISO 27001: A.8.1.1, A.8.1.2
- PCI DSS v4: 12.5.1, 12.5.2

[Additional controls...]

## Compliance Mapping
| Control ID | NIST CSF | ISO 27001 | PCI DSS v4 |
|------------|----------|-----------|------------|
| AM-01 | ID.AM-2 | A.8.1.1 | 12.5.1 |
[Additional mappings...]
```

## Implementation Steps

1. Data Preparation
   - Implement CSV to JSON conversion
   - Verify JSON structure matches expected format
   - Create test configuration file

2. Core Functionality
   - Implement DataProcessor methods
   - Create PolicyGenerator with template handling
   - Set up logging configuration

3. Testing
   - Run basic test case
   - Verify document structure
   - Check framework mappings
   - Validate logging output

4. Validation
   - Compare output to expected format
   - Verify all selected frameworks are included
   - Check policy content completeness

## Logging Examples

```
2024-12-14 10:00:01 - DataProcessor - DEBUG - Starting CSV to JSON conversion
2024-12-14 10:00:02 - DataProcessor - DEBUG - Processing control_guidance.csv
2024-12-14 10:00:03 - DataProcessor - INFO - Successfully converted control_guidance.csv to JSON
2024-12-14 10:00:04 - DataProcessor - DEBUG - Retrieving controls for policy: Access Management Policy
2024-12-14 10:00:05 - PolicyGenerator - DEBUG - Generating policy document with config: {test_name: "Access Management Policy Generation"...}
2024-12-14 10:00:06 - PolicyGenerator - INFO - Successfully generated policy document
```

## Error Handling

Include error handling for:
1. Missing or invalid input files
2. Invalid JSON structure
3. Missing required fields
4. Framework mapping mismatches
5. Template rendering errors

## Next Steps

After successful implementation of basic testing:
1. Expand test cases to cover additional policies
2. Add validation for document structure
3. Implement error handling
4. Add performance metrics logging
5. Create test reports