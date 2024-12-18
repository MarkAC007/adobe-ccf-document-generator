from string import Template
from typing import Dict, List
from datetime import datetime
import re

class PolicyTemplate:
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

## Framework References
| **Control ID** | **Framework** | **Reference** |
|:-----------|:----------|:-----------|
${framework_references}

## Framework Reference Mapping
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

## Framework References
| **Control ID** | **Framework** | **Reference** |
|:-----------|:----------|:-----------|
${framework_references}

## Framework Reference Mapping
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