# Canonical model. Compliance and Q&A agents

Questions and compliance 


## Questions the AI can answer

Which services does the customer consume?

### Business impact
Which workloads would be affected if PostgreSQL BCN fails?

```
Database Platform
↓
Database Service
↓
Workload
```

### Environment analysis
Which services are deployed in Production?
```
Environment
↓
Service Instance
```

### Application dependency
Which workloads depend on the Database Service?
```
Service Instance
↓
Workload
```

### Environment inventory
Show the Production Environment.
```
Applications:
 - ERP
 - E-Commerce

Workloads:
 - ERP Workload
 - E-Commerce Workload

Services:
 - VM Service
 - Web Service
 - Database Service
```

### Application dependency
Which workloads depend on the Database Service?
```
Service Instance
↓
Workload
```


## Recommended MVP hierarchy

Ontology structure:
```
Customer
    ↓
Customer Application
    ↓
Workload
    ↓
Environment
    ↓
Service Instance
    ↓
Infrastructure Resource
    ↓
Capacity Pool
```

Minimum ontology that allows the agent to understand:
```
Business
↓
Application
↓
Workload
↓
Service
↓
Infrastructure
```

## Ontology Governance Agent

### Architecture

```
Canonical Model
        │
        ├── Domains
        ├── Entities
        ├── Attributes
        └── Relationships
                │
                ▼

        Ontology Review Agent

                │

 ┌──────────────┼──────────────┐
 │              │              │

Quality      Consistency     Governance

                │

                ▼

         Findings Repository
```

### Agent Objectives

- Is the ontology complete?
- Are all entities correctly related?
- Are there redundant concepts?
- Are there missing relationships?
- Are there entities without owners?
- Are there concepts that violate modeling standards?


### Review Type 1: Structural Validation


The model defines:
```
Customer
Contract
Subscription
Service Instance

```

Rule1 :
Every Subscription must be linked to a Contract.

Agent query:
Find subscriptions without contract.

Result:
ERROR. SUB-00991. No Contract relationship found.


Rule 2: 
Every Service Instance must be operated by a Team.

Detection: 
3 Service Instances without OPERATED_BY relationship.


### Review Type 2: Domain Validation

The agent validates that entities belong to the correct domain.

Example

```
Database Instance 
    appears inside:
        Commercial Domain

    instead of:
        Infrastructure Domain

```

The agent reports:
WARNING. Possible domain mismatch.




### Review Type 3: Cardinality Validation

Example

```
Rule:
Customer
    HAS_ACCOUNT
        CustomerAccount
            1:N

```

Agent checks: 
Customer A has 6 CustomerAccounts. 
Allowed? Yes.

But:

```
    VM
        RUNS_ON
            HypervisorHost

```

Expected: 1:1

```
Detection:
    VM-001
        RUNS_ON Host A
        RUNS_ON Host B
 
```

The agent reports:
Potential inconsistency.

### Review Type 4: Relationship Validation

One of the most useful capabilities.

Example

```
You define:
DELIVERED_BY
    Customer
DELIVERED_BY
    VM

```

The agent says: 
    Invalid relationship. 
    Customer should consume services.
    Service Instance should be delivered by VM.



### Review Type 5: Naming Validation

Very useful when the model grows.

Example

```
Customer
Client
CustomerAccount

```

The agent may identify: Customer and Client appear to represent the same concept.
Potential duplicate


### Review Type 6: Taxonomy Validation

Example

```
Gold
gold
GOLD

```

Agent: Standardize to: Gold


### Review Type 7: Authority Validation

The agent checks: Every attribute must have an authority.

Example

```
VirtualMachine
    hostname
    cpu
    memory
    criticality

```

Detection: Criticality. No authoritative source assigned.


### Review Type 8: OKF Validation

The agent reads the OKF corpus.

Example

```YAML
type: ServiceInstance
```

but the ontology contains

```YAML
type: InfrastructureServiceInstance
```

Agent reports: Type not found in ontology.


Another example:

CONSUMES → XXX.md

File missing.

Agent reports: Broken OKF reference.


### Review Type 9: Knowledge Graph Validation

The graph allows additional reviews.

Example

```
Customer
↓
Service
↓
Infrastructure

```

Agent detects:
orphan nodes

Example

```
Database Platform
0 incoming relationships
0 outgoing relationships
```

Finding:
Possible obsolete node.


### Review Type 10: Business Validation

This becomes extremely valuable.

Example rule
```
Every customer must consume at least one service.
```

Example
```
Customer
No Contract
No Subscription
No Service

```

Result:
Business inconsistency.


### Example Findings Report

```TEXT
# Ontology Review

Date: 2026-09-15

## Critical

### Finding 001

Entity:
SVC-WEB-002

Issue:
Missing OPERATED_BY relationship

Recommendation:
Assign operational team

---

### Finding 002

Entity:
SUB-0045

Issue:
No Contract relationship

Recommendation:
Link to Contract

```


## LLM + Rules Architecture

Use:
Rules Engine + LLM

### Rules Engine
Deterministic.

Example
Every VM must belong to a Cluster.

### LLM
Semantic review.

Example:
Customer
Client
Account

The LLM may detect: Possible concept overlap.



## Proposed Agents

I would build 4 specialized agents.

### Agent 1. Ontology Governance Agent

Checks:
```
Domains
Entities
Relationships
Attributes
```

### Agent 2. Knowledge Graph Quality Agent

Checks:
```
Orphans
Broken paths
Graph inconsistencies
```

### Agent 3. OKF Quality Agent

Checks:
```
Markdown structure
Metadata
Broken links
```

### Agent 4. Semantic Modeling Agent

Uses AI to suggest:
```
Missing entities
Duplicate concepts
Better relationships
```

### Example Prompt

```
Review the canonical ontology.

Validate:
- Naming consistency
- Domain assignment
- Relationship consistency
- Cardinality
- Missing ownership
- Missing authoritative sources
- Potential duplicate concepts
 
Generate findings grouped by:
Critical
Warning
Recommendation

Do not invent facts.
Only use the information provided.

```


## Recommendation

For this current stage, build a very simple Ontology Governance Agent MVP with three inputs:

1. Canonical Model Excel
2. OKF Repository
3. Relationship Catalog


and make it generate:

Ontology Review Report
- Missing entities
- Missing relationships
- Missing SSOT
- Broken OKF links
- Orphan concepts
- Duplicate concepts

This agent will become the "quality gate" that every change to the Digital Brain must pass before being published to the Knowledge Graph and OKF repository.