import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.data_processor import DataProcessor

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

def main():
    """Process CSV files to JSON format"""
    # Setup paths - use project_root to make paths absolute
    raw_data_path = project_root / 'data/raw'
    processed_data_path = project_root / 'data/processed'
    
    print(f"Processing CSV files from {raw_data_path} to {processed_data_path}")
    
    # Initialize processor
    processor = DataProcessor(raw_data_path, processed_data_path)
    
    try:
        # Add field processing to DataProcessor before conversion
        processor.process_field = lambda field, value: (
            process_ref_field(value) if field.endswith('_ref')
            else 'X' if value == 'X'
            else '' if not value
            else value.strip()
        )
        
        # Convert CSV to JSON
        processor.convert_csv_to_json()
        print("Successfully converted CSV files to JSON format")
        
        # Verify files were created
        expected_files = ['controls_v2.json', 'control_guidance.json', 'controls_mapping.json']
        for file in expected_files:
            json_path = processed_data_path / file
            if json_path.exists():
                print(f"Created: {json_path}")
            else:
                print(f"Warning: {file} was not created")
                
    except Exception as e:
        print(f"Error processing CSV files: {str(e)}")
        raise

if __name__ == "__main__":
    main() 