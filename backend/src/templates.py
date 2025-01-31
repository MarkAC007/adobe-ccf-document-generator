"""
Templates Module
===============

Manages policy document templates and provides template rendering capabilities.
Handles template storage, retrieval, and customization.

Future Improvements:
- Add template versioning
- Implement template inheritance
- Add template validation
- Support custom template variables
- Add template preview generation
- Implement template access control
- Add template migration tools

Architecture Notes:
- Could be split into:
    - TemplateRepository (storage/retrieval)
    - TemplateRenderer (rendering logic)
    - TemplateValidator (validation rules)
    - TemplateManager (high-level operations)
- Implement decorator pattern for template customization
- Add visitor pattern for template processing
- Use strategy pattern for different rendering engines
"""

from string import Template
from typing import Dict, List
from datetime import datetime
import re
import json
from pathlib import Path

class PolicyTemplate:
    TEMPLATES_FILE = Path(__file__).parent.parent / 'data' / 'templates.json'
    TEMPLATES = {
        "standard": {
            "name": "Standard Policy Template",
            "description": "Default template with standard policy sections",
            "content": """# ${policy_standard}

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

## Crosswalk: Common Controls to External Frameworks

${framework_references}

## Crosswalk: External Frameworks to Common Controls
| **Framework** | **Reference** | **Controls** |
|:----------|:----------|:---------|
${reverse_framework_references}
"""
        },
        "detailed": {
            "name": "Detailed Policy Template",
            "description": "Extended template with additional sections",
            "content": """# ${policy_standard}

## Document Control
- **Version:** 1.0
- **Last Updated:** ${current_date}
- **Classification:** Internal
- **Owner:** Information Security Team
- **Next Review Date:** ${next_review_date}

## Executive Summary
This document outlines the comprehensive requirements for ${policy_standard_lower}. The policy is designed to ensure consistent and secure practices across the organization.

## Purpose and Objectives
This policy defines requirements for ${policy_standard_lower} with the following objectives:
1. Establish clear governance and accountability
2. Ensure regulatory compliance
3. Protect organizational assets and data
4. Enable secure business operations

## Scope
This policy applies to:
- All employees and contractors
- All systems and data
- Third-party service providers
- Business partners with access to systems

## Definitions and Terminology
| **Term** | **Definition** |
|:---------|:--------------|
| Control | A measure designed to provide reasonable assurance regarding the achievement of objectives |
| Policy | A formal statement of rules and requirements that must be met |
| Standard | A mandatory requirement that supports policies |
| Procedure | A documented method to implement policies and standards |

## Policy Requirements

${control_sections}

## Crosswalk: Common Controls to External Frameworks

${framework_references}

## Crosswalk: External Frameworks to Common Controls
| **Framework** | **Reference** | **Controls** |
|:----------|:----------|:---------|
${reverse_framework_references}

## Compliance and Monitoring
### Compliance Measurement
- Regular assessments will be conducted to ensure compliance
- Automated monitoring tools will be used where applicable
- Quarterly compliance reports will be generated

### Non-Compliance
Violations of this policy may result in:
1. Disciplinary action
2. Termination of employment
3. Legal action if warranted

## Review and Updates
- This policy will be reviewed annually
- Updates will be made in response to:
  - Changes in business requirements
  - New security threats
  - Regulatory changes
  - Lessons learned from incidents

## Document History
| **Version** | **Date** | **Changes** | **Approved By** |
|:------------|:---------|:------------|:----------------|
| 1.0 | ${current_date} | Initial Release | Information Security Team |
"""
        }
    }

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

    AVAILABLE_SECTIONS = {
        "document_control": {
            "name": "Document Control",
            "type": "metadata",
            "description": "Track document metadata including version, date, classification, and owner",
            "fields": ["version", "date", "classification", "owner"]
        },
        "executive_summary": {
            "name": "Executive Summary",
            "type": "text",
            "description": "A brief overview of the policy's purpose and key points",
            "placeholder": "Brief overview of the policy"
        },
        "purpose": {
            "name": "Purpose",
            "type": "text",
            "description": "Define the main objectives and goals of this policy",
            "placeholder": "Policy purpose and objectives"
        },
        "scope": {
            "name": "Scope",
            "type": "list",
            "description": "Specify who and what this policy applies to",
            "placeholder": "Define policy scope"
        },
        "definitions": {
            "name": "Definitions",
            "type": "table",
            "description": "Define key terms and concepts used in the policy",
            "columns": ["Term", "Definition"]
        },
        "policy_requirements": {
            "name": "Policy Requirements",
            "type": "controls",
            "description": "Core policy controls and requirements",
            "required": True
        },
        "framework_references": {
            "name": "Framework References",
            "type": "table",
            "description": "Map policy controls to compliance frameworks",
            "required": True
        },
        "compliance": {
            "name": "Compliance and Monitoring",
            "type": "sections",
            "description": "Define how compliance will be measured and enforced",
            "subsections": ["Measurement", "Non-Compliance"]
        },
        "review": {
            "name": "Review and Updates",
            "type": "list",
            "description": "Specify review cycle and update procedures"
        }
    }

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

    def __init__(self, template_id="standard"):
        self.template_id = template_id
        self.template = self.TEMPLATES[template_id]["content"]

    @classmethod
    def get_available_templates(cls):
        """Return list of available templates with metadata"""
        return {
            template_id: {
                "name": template["name"],
                "description": template["description"],
                "sections": cls.get_template_sections(template_id)
            }
            for template_id, template in cls.TEMPLATES.items()
        }

    @classmethod
    def get_template_sections(cls, template_id: str) -> List[str]:
        """Get main sections from template"""
        template = cls.TEMPLATES.get(template_id, cls.TEMPLATES["standard"])
        content = template["content"]
        # Extract section headers (##)
        sections = [
            section.strip().split('\n')[0].replace('##', '').strip()
            for section in content.split('##')
            if section.strip() and not section.startswith('#')
        ]
        return sections

    @classmethod
    def render(cls, data: Dict, template_id: str = "standard") -> str:
        """Render the policy template with provided data"""
        print(f"Rendering template: {template_id}")  # Debug log
        
        if template_id not in cls.TEMPLATES:
            print(f"Warning: Template {template_id} not found, using standard")
            template_id = "standard"
        
        template_instance = cls(template_id)
        
        # Print template sections for debugging
        sections = [s.strip().split('\n')[0] for s in template_instance.template.split('##') if s.strip()]
        print(f"Template sections: {sections}")
        
        # Render main template
        return Template(template_instance.template).substitute(data)

    @classmethod
    def from_file(cls, template_path: str) -> 'PolicyTemplate':
        """Create template instance from file"""
        with open(template_path, 'r') as f:
            cls.TEMPLATES["standard"]["content"] = f.read()
        return cls

    @classmethod
    def add_template(cls, template_id: str, name: str, description: str, sections: List[Dict]) -> None:
        """Add a new template"""
        if template_id in cls.TEMPLATES:
            raise ValueError(f"Template {template_id} already exists")
        
        # Generate template content from sections
        content = cls._generate_template_content(sections)
        
        cls.TEMPLATES[template_id] = {
            "name": name,
            "description": description,
            "content": content
        }
        
        # Save templates to file
        cls.save_templates()

    @classmethod
    def update_template(cls, template_id: str, updates: Dict) -> None:
        """Update an existing template"""
        if template_id not in cls.TEMPLATES:
            raise ValueError(f"Template {template_id} not found")
        
        if template_id in ["standard", "detailed"]:
            raise ValueError("Cannot modify built-in templates")
        
        if 'sections' in updates:
            updates['content'] = cls._generate_template_content(updates['sections'])
        
        cls.TEMPLATES[template_id].update(updates)
        
        # Save templates to file
        cls.save_templates()

    @classmethod
    def delete_template(cls, template_id: str) -> None:
        """Delete a template"""
        if template_id in ["standard", "detailed"]:
            raise ValueError("Cannot delete built-in templates")
        if template_id not in cls.TEMPLATES:
            raise ValueError(f"Template {template_id} not found")
        
        del cls.TEMPLATES[template_id]
        
        # Save templates to file
        cls.save_templates()

    @classmethod
    def _generate_template_content(cls, sections: List[Dict]) -> str:
        """Generate template content from section configurations"""
        content_parts = ["# ${policy_standard}\n"]
        
        for section in sections:
            section_type = section['type']
            section_config = cls.AVAILABLE_SECTIONS[section_type]
            
            content_parts.append(f"## {section_config['name']}\n")
            
            # Add appropriate content based on section type
            if section_type == "metadata":
                for field in section_config['fields']:
                    content_parts.append(f"- **{field.title()}:** ${{{field}}}")
            
            elif section_type == "executive_summary":
                content_parts.append("This document outlines the comprehensive requirements for ${policy_standard_lower}. "
                                   "The policy is designed to ensure consistent and secure practices across the organization.")
            
            elif section_type == "purpose":
                content_parts.append("This policy defines requirements for ${policy_standard_lower} with the following objectives:")
                content_parts.append("1. Establish clear governance and accountability")
                content_parts.append("2. Ensure regulatory compliance")
                content_parts.append("3. Protect organizational assets and data")
                content_parts.append("4. Enable secure business operations")
            
            elif section_type == "scope":
                content_parts.append("This policy applies to:")
                content_parts.append("- All employees and contractors")
                content_parts.append("- All systems and data")
                content_parts.append("- Third-party service providers")
                content_parts.append("- Business partners with access to systems")
            
            elif section_type == "definitions":
                content_parts.append("| **Term** | **Definition** |")
                content_parts.append("|:---------|:--------------|")
                content_parts.append("| Control | A measure designed to provide reasonable assurance regarding the achievement of objectives |")
                content_parts.append("| Policy | A formal statement of rules and requirements that must be met |")
                content_parts.append("| Standard | A mandatory requirement that supports policies |")
                content_parts.append("| Procedure | A documented method to implement policies and standards |")
            
            elif section_type == "policy_requirements":
                content_parts.append("${control_sections}")
            
            elif section_type == "framework_references":
                content_parts.append("${framework_references}")
            
            elif section_type == "compliance":
                content_parts.append("### Compliance Measurement")
                content_parts.append("- Regular assessments will be conducted to ensure compliance")
                content_parts.append("- Automated monitoring tools will be used where applicable")
                content_parts.append("- Quarterly compliance reports will be generated")
                content_parts.append("\n### Non-Compliance")
                content_parts.append("Violations of this policy may result in:")
                content_parts.append("1. Disciplinary action")
                content_parts.append("2. Termination of employment")
                content_parts.append("3. Legal action if warranted")
            
            elif section_type == "review":
                content_parts.append("- This policy will be reviewed annually")
                content_parts.append("- Updates will be made in response to:")
                content_parts.append("  - Changes in business requirements")
                content_parts.append("  - New security threats")
                content_parts.append("  - Regulatory changes")
                content_parts.append("  - Lessons learned from incidents")
            
            content_parts.append("")  # Add blank line between sections
        
        return "\n".join(content_parts)

    @classmethod
    def get_template_details(cls, template_id: str) -> Dict:
        """Get detailed template information including section configurations"""
        if template_id not in cls.TEMPLATES:
            raise ValueError(f"Template {template_id} not found")
        
        template = cls.TEMPLATES[template_id]
        
        # Parse the template content to extract section configurations
        content = template["content"]
        sections = []
        
        # Extract sections and their configurations
        for section in content.split('##'):
            if not section.strip():
                continue
            
            lines = section.strip().split('\n')
            section_name = lines[0].strip()
            
            # Determine section type and configuration
            section_type = None
            config = {}
            
            for section_id, section_info in cls.AVAILABLE_SECTIONS.items():
                if section_info['name'] == section_name:
                    section_type = section_id
                    config = section_info.copy()
                    break
            
            if section_type:
                sections.append({
                    "type": section_type,
                    "config": config,
                    "content": '\n'.join(lines[1:]).strip()
                })
        
        return {
            "id": template_id,
            "name": template["name"],
            "description": template["description"],
            "sections": sections
        }

    @classmethod
    def load_templates(cls):
        """Load templates from file"""
        try:
            if cls.TEMPLATES_FILE.exists():
                with open(cls.TEMPLATES_FILE, 'r') as f:
                    stored_templates = json.load(f)
                    # Merge with default templates, preserving built-in ones
                    cls.TEMPLATES = {**stored_templates, **cls.TEMPLATES}
        except Exception as e:
            print(f"Error loading templates: {e}")

    @classmethod
    def save_templates(cls):
        """Save templates to file"""
        try:
            # Create data directory if it doesn't exist
            cls.TEMPLATES_FILE.parent.mkdir(parents=True, exist_ok=True)
            
            # Filter out built-in templates before saving
            custom_templates = {k: v for k, v in cls.TEMPLATES.items() 
                             if k not in ["standard", "detailed"]}
            
            with open(cls.TEMPLATES_FILE, 'w') as f:
                json.dump(custom_templates, f, indent=2)
        except Exception as e:
            print(f"Error saving templates: {e}")
            raise

    def _generate_framework_references_table(self, controls: List[Dict], selected_frameworks: List[str]) -> List[str]:
        """Generate framework references table with frameworks as column headers"""
        # Get unique frameworks and sort them
        frameworks = sorted(set(selected_frameworks))
        
        # Build header rows
        header = ["| Control ID"]
        header.extend([f" | {self._format_framework_name(fw)}" for fw in frameworks])
        header.append(" |")
        
        # Build separator row
        separator = ["|:----------"]
        separator.extend(["|:----------" for _ in frameworks])
        separator.append("|")
        
        table_lines = [
            "## Framework References",
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
            
            for framework in frameworks:
                ref_key = f"{framework}_ref"
                refs = mappings.get(ref_key, [])
                if refs:
                    consolidated_refs[control_id][framework].extend(refs)
        
        # Generate table rows
        for control_id in sorted(consolidated_refs.keys()):
            row = [f"| {control_id}"]
            for framework in frameworks:
                refs = consolidated_refs[control_id][framework]
                ref_string = ", ".join(sorted(set(refs))) if refs else "-"
                row.append(f" | {ref_string}")
            row.append(" |")
            table_lines.append("".join(row))
        
        return table_lines