import logging
from pathlib import Path
from datetime import datetime
from .templates import PolicyTemplate

# Add BACKEND_DIR definition
BACKEND_DIR = Path(__file__).parent.parent

class PolicyGenerator:
    def __init__(self, data_processor=None):
        """Initialize PolicyGenerator with optional data processor"""
        if data_processor is None:
            # Create default data processor if none provided
            from src.data_processor import DataProcessor
            
            # Fix path construction - only use controls_v2.json
            raw_data_path = Path(BACKEND_DIR) / 'data' / 'processed' / 'controls_v2.json'
            processed_data_path = raw_data_path  # Use same file for both since we don't need preprocessing
            
            print(f"\n=== PolicyGenerator Initialization ===")
            print(f"Raw data path: {raw_data_path}")
            print(f"Checking if file exists: {raw_data_path.exists()}")
            
            if not raw_data_path.exists():
                raise FileNotFoundError(f"Controls data file not found at: {raw_data_path}")
            
            data_processor = DataProcessor(
                raw_data_path=raw_data_path,
                processed_data_path=processed_data_path
            )
        self.data_processor = data_processor
        self.template = PolicyTemplate()
        
    def generate_policy(self, config_data, output_format='md'):
        """Generate a policy document based on the provided configuration"""
        # Original policy generation code
        return self.generate_policy_document(config_data)

    def generate_policy_document(self, config: dict) -> str:
        """Generate a policy document based on the provided configuration"""
        
        # Get current date for versioning
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # Get controls data
        controls_data = self.data_processor.get_processed_controls()
        
        # Build policy statements from controls
        policy_statements = []
        implementation_reqs = []
        
        for control_id in config['expected_controls']:
            control = next((c for c in controls_data['controls'] if c['ccf_id'] == control_id), None)
            if control:
                # Add control title and description to policy statements
                policy_statements.append(f"### {control_id}: {control.get('control_name', '')}")
                policy_statements.append(control.get('control_description', ''))
                policy_statements.append("")  # Add blank line for readability
                
                if config['test_parameters'].get('include_implementation_guidance', False):
                    implementation_reqs.append(f"\n### {control_id}")
                    # Get implementation guidance and format it properly
                    guidance = control.get('implementation_guidance', '')
                    if guidance:
                        # Split guidance into numbered steps and format each step
                        steps = [step.strip() for step in guidance.split('.') if step.strip()]
                        formatted_steps = []
                        for step in steps:
                            if step[0].isdigit():  # If step starts with a number, remove it and any separator
                                step = step.split(' ', 1)[1] if ' ' in step else step
                            formatted_steps.append(f"- {step}")
                        implementation_reqs.append("\n".join(formatted_steps))
                    implementation_reqs.append("")  # Add blank line between controls
        
        # Build framework reference table
        compliance_mapping = []
        compliance_mapping.append("| Control ID | Framework | Reference |")
        compliance_mapping.append("|------------|-----------|------------|")
        
        # Add framework mappings for each control
        for control_id in config['expected_controls']:
            control = next((c for c in controls_data['controls'] if c['ccf_id'] == control_id), None)
            if control:
                for framework in config['selected_frameworks']:
                    ref_field = f"{framework}_ref"
                    refs = control.get(ref_field, [])
                    if refs and not isinstance(refs, list):
                        refs = [refs]  # Convert single value to list
                    if refs:
                        for ref in refs:
                            if ref:  # Only add non-empty references
                                compliance_mapping.append(f"| {control_id} | {framework} | {ref} |")
        
        # Use the template with all required parameters
        document = self.template.template.format(
            policy_name=config['policy_standard'],
            date=current_date,
            purpose="This policy defines the requirements and responsibilities for managing access to organizational assets and information systems.",
            scope="This policy applies to all employees, contractors, and third parties who require access to organizational systems and data.",
            policy_statements="\n".join(policy_statements),
            implementation_requirements="\n".join(implementation_reqs),
            compliance_mapping="\n".join(compliance_mapping)
        )
        
        return document
    
    def save_policy_document(self, document: str, output_path: Path) -> Path:
        """Save the generated policy document to a file"""
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Generate filename based on policy name and date
        safe_name = document.split('\n')[0].replace('#', '').strip().lower().replace(' ', '_')
        filename = f"{safe_name}_{datetime.now().strftime('%Y%m%d')}.md"
        
        file_path = output_path / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(document)
        
        return file_path

    def generate_framework_mapping(self, selected_frameworks):
        """Generate framework mapping table without policy filtering"""
        try:
            print("\n=== Starting Framework Mapping Generation ===")
            # Get controls data using the data processor
            print("Getting controls data from processor...")
            controls_data = self.data_processor.get_processed_controls()
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
                    mapped_controls.append(control)
            
            print(f"Found {len(mapped_controls)} controls with framework mappings")
            
            # Generate markdown table
            print("\nGenerating markdown table...")
            table = "| Control ID | Description | " + " | ".join(selected_frameworks) + " |\n"
            table += "|" + "---|" * (len(selected_frameworks) + 2) + "\n"
            
            for control in sorted(mapped_controls, key=lambda x: x['ccf_id']):
                row = [
                    control['ccf_id'],
                    control.get('control_name', '').split('\n')[0]
                ]
                
                for framework in selected_frameworks:
                    refs = control.get('framework_refs', {}).get(framework, [])
                    row.append(", ".join(refs) if refs else "-")
                
                table += "| " + " | ".join(row) + " |\n"
            
            print("Table generation complete")
            return table

        except Exception as e:
            print(f"\n=== Error in Framework Mapping Generation ===")
            print(f"Error type: {type(e)}")
            print(f"Error message: {str(e)}")
            print(f"Error location: {e.__traceback__.tb_frame.f_code.co_filename}:{e.__traceback__.tb_lineno}")
            raise Exception(f"Error generating framework mapping: {str(e)}")

    def convert_mapping_to_docx(self, markdown_content):
        """Convert markdown mapping table to DOCX format"""
        try:
            # Implementation of DOCX conversion
            # This would use python-docx or similar library
            pass
        except Exception as e:
            raise Exception(f"Error converting to DOCX: {str(e)}")
