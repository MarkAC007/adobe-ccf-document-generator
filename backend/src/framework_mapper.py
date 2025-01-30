import logging
from pathlib import Path
from datetime import datetime
from .data_processor import DataProcessor
import json

BACKEND_DIR = Path(__file__).parent.parent

class FrameworkMapper:
    def __init__(self):
        """Initialize FrameworkMapper"""
        # Create framework name mapping
        self.framework_names = {
            'nist_cybersecurity': 'NIST CSF',
            'iso_27001': 'ISO 27001',
            'iso_27002': 'ISO 27002',
            'iso_27017': 'ISO 27017',
            'iso_27018': 'ISO 27018',
            'fedramp_moderate': 'FedRAMP Moderate',
            'fedramp_tailored': 'FedRAMP Tailored',
            'hipaa_security': 'HIPAA Security',
            'soc_2': 'SOC 2',
            'cis_v8': 'CIS v8',
            'bsi_c5': 'BSI C5',
            'mlps': 'MLPS',
            'iso_22301': 'ISO 22301',
            'cyber_essentials_uk': 'Cyber Essentials (UK)',
            'ens': 'ENS',
            'tx_ramp_L1': 'TX-RAMP Level 1',
            'irap': 'IRAP',
            'ismap': 'ISMAP',
            'mas': 'MAS',
            'kfsi': 'K-FSI',
            'pci_dss_v4': 'PCI DSS v4'
        }
        
        # Create data processor with correct path
        controls_file = Path(BACKEND_DIR) / 'data' / 'processed' / 'controls_v2.json'
        
        print(f"\n=== FrameworkMapper Initialization ===")
        print(f"Controls file path: {controls_file}")
        print(f"Checking if file exists: {controls_file.exists()}")
        
        if not controls_file.exists():
            raise FileNotFoundError(f"Controls data file not found at: {controls_file}")
        
        # Pass the same path for both parameters since we're reading directly from the file
        self.data_processor = DataProcessor(
            raw_data_path=str(controls_file),  # Convert Path to string
            processed_data_path=str(controls_file)  # Convert Path to string
        )
        print("DataProcessor initialized successfully")

    def get_friendly_name(self, framework_id):
        """Get friendly name for a framework ID"""
        return self.framework_names.get(framework_id, framework_id)

    def generate_mapping(self, selected_frameworks):
        """Generate framework mapping table"""
        try:
            print("\n=== Starting Framework Mapping Generation ===")
            # Get controls data using the data processor
            print("Getting controls data from processor...")
            controls_data = self.data_processor.get_processed_controls()
            
            # Get control guidance data for policy standards
            guidance_path = Path(BACKEND_DIR) / 'data' / 'processed' / 'control_guidance.json'
            with open(guidance_path, 'r', encoding='utf-8') as f:
                guidance_data = json.load(f)
            
            # Create guidance lookup by ccf_id
            guidance_lookup = {
                control['ccf_id']: control['policy_standard']
                for control in guidance_data['controls']
            }
            
            if not controls_data or 'controls' not in controls_data:
                raise ValueError("Invalid controls data format")
            
            print(f"Retrieved {len(controls_data.get('controls', []))} controls")
            
            # Filter controls that have mappings to selected frameworks
            print(f"\nFiltering controls for frameworks: {selected_frameworks}")
            mapped_controls = []
            for control in controls_data['controls']:
                framework_refs = {}
                for framework in selected_frameworks:
                    ref_field = f"{framework}_ref"
                    if ref_field in control:
                        refs = control[ref_field]
                        if refs:
                            if not isinstance(refs, list):
                                refs = [refs]
                            framework_refs[framework] = refs
                
                if any(framework in framework_refs for framework in selected_frameworks):
                    control['framework_refs'] = framework_refs
                    # Add policy standard from guidance
                    control['policy_standard'] = guidance_lookup.get(control['ccf_id'], 'N/A')
                    mapped_controls.append(control)
            
            print(f"Found {len(mapped_controls)} controls with framework mappings")
            
            # Generate markdown table with policy standard column
            print("\nGenerating markdown table...")
            table = "| Control ID | Control Name | Document Name | " + " | ".join(self.get_friendly_name(f) for f in selected_frameworks) + " |\n"
            table += "|" + "---|" * (len(selected_frameworks) + 3) + "\n"
            
            for control in sorted(mapped_controls, key=lambda x: x['ccf_id']):
                row = [
                    control['ccf_id'],
                    control.get('control_name', '').split('\n')[0],
                    control.get('policy_standard', 'N/A')
                ]
                
                for framework in selected_frameworks:
                    refs = control.get('framework_refs', {}).get(framework, [])
                    row.append(", ".join(refs) if refs else "-")
                
                table += "| " + " | ".join(row) + " |\n"
            
            print("Table generation complete")
            
            # Add title and summary
            title = f"Framework Mapping Analysis ({datetime.now().strftime('%Y-%m-%d')})\n\n"
            summary = "### Summary\n"
            summary += f"Total Controls Mapped: {len(mapped_controls)}\n\n"
            
            # Add framework coverage stats with friendly names
            for framework in selected_frameworks:
                friendly_name = self.get_friendly_name(framework)
                controls_with_refs = sum(1 for c in mapped_controls if c['framework_refs'].get(framework))
                coverage = (controls_with_refs / len(mapped_controls)) * 100
                summary += f"- {friendly_name}: {controls_with_refs} controls ({coverage:.1f}%)\n"
            
            summary += "\n### Mapping Table\n"
            
            # Combine all parts
            return title + summary + table

        except Exception as e:
            print(f"\n=== Error in Framework Mapping Generation ===")
            print(f"Error type: {type(e)}")
            print(f"Error message: {str(e)}")
            print(f"Error location: {e.__traceback__.tb_frame.f_code.co_filename}:{e.__traceback__.tb_lineno}")
            raise Exception(f"Error generating framework mapping: {str(e)}") 