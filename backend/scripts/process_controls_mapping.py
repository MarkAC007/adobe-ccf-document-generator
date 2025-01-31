import sys
import json
import csv
from pathlib import Path

# Add the project root directory to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

def process_ref_field(value):
    """Convert reference field string to array if it contains values"""
    if not value:
        return []
    # First split by newlines, then by commas, and flatten the result
    refs = []
    for item in value.split('\n'):
        item = item.strip()
        if item:
            if ',' in item:
                refs.extend([ref.strip() for ref in item.split(',') if ref.strip()])
            else:
                refs.append(item)
    return refs

def process_controls_mapping():
    """Process controls_mapping_check.csv to JSON format"""
    # Setup hardcoded paths
    input_file = project_root / 'data/raw/controls_mapping_check.csv'
    output_file = project_root / 'data/processed/controls_mapping_check.json'
    
    print(f"Processing {input_file} to {output_file}")
    
    try:
        # Read CSV file
        with open(input_file, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = []
            for row in reader:
                # Convert all reference fields to arrays
                for key in row:
                    if key.endswith('_ref'):
                        row[key] = process_ref_field(row[key])
                    elif row[key] == 'X':  # Handle framework fields
                        row[key] = 'X'
                    elif not row[key]:  # Handle empty fields
                        row[key] = ''
                    else:
                        row[key] = row[key].strip()
                data.append(row)
        
        # Create output directory if it doesn't exist
        output_file.parent.mkdir(parents=True, exist_ok=True)
            
        # Wrap data in "controls" key to match existing format
        output_data = {"controls": data}
            
        # Write JSON file
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(output_data, json_file, indent=2)
            
        print(f"Successfully created: {output_file}")
                
    except Exception as e:
        print(f"Error processing controls mapping file: {str(e)}")
        raise

if __name__ == "__main__":
    process_controls_mapping() 