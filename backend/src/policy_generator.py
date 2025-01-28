import logging
from pathlib import Path
from datetime import datetime
from .templates import PolicyTemplate

class PolicyGenerator:
    def __init__(self, data_processor):
        self.data_processor = data_processor
        self.template = PolicyTemplate()
        
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
