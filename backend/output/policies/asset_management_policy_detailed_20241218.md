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


### AM-04 - Inventory Reconciliation: Logging

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Organization reconciles the enterprise log repository against the established device inventory on a quarterly basis; non-inventoried devices are assigned an owner.

#### Implementation Requirements
1. Ensure logs from enterprise logging solutions are reconciled with the system device asset inventory on a quarterly basis.
2. Ensure necessary actions are taken to include non-inventoried assets in the inventory with appropriate ownership details

#### Testing Procedures
1. Inspect the reconciliation report of enterprise log repository against the established device inventory to determine that the inventories are reconciled on a quarterly basis.
2. Inspect the non-inventoried devices to determine that the assets have a designed owner.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-AM-03 | Asset Management | Asset Reconciliation Records |
| E-AM-02 | Asset Management | Asset Inventory |


### AM-05 - Inventory Labels

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Organization assets are labeled and have designated owners.

#### Implementation Requirements
1. Ensure all assets in the system device asset inventory are assigned appropriate labels as per the organization's labelling procedures.
2. Ensure each asset has an assigned owner and accuracy is maintained.

#### Testing Procedures
1. Inspect documentation to determine whether requirements for asset labelling ownership assessment are defined.
2. Inspect the asset listings to determine whether the assets are labelled and have a designated owner.
3. For a sample of services, inspect the asset reports to determine asset are labelled and have a designated owner.
4. Observe and compare physical assets at an organization's data center to determine whether the assets were labelled according to in-scope asset listings.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-AM-02 | Asset Management | Asset Inventory |
| E-AM-01 | Asset Management | Asset Management Policy |


### AM-06 - Media Marking

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Where applicable, Organization marks information system media indicating the distribution limitations, handling caveats, and applicable security markings (if any) of the information. Exemptions must be approved by management and remain in a specific controlled area.

#### Implementation Requirements
1. Ensure that a process is established and documented for media marking and handling, including distribution limitation.
2. Ensure that sensitive information containing media is marked as per the organization's media marking requirements as applicable.
3. Ensure that any exceptions are approved by management, documented and retained by authorized personnel.

#### Testing Procedures
1. Inspect information system media marking to indicate the distribution limitations, handling caveats, and applicable security markings (if any) of the information.
2. Inspect exemption cases to validate that it must be approved by management and remain in a specific area.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-AM-01 | Asset Management | Asset Management Policy |
| E-AM-05 | Asset Management | Evidence of Media Snapshots |


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


### AM-08 - Asset Transportation Documentation

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Organization documents the transportation of physical media outside of datacenters. Physical media is packaged securely and transported in a secure, traceable manner.

#### Implementation Requirements
1. Ensure appropriate records and approvals are obtained and documented against entry and exit of each asset.
2. Ensure all assets being transported are secured as per the organization's policy and can be tracked when offsite.

#### Testing Procedures
1. Inspect the policy and/or standard to determine whether the transportation of physical media outside of datacenters are defined.
2. Inspect the logs of physical media evidence that have been transported to determine that physical media is packed securely and transported in a secure, traceable manner.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-AM-01 | Asset Management | Asset Management Policy |
| E-AM-06 | Asset Management | Asset Movement Records |


### AM-09 - Use of Portable Media

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
The use of portable media in Organization datacenters is prohibited unless explicitly authorized by management.

#### Implementation Requirements
1. Ensure policy and procedures are established and communicated prohibiting the use of portable media.
2. Ensure necessary controls are in place to detect the usage of portable media inside the organization's network.
3. Ensure any exceptions are documented based on business justification and need and are approved appropriately.

#### Testing Procedures
1. Inspect the policy and/or standard to determine that the use of portable media in the datacenters is prohibited unless explicitly authorized by management.
2. Inspect Configurations to detect the use of portable media.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-AM-01 | Asset Management | Asset Management Policy |
| E-AM-07 | Asset Management | Portable Media Configuration Evidence |


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


### AM-12 - Component Installation: Inspection and Approval

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Prior to installation in a production network, hardware components are inspected for improper or unauthorized modifications.

#### Implementation Requirements
1. Ensure a process is established and documented for approval of hardware prior to installation on production.
2. Ensure each asset is inspected with agreed on procedures before being enabled on production.

#### Testing Procedures
1. Validate if a process exists for the approval and verification of hardware prior to production installation.
2. Inspect hardware components installation records in a production network to determine that modifications were validated before installation.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-AM-01 | Asset Management | Asset Management Policy |
| E-AM-10 | Asset Management | Hardware Installation Records |


## Framework References
| **Control ID** | **Framework** | **Reference** |
|:-----------|:----------|:-----------|
| AM-01 | FedRAMP Moderate | CM-08, CM-08 (01) |
| AM-02 | FedRAMP Moderate | CM-08, CM-08 (01) |
| AM-04 | FedRAMP Moderate | CM-08 (03) |
| AM-05 | FedRAMP Moderate | CM-08 |
| AM-06 | FedRAMP Moderate | MP-03 |
| AM-07 | FedRAMP Moderate | MA-02, PE-08, SA-09 (05) |
| AM-08 | FedRAMP Moderate | MA-02, MP-05 |
| AM-09 | FedRAMP Moderate | MP-05, MP-07 |
| AM-10 | FedRAMP Moderate | CM-08, MA-02, MA-03, MA-04, MP-01 |
| AM-12 | FedRAMP Moderate | MA-03 (02) |

## Framework Reference Mapping
| **Framework** | **Reference** | **Controls** |
|:----------|:----------|:---------|
| FedRAMP Moderate | CM-08 | AM-01, AM-02, AM-05, AM-10 |
| FedRAMP Moderate | CM-08 (01) | AM-01, AM-02 |
| FedRAMP Moderate | CM-08 (03) | AM-04 |
| FedRAMP Moderate | MA-02 | AM-07, AM-08, AM-10 |
| FedRAMP Moderate | MA-03 | AM-10 |
| FedRAMP Moderate | MA-03 (02) | AM-12 |
| FedRAMP Moderate | MA-04 | AM-10 |
| FedRAMP Moderate | MP-01 | AM-10 |
| FedRAMP Moderate | MP-03 | AM-06 |
| FedRAMP Moderate | MP-05 | AM-08, AM-09 |
| FedRAMP Moderate | MP-07 | AM-09 |
| FedRAMP Moderate | PE-08 | AM-07 |
| FedRAMP Moderate | SA-09 (05) | AM-07 |

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
