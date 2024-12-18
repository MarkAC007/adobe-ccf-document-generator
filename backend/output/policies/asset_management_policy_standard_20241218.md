# Asset Management Policy

## Document Control
- **Version:** 1.0
- **Last Updated:** 2024-12-18
- **Classification:** Internal

## Purpose
This policy defines requirements for asset management policy.

## Scope
This policy applies to all systems and data.

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
