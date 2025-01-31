# Asset Management Policy

## Document Control
- **Version:** 1.0
- **Last Updated:** 2025-01-31
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


### AM-03 - Inventory Reconciliation: ARP Table

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Organization reconciles network discovery scans against the established device inventory on a quarterly basis; non-inventoried devices are assigned an owner.

#### Implementation Requirements
1. Design and document a process for conducting network discovery scans on a periodic basis.
2. Ensure the results of the scans are reconciled with the system asset inventory at least quarterly.
3. Ensure necessary actions are taken to include non-inventoried assets in the inventory with appropriate ownership details.

#### Testing Procedures
1. Inspect network discovery scans result to ensure periodic scans were conducted.
2. Observe the reconciliation report of network discovery scans against the established device inventory to determine that the inventories are reconciled on a quarterly basis.
3. Inspect the device inventory to ensure non-inventoried devices have been added and have a designed owner.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-AM-04 | Asset Management | Network Discovery Scan Records |
| E-AM-03 | Asset Management | Asset Reconciliation Records |
| E-AM-02 | Asset Management | Asset Inventory |


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


### AM-11 - Tampering of Payment Card Capture Devices

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Detective | Process |

#### Policy Description
Devices that physically capture payment card data are inspected for evidence of tampering on a semi-annual basis.

#### Implementation Requirements
1. Ensure all payment card devices are inspected on semiannual basis to check for tampering.
2. Ensure that appropriate documentation is maintained regarding maintenance activities of these devices

#### Testing Procedures
1. Inspect devices verification records for tampering check.
2. Inspect and validate whether these verification were done at least semi-annually.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-AM-09 | Asset Management | Payment Card Device Verification Records |


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


### AM-13 - Software bill of Material

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Organization maintains a comprehensive software bill of materials

#### Implementation Requirements
1. Ensure a Software bill of material is established.
2. Ensure that a process has been established and documented for the addition, removal, and update of components from SBOM.

#### Testing Procedures
1. Inspect and validate that a Software bill of material is established.
2. Validate that a process has been established and documented for addition, removal, and update of components from SBOM.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-AM-01 | Asset Management | Asset Management Policy |
| E-AM-11 | Asset Management | Software Bill of Materials |


## Compliance Requirements

| Control ID | BSI C5 | CIS v8 | Cyber Essentials (UK) | ENS | FedRAMP Moderate | FedRAMP Tailored | HIPAA Security | IRAP | ISMAP | ISO 22301 | ISO 27001 | ISO 27002 | ISO 27017 | ISO 27018 | K-FSI | MAS | MLPS | NIST CSF | PCI DSS v4 | SOC 2 | TX-RAMP Level 1 |
|:-----------|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
| AM-01 | AM-01, AM-06 | 1.1, 6.6 | - | 10, 26, 8, 9 | CM-08, CM-08 (01) | CM-08 | 164.310(d)(1) | ISM-0336, ISM-1359, ISM-1493, ISM-1549, ISM-1551, ISM-1713 | 11.2.1.9, 18.1.2.4, 18.1.3.12, 8.1.1.1, 8.1.1.2, 8.1.1.3, 8.1.1.4, 8.1.1.5, 8.1.1.6.PB, 8.3.1.11, 8.3.1.3, 8.3.1.8 | - | - | - | - | - | 3.1.1 | 3.3 | 8.1.10.2, 8.1.4.2 | ID.AM-1, ID.AM-2 | 12.5.1, 12.5.2, 12.5.2.1, 9.5.1.1 | CC6.1 | CM-08 |
| AM-02 | AM-01, AM-06 | 1.1, 6.6 | - | 10, 26, 8, 9 | CM-08, CM-08 (01) | CM-08 | 164.310(d)(1) | ISM-0336, ISM-1359, ISM-1493, ISM-1549, ISM-1551, ISM-1713 | 11.2.1.9, 18.1.2.4, 18.1.3.12, 8.1.1.1, 8.1.1.2, 8.1.1.3, 8.1.1.4, 8.1.1.5, 8.1.1.6.PB, 8.3.1.11, 8.3.1.3, 8.3.1.8 | - | - | - | - | - | 3.1.1 | 3.3 | 8.1.10.2, 8.1.4.2 | ID.AM-1, ID.AM-2 | 12.5.1, 12.5.2, 12.5.2.1, 9.5.1.1 | CC6.1 | CM-08 |
| AM-03 | - | 1.2, 1.3, 1.5 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | 8.1.10.2 | - | 11.2, 11.2.1, 11.2.2, 11.3.1, 11.3.1.3, 11.4.5, 11.4.6 | - | - |
| AM-04 | - | 1.4 | - | - | CM-08 (03) | - | - | - | - | - | - | - | - | - | - | - | - | - | 12.5.1, 12.5.2, 12.5.2.1, 9.4.5, 9.4.5..1 | - | - |
| AM-05 | AM-01, AM-06 | 1.1 | - | 10, 26, 8, 80, 9, 92, 93 | CM-08 | CM-08 | - | ISM-0294, ISM-0325, ISM-0330, ISM-0332, ISM-0378, ISM-0831, ISM-1071, ISM-1187, ISM-1217, ISM-1525 | 8.1.2.1, 8.1.2.2, 8.1.2.3, 8.1.2.4, 8.1.2.5, 8.1.2.6 | - | - | 5.13 | - | - | 3.1.1 | 3.3 | 8.1.4.2 | - | 9.4.2 | CC6.1 | CM-08 |
| AM-06 | - | - | - | - | MP-03 | - | - | ISM-0270, ISM-0323, ISM-0325, ISM-0330, ISM-0337, ISM-0831, ISM-1574, ISM-1599 | 18.1.3.2, 18.1.3.4, 18.1.3.5, 18.1.3.7 | - | - | 5.1, 7.8 | - | - | - | - | 8.1.10.3 | - | 9.4 | - | - |
| AM-07 | - | - | - | 57, 68, 69, 84 | MA-02, PE-08, SA-09 (05) | MA-02, PE-08 | 164.310(d)(1), 164.310(d)(2)(iii) | ISM-1243, ISM-1779 | 11.2.5.1, 11.2.5.2, 11.2.5.3, 11.2.5.4, 11.2.6.2, 6.1.2.2, 8.3.1.2 | - | - | 7.1 | - | A.10.4 | - | - | - | ID.AM-4, PR.DS-3 | 9.4.4 | CC6.7 | MA-02, PE-08 |
| AM-08 | - | - | - | 57, 68, 69 | MA-02, MP-05 | MA-02 | - | ISM-0310 | 11.2.5.1, 11.2.6.3, 11.2.6.5, 8.3.3.1, 8.3.3.2, 8.3.3.3, 8.3.3.4, 8.3.3.5 | - | - | - | - | A.10.4 | - | - | 8.1.10.3, 8.1.10.4 | - | 9.4.3 | - | MA-02 |
| AM-09 | - | - | - | - | MP-05, MP-07 | MP-07 | - | - | - | - | - | - | - | - | - | - | - | - | 9.4.4 | - | MP-07 |
| AM-10 | PS-06 | - | - | 13, 29 | CM-08, MA-02, MA-03, MA-04, MP-01 | CM-08, MA-02, MA-04, MP-01, SA-22, SR-11 (02) | 164.310(a)(2)(iv) | ISM-0305, ISM-0306, ISM-0307, ISM-1598 | 11.2.1.10, 11.2.4.1, 11.2.4.10, 11.2.4.11, 11.2.4.2, 11.2.4.3, 11.2.4.4, 11.2.4.5, 11.2.4.6, 11.2.4.7, 11.2.4.8, 11.2.4.9, 6.1.1.5, 8.3.1.4, 8.3.1.5, 8.3.1.6, 8.3.1.9 | - | - | 7.13 | - | - | - | 7.3 | 8.1.10.4, 8.1.10.6 | PR.DS-8, PR.MA-1 | 9.4.4 | A1.2 | CM-08, MA-02, MA-04, MP-01 |
| AM-11 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | 9.5.1.2 | - | - |
| AM-12 | AM-03 | 4.2 | - | - | MA-03 (02) | SR-11, SR-11 (01) | - | ISM-0343, ISM-1418 | - | - | - | - | - | - | - | - | - | - | 2.2, 6.5.1 | - | - |
| AM-13 | - | - | - | - | - | - | - | ISM-1730 | - | - | - | - | - | - | - | - | - | - | - | - | - |

## Framework Reference Mapping
| **Framework** | **Reference** | **Controls** |
|:----------|:----------|:---------|
| BSI C5 | AM-01 | AM-01, AM-02, AM-05 |
| BSI C5 | AM-03 | AM-12 |
| BSI C5 | AM-06 | AM-01, AM-02, AM-05 |
| BSI C5 | PS-06 | AM-10 |
| CIS v8 | 1.1 | AM-01, AM-02, AM-05 |
| CIS v8 | 1.2 | AM-03 |
| CIS v8 | 1.3 | AM-03 |
| CIS v8 | 1.4 | AM-04 |
| CIS v8 | 1.5 | AM-03 |
| CIS v8 | 4.2 | AM-12 |
| CIS v8 | 6.6 | AM-01, AM-02 |
| ENS | 10 | AM-01, AM-02, AM-05 |
| ENS | 13 | AM-10 |
| ENS | 26 | AM-01, AM-02, AM-05 |
| ENS | 29 | AM-10 |
| ENS | 57 | AM-07, AM-08 |
| ENS | 68 | AM-07, AM-08 |
| ENS | 69 | AM-07, AM-08 |
| ENS | 8 | AM-01, AM-02, AM-05 |
| ENS | 80 | AM-05 |
| ENS | 84 | AM-07 |
| ENS | 9 | AM-01, AM-02, AM-05 |
| ENS | 92 | AM-05 |
| ENS | 93 | AM-05 |
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
| FedRAMP Tailored | CM-08 | AM-01, AM-02, AM-05, AM-10 |
| FedRAMP Tailored | MA-02 | AM-07, AM-08, AM-10 |
| FedRAMP Tailored | MA-04 | AM-10 |
| FedRAMP Tailored | MP-01 | AM-10 |
| FedRAMP Tailored | MP-07 | AM-09 |
| FedRAMP Tailored | PE-08 | AM-07 |
| FedRAMP Tailored | SA-22 | AM-10 |
| FedRAMP Tailored | SR-11 | AM-12 |
| FedRAMP Tailored | SR-11 (01) | AM-12 |
| FedRAMP Tailored | SR-11 (02) | AM-10 |
| HIPAA Security | 164.310(a)(2)(iv) | AM-10 |
| HIPAA Security | 164.310(d)(1) | AM-01, AM-02, AM-07 |
| HIPAA Security | 164.310(d)(2)(iii) | AM-07 |
| IRAP | ISM-0270 | AM-06 |
| IRAP | ISM-0294 | AM-05 |
| IRAP | ISM-0305 | AM-10 |
| IRAP | ISM-0306 | AM-10 |
| IRAP | ISM-0307 | AM-10 |
| IRAP | ISM-0310 | AM-08 |
| IRAP | ISM-0323 | AM-06 |
| IRAP | ISM-0325 | AM-05, AM-06 |
| IRAP | ISM-0330 | AM-05, AM-06 |
| IRAP | ISM-0332 | AM-05 |
| IRAP | ISM-0336 | AM-01, AM-02 |
| IRAP | ISM-0337 | AM-06 |
| IRAP | ISM-0343 | AM-12 |
| IRAP | ISM-0378 | AM-05 |
| IRAP | ISM-0831 | AM-05, AM-06 |
| IRAP | ISM-1071 | AM-05 |
| IRAP | ISM-1187 | AM-05 |
| IRAP | ISM-1217 | AM-05 |
| IRAP | ISM-1243 | AM-07 |
| IRAP | ISM-1359 | AM-01, AM-02 |
| IRAP | ISM-1418 | AM-12 |
| IRAP | ISM-1493 | AM-01, AM-02 |
| IRAP | ISM-1525 | AM-05 |
| IRAP | ISM-1549 | AM-01, AM-02 |
| IRAP | ISM-1551 | AM-01, AM-02 |
| IRAP | ISM-1574 | AM-06 |
| IRAP | ISM-1598 | AM-10 |
| IRAP | ISM-1599 | AM-06 |
| IRAP | ISM-1713 | AM-01, AM-02 |
| IRAP | ISM-1730 | AM-13 |
| IRAP | ISM-1779 | AM-07 |
| ISMAP | 11.2.1.10 | AM-10 |
| ISMAP | 11.2.1.9 | AM-01, AM-02 |
| ISMAP | 11.2.4.1 | AM-10 |
| ISMAP | 11.2.4.10 | AM-10 |
| ISMAP | 11.2.4.11 | AM-10 |
| ISMAP | 11.2.4.2 | AM-10 |
| ISMAP | 11.2.4.3 | AM-10 |
| ISMAP | 11.2.4.4 | AM-10 |
| ISMAP | 11.2.4.5 | AM-10 |
| ISMAP | 11.2.4.6 | AM-10 |
| ISMAP | 11.2.4.7 | AM-10 |
| ISMAP | 11.2.4.8 | AM-10 |
| ISMAP | 11.2.4.9 | AM-10 |
| ISMAP | 11.2.5.1 | AM-07, AM-08 |
| ISMAP | 11.2.5.2 | AM-07 |
| ISMAP | 11.2.5.3 | AM-07 |
| ISMAP | 11.2.5.4 | AM-07 |
| ISMAP | 11.2.6.2 | AM-07 |
| ISMAP | 11.2.6.3 | AM-08 |
| ISMAP | 11.2.6.5 | AM-08 |
| ISMAP | 18.1.2.4 | AM-01, AM-02 |
| ISMAP | 18.1.3.12 | AM-01, AM-02 |
| ISMAP | 18.1.3.2 | AM-06 |
| ISMAP | 18.1.3.4 | AM-06 |
| ISMAP | 18.1.3.5 | AM-06 |
| ISMAP | 18.1.3.7 | AM-06 |
| ISMAP | 6.1.1.5 | AM-10 |
| ISMAP | 6.1.2.2 | AM-07 |
| ISMAP | 8.1.1.1 | AM-01, AM-02 |
| ISMAP | 8.1.1.2 | AM-01, AM-02 |
| ISMAP | 8.1.1.3 | AM-01, AM-02 |
| ISMAP | 8.1.1.4 | AM-01, AM-02 |
| ISMAP | 8.1.1.5 | AM-01, AM-02 |
| ISMAP | 8.1.1.6.PB | AM-01, AM-02 |
| ISMAP | 8.1.2.1 | AM-05 |
| ISMAP | 8.1.2.2 | AM-05 |
| ISMAP | 8.1.2.3 | AM-05 |
| ISMAP | 8.1.2.4 | AM-05 |
| ISMAP | 8.1.2.5 | AM-05 |
| ISMAP | 8.1.2.6 | AM-05 |
| ISMAP | 8.3.1.11 | AM-01, AM-02 |
| ISMAP | 8.3.1.2 | AM-07 |
| ISMAP | 8.3.1.3 | AM-01, AM-02 |
| ISMAP | 8.3.1.4 | AM-10 |
| ISMAP | 8.3.1.5 | AM-10 |
| ISMAP | 8.3.1.6 | AM-10 |
| ISMAP | 8.3.1.8 | AM-01, AM-02 |
| ISMAP | 8.3.1.9 | AM-10 |
| ISMAP | 8.3.3.1 | AM-08 |
| ISMAP | 8.3.3.2 | AM-08 |
| ISMAP | 8.3.3.3 | AM-08 |
| ISMAP | 8.3.3.4 | AM-08 |
| ISMAP | 8.3.3.5 | AM-08 |
| ISO 27002 | 5.1 | AM-06 |
| ISO 27002 | 5.13 | AM-05 |
| ISO 27002 | 7.1 | AM-07 |
| ISO 27002 | 7.13 | AM-10 |
| ISO 27002 | 7.8 | AM-06 |
| ISO 27018 | A.10.4 | AM-07, AM-08 |
| K-FSI | 3.1.1 | AM-01, AM-02, AM-05 |
| MAS | 3.3 | AM-01, AM-02, AM-05 |
| MAS | 7.3 | AM-10 |
| MLPS | 8.1.10.2 | AM-01, AM-02, AM-03 |
| MLPS | 8.1.10.3 | AM-06, AM-08 |
| MLPS | 8.1.10.4 | AM-08, AM-10 |
| MLPS | 8.1.10.6 | AM-10 |
| MLPS | 8.1.4.2 | AM-01, AM-02, AM-05 |
| NIST CSF | ID.AM-1 | AM-01, AM-02 |
| NIST CSF | ID.AM-2 | AM-01, AM-02 |
| NIST CSF | ID.AM-4 | AM-07 |
| NIST CSF | PR.DS-3 | AM-07 |
| NIST CSF | PR.DS-8 | AM-10 |
| NIST CSF | PR.MA-1 | AM-10 |
| PCI DSS v4 | 11.2 | AM-03 |
| PCI DSS v4 | 11.2.1 | AM-03 |
| PCI DSS v4 | 11.2.2 | AM-03 |
| PCI DSS v4 | 11.3.1 | AM-03 |
| PCI DSS v4 | 11.3.1.3 | AM-03 |
| PCI DSS v4 | 11.4.5 | AM-03 |
| PCI DSS v4 | 11.4.6 | AM-03 |
| PCI DSS v4 | 12.5.1 | AM-01, AM-02, AM-04 |
| PCI DSS v4 | 12.5.2 | AM-01, AM-02, AM-04 |
| PCI DSS v4 | 12.5.2.1 | AM-01, AM-02, AM-04 |
| PCI DSS v4 | 2.2 | AM-12 |
| PCI DSS v4 | 6.5.1 | AM-12 |
| PCI DSS v4 | 9.4 | AM-06 |
| PCI DSS v4 | 9.4.2 | AM-05 |
| PCI DSS v4 | 9.4.3 | AM-08 |
| PCI DSS v4 | 9.4.4 | AM-07, AM-09, AM-10 |
| PCI DSS v4 | 9.4.5 | AM-04 |
| PCI DSS v4 | 9.4.5..1 | AM-04 |
| PCI DSS v4 | 9.5.1.1 | AM-01, AM-02 |
| PCI DSS v4 | 9.5.1.2 | AM-11 |
| SOC 2 | A1.2 | AM-10 |
| SOC 2 | CC6.1 | AM-01, AM-02, AM-05 |
| SOC 2 | CC6.7 | AM-07 |
| TX-RAMP Level 1 | CM-08 | AM-01, AM-02, AM-05, AM-10 |
| TX-RAMP Level 1 | MA-02 | AM-07, AM-08, AM-10 |
| TX-RAMP Level 1 | MA-04 | AM-10 |
| TX-RAMP Level 1 | MP-01 | AM-10 |
| TX-RAMP Level 1 | MP-07 | AM-09 |
| TX-RAMP Level 1 | PE-08 | AM-07 |
