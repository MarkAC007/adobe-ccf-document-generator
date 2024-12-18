# Asset Management Policy

## Document Control
- **Version:** 1.0
- **Last Updated:** 2024-12-18
- **Classification:** Internal
- **Owner:** Information Security Team
- **Next Review Date:** 2025-12-18

## Executive Summary
This document outlines the comprehensive requirements for asset management policy. The policy is designed to ensure consistent and secure practices across the organization.

## Purpose and Objectives
This policy defines requirements for asset management policy with the following objectives:
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

### AM-01 - Inventory Management

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Organization maintains an inventory of information systems, which is reconciled on a periodic basis.

#### Implementation Requirements
1. Design and document a process for maintaining an inventory of information systems for management of assets within an organization.
2. Perform inventory reconciliation on a periodic basis.
3. Create and maintain periodic reconciliation documentation.

#### Testing Procedures
1. Inspect the policy and standard to determine whether requirements for maintaining and reconciling a system of inventory for information systems are defined.
2. Observe the inventory of system devices to determine whether the organization maintains the inventory in a system of record.
3. Inspect periodic reconciliation documentation to determine whether reconciliation was performed.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-AM-01 | Asset Management | Asset Management Policy |
| E-AM-02 | Asset Management | Asset Inventory |
| E-AM-03 | Asset Management | Asset Reconciliation Records |


### AM-02 - Inventory Management: Applications

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Organization maintains an inventory of application assets, which is reconciled on a periodic basis.

#### Implementation Requirements
1. Design and document a process for maintaining an inventory of application assets for management of assets within an organization.
2. Perform inventory reconciliation on a periodic basis.
3. Create and maintain periodic reconciliation documentation.

#### Testing Procedures
1. Inspect the policy and standard to determine whether requirements for maintaining and reconciling a system of inventory for application assets are defined.
2. Observe the inventory of system devices to determine whether the organization maintains the inventory in a system of record.
3. Inspect periodic reconciliation documentation to determine whether reconciliation was performed.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-AM-01 | Asset Management | Asset Management Policy |
| E-AM-02 | Asset Management | Asset Inventory |
| E-AM-03 | Asset Management | Asset Reconciliation Records |


### AM-07 - Asset Transportation Authorization

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Organization authorizes and records the entry and exit of systems at datacenter locations.

#### Implementation Requirements
1. Ensure a process is established and documented to control the transport of assets in and out of data center locations.
2. Ensure appropriate records and approvals are obtained and maintained against entry and exit of each asset.

#### Testing Procedures
1. Inspect the policy and/or standard to determine whether requirements have been established to authorize and record the entry and exit of systems at datacenter locations.
2. Inspect evidence of asset movement from a sample of data centers and colocations.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-AM-01 | Asset Management | Asset Management Policy |
| E-AM-06 | Asset Management | Asset Movement Records |


### AM-10 - Maintenance of Assets

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Equipment maintenance is documented and approved according to management requirements.

#### Implementation Requirements
1. Ensure a process is established and documented for maintenance of assets.
2. Ensure all maintenance is approved by the management and is carried out through approved vendors.
3. Ensure proper testing of equipment is conducted post maintenance before use.

#### Testing Procedures
1. Inspect the policy and/or standard to determine whether management requirements have been established for the documentation and approval of equipment maintenance.
2. Inspect equipment maintenance requests to determine whether equipment maintenance is documented and approved according to management requirements.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-AM-01 | Asset Management | Asset Management Policy |
| E-AM-08 | Asset Management | Asset Maintenance Records |


## Framework References
| **Control ID** | **Framework** | **Reference** |
|:-----------|:----------|:-----------|
| AM-01 | NIST CSF | ID.AM-1, ID.AM-2 |
| AM-02 | NIST CSF | ID.AM-1, ID.AM-2 |
| AM-07 | NIST CSF | ID.AM-4, PR.DS-3 |
| AM-10 | NIST CSF | PR.DS-8, PR.MA-1 |

## Framework Reference Mapping
| **Framework** | **Reference** | **Controls** |
|:----------|:----------|:---------|
| NIST CSF | ID.AM-1 | AM-01, AM-02 |
| NIST CSF | ID.AM-2 | AM-01, AM-02 |
| NIST CSF | ID.AM-4 | AM-07 |
| NIST CSF | PR.DS-3 | AM-07 |
| NIST CSF | PR.DS-8 | AM-10 |
| NIST CSF | PR.MA-1 | AM-10 |

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
| 1.0 | 2024-12-18 | Initial Release | Information Security Team |
