---
type: CanonicalEntity
domain: Infrastructure
entity: DatabaseInstance
entity_name: ORACLE-DB-BPM
description: Active running instance process of a database platform engine.
id_unico: IF-DBI-ORA-003
status: Active
ssot_principal: CMDB
relations:
  - type: USED_BY
    target: /workloads/WL-CS1-TM4.md
  - type: MEMBER_OF
    target: /infrastructure/IF-DBP-ORA-002.md
  - type: RUNS_ON
    target: /infrastructure/IF-VMS-LNX-003.md
---

# DatabaseInstance

Active runtime execution process for database instances.

---

## Arquitectura y Dependencias

- **Producto**: `ORACLE DATABASE ENTERPRISE EDITION`
- **Versión producto**: `19`
- **Gestión de Servicio**: Administrado vía `systemd` (`tomcat.service`)
- **Automatización**: **Ansible Playbooks** / Terraform / Deployment Manager

---

## Configuración Global Estándar (Default Baseline)

### Parámetros
- **Puerto**: `1522`


### Capacity
- **DB size**: `84`
- **evidence**: 22/09/2026
- **ssot**: `observability`
