# Business Continuity Policy

## Document Control
- **Version:** 1.0
- **Last Updated:** 2024-12-18
- **Classification:** Internal

## Purpose
This policy defines requirements for business continuity policy.

## Scope
This policy applies to all systems and data.

## Policy Requirements

### BC-01 - Business Continuity Plan

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Preventive | Process |

#### Policy Description
Organization's business contingency plan is periodically reviewed, approved by management and communicated to relevant team members.

#### Implementation Requirements
1. Design and document a process for Business Continuity and Disaster Recovery.
2. Define steps for recovery with all roles and responsibilities in the Business Continuity Plan.
3. Ensure that the Business Continuity Plan is approved by the process owners, and is communicated to all the relevant team members.

#### Testing Procedures
1. Inspect and validate whether the Business Continuity and Disaster Recovery Processes are designed and documented.
2. Inspect Organization's Business Continuity Plan (BCP) to determine whether Organization has established recovery steps and phases, recovery capabilities, and identified personnel responsible to execute recovery procedures.
3. Inspect the most recent version of Organizations BCP to determine whether it is periodically reviewed and approved.
4. Inspect the corporate intranet to determine whether Organizations BCP is communicated to relevant team members.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-BC-01 | Business Continuity | Business Continuity Policy |
| E-BC-02 | Business Continuity | Business Continuity Plan |


### BC-02 - Business Continuity Plan: Personal Health Information

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Corrective | Process |

#### Policy Description
Organization's Business Contingency Plan addresses how to access facilities and obtain data during an emergency.

#### Implementation Requirements
1. Ensure that steps to be followed in case of an emergency are clearly mentioned in the Business Continuity Plan so that access to the facilities and data is facilitated during an emergency.

#### Testing Procedures
1. Inspect an organization's Business Contingency Plan to determine whether Organization has addresses how to access facilities and obtain data during an emergency.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-BC-02 | Business Continuity | Business Continuity Plan |


### BC-04 - Continuity Testing

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Detective | Process |

#### Policy Description
Organization performs business contingency and disaster recovery tests on a periodic basis and ensures the following:  tests are executed with relevant contingency teams  test results are documented  corrective actions are taken for exceptions noted  plans are updated based on results

#### Implementation Requirements
1. Ensure that Business Continuity testing should be performed on a periodic basis as per the organization policy.
2. The business continuity testing should emulate the Business Continuity Plan and should check the coverage and efficiency of the plan. All the relevant team preparedness should be assessed in this testing.
3. Ensure that the test results are documented, and any exceptions are noted and appropriate corrective action is undertaken.

#### Testing Procedures
1. Inspect whether Business Continuity Testing was performed on a periodic basis as per the organization's policy.
2. Inspect the most recent BCP test and inspect DR tests results to determine whether tests were executed and results were documented.
3. Validate whether the results of the testing exercises were tracked to remediation.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-BC-03 | Business Continuity | Business Continuity/Disaster Recovery Test Results |


### BC-05 - Business Impact Analysis

#### Control Information
| **Type** | **Theme** |
|:-----|:------|
| Corrective | Process |

#### Policy Description
Organization identifies the business impact of relevant threats to assets, infrastructure, and resources that support critical business functions. Recovery objectives are established for critical business functions.

#### Implementation Requirements
1. Design and document a process for conducting Business Impact Analysis to determine the criticality of business activities and associated resource requirements.
2. Ensure that BIA is conducted for all processes and assets to identify criticality.
3. Ensure that recovery objectives are established for critical processes.

#### Testing Procedures
1. Inspect and validate whether a documented process exists for conducting Business Impact Analysis.
2. Inspect Business Impact Analysis to determine whether the threats to assets, infrastructure, and resources are identified and the recovery objectives are established.

#### Audit Requirements
Evidence Required:

| **ID** | **Domain** | **Title** |
|:---|:-------|:------|
| E-BC-01 | Business Continuity | Business Continuity Policy |
| E-BC-02 | Business Continuity | Business Continuity Plan |


## Framework References
| **Control ID** | **Framework** | **Reference** |
|:-----------|:----------|:-----------|
| BC-01 | HIPAA Security | 164.308(a)(7)(i), 164.308(a)(7)(ii), 164.308(a)(7)(ii)(B) |
| BC-01 | SOC 2 | CC7.5 |
| BC-02 | HIPAA Security | 164.310(a)(2)(i), 164.312(a)(2)(ii) |
| BC-04 | HIPAA Security | 164.308(a)(7)(ii), 164.308(a)(7)(ii)(B), 164.308(a)(7)(ii)(D), 164.310(a)(2)(i) |
| BC-04 | SOC 2 | A1.3, CC7.5 |
| BC-05 | HIPAA Security | 164.308(a)(7)(ii)(E) |
| BC-05 | SOC 2 | CC7.5 |

## Framework Reference Mapping
| **Framework** | **Reference** | **Controls** |
|:----------|:----------|:---------|
| HIPAA Security | 164.308(a)(7)(i) | BC-01 |
| HIPAA Security | 164.308(a)(7)(ii) | BC-01, BC-04 |
| HIPAA Security | 164.308(a)(7)(ii)(B) | BC-01, BC-04 |
| HIPAA Security | 164.308(a)(7)(ii)(D) | BC-04 |
| HIPAA Security | 164.308(a)(7)(ii)(E) | BC-05 |
| HIPAA Security | 164.310(a)(2)(i) | BC-02, BC-04 |
| HIPAA Security | 164.312(a)(2)(ii) | BC-02 |
| SOC 2 | A1.3 | BC-04 |
| SOC 2 | CC7.5 | BC-01, BC-04, BC-05 |
