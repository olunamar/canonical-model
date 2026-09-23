---
type: CanonicalEntity
domain: Environments
entity: Environment
entity_name: Production
description: Deployment stage environment (e.g., Production, Staging, Development).
id_unico: EV-CS1-PRO
status: Active
ssot_principal: CMDB
relations:
  - type: CONTAINS
    target: /workloads/WL-CS1-TM4.md
  - type: CONTAINS
    target: /workloads/WL-CS1-XXI.md
  - type: CONTAINS
    target: /workloads/WL-CS1-EMP.md
  - type: USES
    target: /services/SRV-CS1-SRVA.md
---

# Environment
Logical segregation of runtime stages.
