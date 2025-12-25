import json
import argparse
from typing import Dict, List
from datetime import datetime
from pathlib import Path
import re
import sys
from string import Template

# Add the parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

from src.templates import PolicyTemplate
from src.document_converter import DocumentConverter

class PolicyGenerator:
    def __init__(self, template_path: str = None):
        """Initialize with both control guidance and mapping data"""
        # Get the base directory
        base_dir = Path(__file__).parent.parent
        
        # Load control guidance
        with open(base_dir / 'data/processed/control_guidance.json', 'r') as f:
            self.control_guidance = json.load(f)
        
        # Load control data
        with open(base_dir / 'data/processed/controls_v2.json', 'r') as f:
            self.controls_data = json.load(f)
        
        # Load control mappings
        with open(base_dir / 'data/processed/controls_mapping.json', 'r') as f:
            self.controls_mapping = json.load(f)
        
        # Load evidence requirement library
        with open(base_dir / 'data/processed/erl.json', 'r') as f:
            self.erl_data = json.load(f)
        
        # Initialize template
        self.template = PolicyTemplate
        if template_path:
            self.template = PolicyTemplate.from_file(template_path)

    def _get_framework_field(self, framework: str) -> str:
        """Convert framework name to the corresponding field name in the data"""
        return f"{framework}_ref"

    def _control_matches_frameworks(self, control: Dict, selected_frameworks: List[str]) -> bool:
        """Check if control has mappings for any of the selected frameworks"""
        control_id = control.get("ccf_id")
        if not control_id:
            return False
            
        mappings = self.controls_mapping.get(control_id, {})
        
        for framework in selected_frameworks:
            ref_key = f"{framework}_ref"
            
            # Check for mappings in either source
            has_mapping = bool(mappings.get(ref_key)) or bool(control.get(ref_key))
            
            if has_mapping:
                print(f"Control {control_id} matched framework {framework}")
                return True
            
        return False

    def _get_controls_for_domain(self, policy_standard: str, selected_frameworks: List[str]) -> List[Dict]:
        """Get controls for domain that have mappings to selected frameworks"""
        matching_controls = []
        print(f"\nProcessing controls for {policy_standard}")
        
        # Get all controls for the domain from control_guidance
        controls_list = self.control_guidance.get("controls", [])
        for control in controls_list:
            if control.get("policy_standard") == policy_standard:
                # Check framework mappings first
                if self._control_matches_frameworks(control, selected_frameworks):
                    # Get evidence details
                    audit_artifacts = control.get('audit_artifacts', [])
                    evidence_details = self._get_evidence_details(audit_artifacts)
                    
                    # Only enrich control data if it matches frameworks
                    enriched_control = {
                        'ccf_id': control.get('ccf_id'),
                        'control_name': control.get('control_name'),
                        'control_description': control.get('control_description'),
                        'implementation_guidance': control.get('implementation_guidance'),
                        'control_theme': control.get('control_theme'),
                        'control_type': control.get('control_type'),
                        'testing_procedure': control.get('testing_procedure'),
                        'evidence_details': evidence_details
                    }
                    matching_controls.append(enriched_control)
                    print(f"Added control {control.get('ccf_id')} to policy")
                else:
                    print(f"Skipped control {control.get('ccf_id')}: no framework mappings")
        
        print(f"Found {len(matching_controls)} matching controls")
        return matching_controls

    def _get_framework_references(self, control_id: str, frameworks: List[str]) -> List[str]:
        """Get framework references for a control"""
        # Create a dictionary to group references by framework
        framework_refs = {}
        
        if control_id in self.controls_mapping:
            control_data = self.controls_mapping[control_id]
            for framework in frameworks:
                framework_field = self._get_framework_field(framework)
                refs = control_data.get(framework_field, [])
                if refs:
                    framework_name = self._format_framework_name(framework)
                    # Store framework name and its references
                    framework_refs[framework_name] = refs
        
        # Format consolidated references
        table_rows = []
        for framework, refs in framework_refs.items():
            # Join all references with commas
            ref_string = ', '.join(refs)
            table_rows.append(f"| {control_id} | {framework} | {ref_string} |")
            
        return table_rows

    def _format_framework_name(self, framework: str) -> str:
        """Convert framework ID to readable name"""
        framework_names = {
            "nist_cybersecurity": "NIST CSF",
            "iso_27001": "ISO 27001",
            "pci_dss_v4": "PCI DSS v4",
            "iso_27002": "ISO 27002",
            "iso_27017": "ISO 27017",
            "iso_27018": "ISO 27018",
            "fedramp_moderate": "FedRAMP Moderate",
            "fedramp_tailored": "FedRAMP Tailored",
            "hipaa_security": "HIPAA Security",
            "soc_2": "SOC 2",
            "cis_v8": "CIS v8",
            "bsi_c5": "BSI C5",
            "mlps": "MLPS",
            "iso_22301": "ISO 22301",
            "cyber_essentials_uk": "Cyber Essentials (UK)",
            "ens": "ENS",
            "tx_ramp_L1": "TX-RAMP Level 1",
            "irap": "IRAP",
            "ismap": "ISMAP",
            "mas": "MAS",
            "kfsi": "K-FSI"
        }
        return framework_names.get(framework, framework)

    def _generate_framework_references_table(self, controls: List[Dict], selected_frameworks: List[str]) -> str:
        """Generate framework references table with frameworks as column headers"""
        # Get unique frameworks and sort them
        frameworks = sorted(set(selected_frameworks))
        
        # Build header rows with proper framework display names
        header = ["| Control ID"]
        header.extend([f" | {self._format_framework_name(fw)}" for fw in frameworks])
        header.append(" |")
        
        # Build separator row with proper alignment
        separator = ["|:-----------|"]  # Left align Control ID
        separator.extend([":----------:|" for _ in frameworks])  # Center align framework columns
        separator[-1] = separator[-1][:-1] + "|"  # Fix last separator
        
        table_lines = [
            "".join(header),
            "".join(separator)
        ]
        
        # Build consolidated references by control ID
        consolidated_refs = {}
        for control in controls:
            control_id = control.get("ccf_id")
            if not control_id:
                continue
            
            mappings = self.controls_mapping.get(control_id, {})
            if control_id not in consolidated_refs:
                consolidated_refs[control_id] = {fw: [] for fw in frameworks}
            
            # Process each framework's references
            for framework in frameworks:
                ref_key = f"{framework}_ref"
                refs = mappings.get(ref_key, [])
                if refs:
                    # Sort and deduplicate references
                    consolidated_refs[control_id][framework] = sorted(set(refs))
        
        # Generate table rows
        for control_id in sorted(consolidated_refs.keys()):
            row = [f"| {control_id}"]
            for framework in frameworks:
                refs = consolidated_refs[control_id][framework]
                # Format references with proper spacing and handling of empty values
                ref_string = ", ".join(refs) if refs else "-"
                row.append(f" | {ref_string}")
            row.append(" |")
            table_lines.append("".join(row))
        
        return "\n".join(table_lines)

    def _format_control_sections(self, controls: List[Dict]) -> str:
        """Format control sections using the template"""
        control_sections = []
        for control in controls:
            # Format numbered lists
            implementation = PolicyTemplate._format_numbered_list(control.get('implementation_guidance', ''))
            testing = PolicyTemplate._format_numbered_list(control.get('testing_procedure', ''))
            
            # Format evidence table rows
            evidence_rows = []
            for evidence in control.get('evidence_details', []):
                evidence_rows.append(
                    f"| {evidence['id']} | {evidence['domain']} | {evidence['title']} |"
                )
            evidence_table = '\n'.join(evidence_rows) if evidence_rows else '| - | - | - |'
            
            # Prepare control section data
            control_data = {
                'control_id': control.get('ccf_id', ''),
                'control_name': control.get('control_name', ''),
                'control_theme': control.get('control_theme', ''),
                'control_type': control.get('control_type', ''),
                'policy_description': control.get('control_description', ''),
                'formatted_implementation': implementation,
                'formatted_testing': testing,
                'evidence_table': evidence_table
            }
            
            # Render control section
            control_section = Template(PolicyTemplate.CONTROL_SECTION_TEMPLATE).substitute(control_data)
            control_sections.append(control_section)
        
        return '\n\n'.join(control_sections)

    def generate_policy_markdown(self, config: Dict) -> str:
        """Generate markdown content for policy"""
        policy_standard = config["policy_standard"]
        selected_frameworks = config.get("selected_frameworks", [])
        template_id = config.get("template_id", "standard")
        
        print(f"Generating policy with template: {template_id}")  # Debug log
        
        # Get controls and sort them
        controls = self._get_controls_for_domain(policy_standard, selected_frameworks)
        controls.sort(key=lambda x: x.get("ccf_id", ""))
        
        # Calculate dates
        current_date = datetime.now().strftime("%Y-%m-%d")
        next_review = datetime.now().replace(year=datetime.now().year + 1)
        next_review_date = next_review.strftime("%Y-%m-%d")
        
        # Format control sections
        control_sections = self._format_control_sections(controls)
        
        # Generate framework references with new format
        framework_references = self._generate_framework_references_table(controls, selected_frameworks)
        
        # Prepare template data
        template_data = {
            "policy_standard": policy_standard,
            "policy_standard_lower": policy_standard.lower(),
            "current_date": current_date,
            "next_review_date": next_review_date,
            "control_sections": control_sections,
            "framework_references": framework_references,
            "reverse_framework_references": '\n'.join(self._get_reverse_framework_references(controls, selected_frameworks))
        }
        
        # Render template with specified template_id
        return self.template.render(template_data, template_id)

    def _get_all_framework_references(self, controls: List[Dict], frameworks: List[str]) -> List[str]:
        """Get all framework references for controls"""
        # Dictionary to store consolidated references
        consolidated_refs = {}
        
        for control in controls:
            control_id = control.get("ccf_id")
            if not control_id:
                continue
                
            if control_id in self.controls_mapping:
                control_data = self.controls_mapping[control_id]
                for framework in frameworks:
                    framework_field = self._get_framework_field(framework)
                    refs = control_data.get(framework_field, [])
                    if refs:
                        framework_name = self._format_framework_name(framework)
                        # Create key for control-framework pair
                        key = (control_id, framework_name)
                        if key not in consolidated_refs:
                            consolidated_refs[key] = []
                        consolidated_refs[key].extend(refs)
        
        # Format into table rows
        table_rows = []
        # Sort by control ID and framework
        for (control_id, framework), refs in sorted(consolidated_refs.items()):
            # Remove duplicates and sort references
            unique_refs = sorted(set(refs))
            ref_string = ', '.join(unique_refs)
            table_rows.append(f"| {control_id} | {framework} | {ref_string} |")
        
        return table_rows

    def generate_policy(self, config: Dict, output_format: str = 'md'):
        """Generate policy and save to file"""
        # Generate markdown content
        md_content = self.generate_policy_markdown(config)
        
        # Create output directory with proper permissions
        output_dir = Path("output/policies")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate base filename (include template_id in filename)
        domain_name = config["policy_standard"].lower().replace(" ", "_")
        template_id = config.get("template_id", "standard")
        current_date = datetime.now().strftime("%Y%m%d")
        base_filename = f"{domain_name}_{template_id}_{current_date}"
        
        # Save markdown first
        md_path = output_dir / f"{base_filename}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        
        if output_format.lower() == 'docx':
            # Convert markdown to Word
            docx_path = output_dir / f"{base_filename}.docx"
            converter = DocumentConverter()
            output_path = converter.markdown_to_docx(md_path, docx_path)
            return str(output_path)
        
        return str(md_path)

    def _get_evidence_details(self, evidence_ids: List[str]) -> List[Dict[str, str]]:
        """Get evidence details from ERL data"""
        evidence_details = []
        for eid in evidence_ids:
            if eid in self.erl_data:
                evidence_details.append({
                    'id': eid,
                    'domain': self.erl_data[eid].get('evidence_domain', ''),
                    'title': self.erl_data[eid].get('evidence_title', '')
                })
        return evidence_details

    def _get_reverse_framework_references(self, controls: List[Dict], frameworks: List[str]) -> List[str]:
        """Get reverse framework mapping (framework ref -> controls)"""
        # Dictionary to store reverse mappings
        reverse_refs = {}
        
        for control in controls:
            control_id = control.get("ccf_id")
            if not control_id or control_id not in self.controls_mapping:
                continue
                
            control_data = self.controls_mapping[control_id]
            for framework in frameworks:
                framework_field = self._get_framework_field(framework)
                refs = control_data.get(framework_field, [])
                if refs:
                    framework_name = self._format_framework_name(framework)
                    # For each reference, store the control ID
                    for ref in refs:
                        key = (framework_name, ref)
                        if key not in reverse_refs:
                            reverse_refs[key] = []
                        reverse_refs[key].append(control_id)
        
        # Format into table rows
        table_rows = []
        # Sort by framework and reference
        for (framework, ref), controls in sorted(reverse_refs.items()):
            # Remove duplicates and sort controls
            unique_controls = sorted(set(controls))
            controls_string = ', '.join(unique_controls)
            table_rows.append(f"| {framework} | {ref} | {controls_string} |")
        
        return table_rows

    def generate_policy_document(self, config: dict) -> str:
        """Generate policy document based on configuration"""
        template_id = config.get('template_id', 'standard')
        # ... rest of the existing generation logic ...
        return PolicyTemplate.render(template_data, template_id)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate policy document from configuration')
    parser.add_argument('config_file', help='Path to the configuration JSON file')
    args = parser.parse_args()

    # Validate and resolve the config file path securely
    config_path = Path(args.config_file).resolve()

    # Security: Ensure path is a regular file and exists
    if not config_path.exists():
        print(f"Error: Config file '{args.config_file}' not found")
        exit(1)
    if not config_path.is_file():
        print(f"Error: '{args.config_file}' is not a regular file")
        exit(1)
    if config_path.suffix.lower() != '.json':
        print(f"Error: Config file must be a JSON file (got '{config_path.suffix}')")
        exit(1)

    # Load configuration from file
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Config file '{args.config_file}' is not valid JSON")
        exit(1)

    # Validate required fields
    required_fields = ['policy_standard', 'selected_frameworks']
    missing_fields = [field for field in required_fields if field not in config]
    if missing_fields:
        print(f"Error: Missing required fields in config: {', '.join(missing_fields)}")
        exit(1)

    # Create policy generator and generate policy
    generator = PolicyGenerator()
    try:
        output_file = generator.generate_policy(config)
        print(f"Policy generated and saved to: {output_file}")
    except Exception as e:
        print(f"Error generating policy: {str(e)}")
        exit(1)