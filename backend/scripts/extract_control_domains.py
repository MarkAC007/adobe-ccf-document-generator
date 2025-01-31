"""
Extract Control Domains Script
============================

This script reads the control_guidance.json file and extracts all unique control domains.
It's useful for:
- Auditing the different types of control domains in use
- Verifying control domain consistency
- Getting a quick overview of control coverage areas

The script expects control_guidance.json to have a structure like:
{
    "controls": [
        {
            "ccf_id": "XX-XX",
            "control_domain": "Domain Name",
            "control_name": "Control Name",
            ...
        },
        ...
    ]
}

Output:
- Prints the data structure type
- Lists all unique control domains in alphabetical order
- Shows the total count of unique domains found
"""

import json
import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

try:
    # Use project_root to create absolute path
    json_path = project_root / 'data/processed/control_guidance.json'
    
    with open(json_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            print("Data structure:", type(data))
            
            # Get controls from the 'controls' key
            controls = data.get('controls', [])
            
            # Process the controls
            unique_domains = set()
            for control in controls:
                if isinstance(control, dict) and "control_domain" in control:
                    domain = control["control_domain"]
                    unique_domains.add(domain)
            
            if unique_domains:
                print("\nFound Control Domains:")
                for domain in sorted(unique_domains):
                    print(f"- {domain}")
                print(f"\nTotal number of unique domains: {len(unique_domains)}")
            else:
                print("\nNo control domains found in the data structure:")
                print(json.dumps(data, indent=2)[:200] + "...")
                
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            sys.exit(1)
            
except FileNotFoundError:
    print(f"Error: Could not find the file '{json_path}'")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)