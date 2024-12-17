import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.data_processor import DataProcessor

def main():
    """Process CSV files to JSON format"""
    # Setup paths
    raw_data_path = Path('data/raw')
    processed_data_path = Path('data/processed')
    
    print(f"Processing CSV files from {raw_data_path} to {processed_data_path}")
    
    # Initialize processor
    processor = DataProcessor(raw_data_path, processed_data_path)
    
    try:
        # Convert CSV to JSON
        processor.convert_csv_to_json()
        print("Successfully converted CSV files to JSON format")
        
        # Verify files were created
        expected_files = ['controls_v2.json', 'control_guidance.json']
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