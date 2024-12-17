from string import Template
from typing import Dict, List
from datetime import datetime
import re

class PolicyTemplate:
    DEFAULT_TEMPLATE = """# ${policy_standard}

## Document Control
- **Version:** 1.0
- **Last Updated:** ${current_date}
- **Classification:** Internal

## Purpose
This policy defines requirements for ${policy_standard_lower}.

## Scope
This policy applies to all systems and data.

## Policy Requirements

${control_sections}

## Framework References
| **Control ID** | **Framework** | **Reference** |
|:-----------|:----------|:-----------|
${framework_references}

## Framework Reference Mapping
| **Framework** | **Reference** | **Controls** |
|:----------|:----------|:---------|
${reverse_framework_references}
"""

    CONTROL_SECTION_TEMPLATE = """### ${control_id} - ${control_name}

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| ${control_type} | ${control_theme} |

#### Policy Description
${policy_description}

#### Implementation Requirements
${formatted_implementation}

#### Testing Procedures
${formatted_testing}

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
${evidence_table}
"""

    @classmethod
    def _format_numbered_list(cls, text: str) -> str:
        """Format text into a properly numbered list"""
        if not text:
            return ""
        
        # Split on numbers followed by dot or period, or on newlines
        items = re.split(r'\d+\.\s*|\n+', text)
        # Filter empty items and clean whitespace
        items = [item.strip() for item in items if item.strip()]
        
        # Format as numbered list
        return '\n'.join(f"{i+1}. {item}" for i, item in enumerate(items))

    @classmethod
    def render(cls, data: Dict) -> str:
        """Render the policy template with provided data"""
        # Add current date to template data
        data['current_date'] = datetime.now().strftime("%Y-%m-%d")
        
        # Prepare control sections
        control_sections = []
        for control in data.get('controls', []):
            # Format numbered lists
            implementation = cls._format_numbered_list(control.get('implementation_guidance', ''))
            testing = cls._format_numbered_list(control.get('testing_procedure', ''))
            
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
            control_section = Template(cls.CONTROL_SECTION_TEMPLATE).substitute(control_data)
            control_sections.append(control_section)

        # Render main template
        return Template(cls.DEFAULT_TEMPLATE).substitute(
            policy_standard=data['policy_standard'],
            policy_standard_lower=data['policy_standard'].lower(),
            current_date=data['current_date'],
            control_sections='\n\n'.join(control_sections),
            framework_references='\n'.join(data.get('framework_references', [])),
            reverse_framework_references='\n'.join(data.get('reverse_framework_references', []))
        )

    @classmethod
    def from_file(cls, template_path: str) -> 'PolicyTemplate':
        """Create template instance from file"""
        with open(template_path, 'r') as f:
            cls.DEFAULT_TEMPLATE = f.read()
        return cls