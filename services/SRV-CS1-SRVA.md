---
type: CanonicalEntity
domain: Services
entity: ServiceInstance
entity_name: Service SILVER
description: Base instance of a service running in a specific environment.
id_unico: SRV-CS1-SRVA
status: Active
ssot_principal: CMDB
relations:
  - type: CONSUMED_BY
    target: /customers/CUST-000001.md
  - type: SUPPORTS
    target: /workloads/WL-CS1-EMP.md
---

# ServiceInstance

Base operational service instance model.

## Parameters
- Nivel de servicio
- Horario
- Ventana de actuación

## Equipos
