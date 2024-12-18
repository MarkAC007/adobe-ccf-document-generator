# Infrastructure Management Policy

## Document Control
- **Version:** 1.0
- **Last Updated:** 2024-12-18
- **Classification:** Internal

## Purpose
This policy defines requirements for infrastructure management policy.

## Scope
This policy applies to all systems and data.

## Policy Requirements

### BC-06 - Capacity Forecasting

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Budgets for infrastructure capacity are established based on analysis of historical business activity and growth projections; purchases are made against the established budget and plans are updated on a quarterly basis.

#### Implementation Requirements
1. Ensure that capacity forecasts are created based on the business forecasts, growth projections and analysis of historic business activity.
2. Ensure that budget allocation is done for infrastructure and resources basis Capacity forecasts.

#### Testing Procedures
1. Inspect and validate whether capacity planning was done and forecasts were created.
2. Validate whether budgets were established and capacity forecasts were taken into the account for the same.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-BC-05 | Business Continuity | Capacity Planning Meeting Minutes |


### CFM-01 - Baseline Configuration Standard

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Organization ensures security hardening and baseline configuration standards have been established according to industry standards and are reviewed and updated periodically.

#### Implementation Requirements
1. Prepare and maintain Security hardening and Baseline configuration standards shall be established.
2. Configuration of systems (systems can include AWS, Azure, GCP, and more) shall be configured with the baseline configuration.
3. Configure required permissions for the configuration management server.
4. Configuration of Security Groups, NACLs, and virtual firewall appliances shall be in place.
5. Configuration of VPC Firewall Rules and virtual firewall appliances to allow traffic from the configuration management server to the other system servers.
6. All production systems shall be able to demonstrate consistent system configurations via version control number, last update date, settings, or other.
7. Process shall be established to ensure that latest version patch (hardened as per industry practices) is applied wherever possible.
8. Ensure that security hardening and configuration baselines are monitored are flagged wherever deviation is observed.
9. Establish a process ensuring regular rule set reviews are conducted by relevant teams for network devices.

#### Testing Procedures
1. Validate whether Security hardening and Baseline configuration standards are established.
2. Inspect baseline configuration of systems (systems can include AWS, Azure, GCP, and more) shall be configured with the baseline configuration.
3. Validate whether the required permissions are present for the configuration management server.
4. Inspect Security Groups, NACLs, and virtual firewall appliances configurations.
5. Validate whether VPC Firewall Rules and virtual firewall appliances are configured to allow traffic from the configuration management server to the other system servers.
6. Inspect production systems to determine whether they demonstrate consistent system configurations via version control #, last update date, settings, or other.
7. For a sample of in scope servers validate whether latest version patch (hardened as per industry practices) is applied wherever possible.
8. Validate that security hardening and configuration baselines are monitored are flagged wherever deviation is observed.
9. Validate that regular rule set reviews are conducted by relevant teams for network devices.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-CFM-01 | Configuration Management | Firewall standard |
| E-CFM-02 | Configuration Management | Configuration Management Standard |
| E-CFM-03 | Configuration Management | Periodic Rule review documentation |
| E-CFM-04 | Configuration Management | System generated Latest patch versioning documentation |
| E-CFM-05 | Configuration Management | Configuration deviation samples |


### CFM-02 - Default "Deny-all" Settings

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Technology |

#### Policy Description
Where applicable, the information system default access configurations are set to "deny-all."

#### Implementation Requirements
1. Prepare a list of in-scope network devices and production accounts and ensure that default deny-all rules are configured
2. Ensure that deny-all rule precedes all other applied rules in terms of priority.

#### Testing Procedures
1. For a list of in-scope network devices and production accounts, validate that default deny-all rules are configured
2. Validate that deny-all rule precedes all other applied rules in terms of priority.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-AM-02 | Asset Management | Asset Inventory |
| E-CFM-03 | Configuration Management | Periodic Rule review documentation |


### CFM-07 - Configuration Checks

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Detective | Technology |

#### Policy Description
Organization uses mechanisms to detect deviations from baseline configurations on production environments.

#### Implementation Requirements
1. Ensure that security hardening and configuration baselines are being monitored for in-scope servers.
2. Deviations shall be generated for in-scope servers for which remediations shall be tracked to closure.
3. Design a process for security hardening and configuration baselines checks being accurate and updated at least annually.

#### Testing Procedures
1. Validate that security hardening and configuration baselines are being monitored for in-scope servers.
2. Validate that deviations are being generated for in-scope servers and remediations are tracked to closure.
3. Validate that the security hardening and configuration baselines checks are accurate and updated at least annually.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-CFM-11 | Configuration Management | Security hardening and configuration baselines checks review documentation |
| E-CFM-05 | Configuration Management | Configuration deviation samples |


### CFM-11 - Default Device Passwords

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Technology |

#### Policy Description
Vendor-supplied default passwords are changed according to Organization standards prior to device installation on the Organization network or immediately after software or operating system installation.

#### Implementation Requirements
1. Ensure that the security hardening and configuration baseline checks include enforcing disablement of default accounts.
2. Ensure that the security hardening and configuration baseline deviations are being tracked to resolution

#### Testing Procedures
1. Inspect security hardening and configuration baseline checks to determine whether they are configured to enforce disabling of default accounts.
2. Validate that the security hardening and configuration baseline deviations are being tracked to resolution.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-CFM-02 | Configuration Management | Configuration Management Standard |
| E-CFM-05 | Configuration Management | Configuration deviation samples |


### CFM-14 - Software Installation

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Installation of software or programs in the production environment is approved by authorized personnel.

#### Implementation Requirements
1. Ensure Security hardening and Baseline configuration standards includes process established to determine whether the installation of software or programs in the production environment is approved by authorized personnel.
2. Prepare an authorized approval matrix for installation of software or programs in the production environment.

#### Testing Procedures
1. Inspect Security hardening and Baseline configuration standards to ensure that the installation of software or programs in the production environment is approved by authorized personnel is defined.
2. Inspect the authorized approval matrix for installation of software or programs in the production environment.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-CFM-02 | Configuration Management | Configuration Management Standard |
| E-CFM-20 | Configuration Management | Authorized approval matrix |


### VM-08 - Infrastructure Patch Management

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Organization installs security-relevant patches, including software or firmware updates; identified end-of-life software must have a documented decommission plan in place.

#### Implementation Requirements
1. Ensure that a process for patch management and end-of-life requirements is defined and documented.
2. Ensure that patch updates are implemented for all compute resources.
3. Ensure all end-of-life software are decommissioned with a documented plan.

#### Testing Procedures
1. Inspect and validate that a process for patch management and end-of-life requirements is defined and documented.
2. For a sample of servers/virtual machine validate that patch updates are implemented.
3. For a sample of end-of-life software validate that it was decommissioned with a documented plan.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-VM-09 | Vulnerability Management | Infrastructure Management Policy |
| E-VM-10 | Vulnerability Management | Patch Implementation Evidence |
| E-VM-11 | Vulnerability Management | End of Life software decomission plan |


## Framework References
| **Control ID** | **Framework** | **Reference** |
|:-----------|:----------|:-----------|
| BC-06 | HIPAA Security | 164.308(a)(7)(ii) |
| CFM-01 | HIPAA Security | 164.308(a)(5)(ii)(B) |
| CFM-02 | Cyber Essentials (UK) | Firewalls |
| CFM-07 | HIPAA Security | 164.308(a)(5)(ii)(B) |
| CFM-11 | Cyber Essentials (UK) | Firewalls, Secure Configuration |
| CFM-14 | Cyber Essentials (UK) | Malware protection |
| VM-08 | Cyber Essentials (UK) | Security Update Management |
| VM-08 | HIPAA Security | 164.312(c)(1) |

## Framework Reference Mapping
| **Framework** | **Reference** | **Controls** |
|:----------|:----------|:---------|
| Cyber Essentials (UK) | Firewalls | CFM-02, CFM-11 |
| Cyber Essentials (UK) | Malware protection | CFM-14 |
| Cyber Essentials (UK) | Secure Configuration | CFM-11 |
| Cyber Essentials (UK) | Security Update Management | VM-08 |
| HIPAA Security | 164.308(a)(5)(ii)(B) | CFM-01, CFM-07 |
| HIPAA Security | 164.308(a)(7)(ii) | BC-06 |
| HIPAA Security | 164.312(c)(1) | VM-08 |
