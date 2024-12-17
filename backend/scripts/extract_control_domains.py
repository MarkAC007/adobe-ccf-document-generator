import json
import sys

try:
    with open('data/processed/control_guidance.json', 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            # Debug: Print the structure of the data
            print("Data structure:", type(data))
            
            if isinstance(data, list):
                # If it's a list of controls
                unique_domains = set()  # To store unique control domains
                for item in data:
                    if isinstance(item, dict) and "control_domain" in item:
                        domain = item["control_domain"]
                        unique_domains.add(domain)
                
                # Print unique control domains
                for domain in sorted(unique_domains):
                    print(f"Control Domain: {domain}")
            
            elif isinstance(data, dict):
                # If it's a single control
                if "control_domain" in data:
                    print(f"Control Domain: {data['control_domain']}")
                else:
                    print("No control_domain found in the data")
            
            else:
                print(f"Unexpected data type: {type(data)}")
                
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            sys.exit(1)
            
except FileNotFoundError:
    print(f"Error: Could not find the file 'data/processed/control_guidance.json'")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)