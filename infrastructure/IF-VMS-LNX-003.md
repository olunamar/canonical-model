---
type: CanonicalEntity
domain: Infrastructure
entity: VirtualMachine
entity_name: VM-LINUX-003
description: Virtualized server instance running within a hypervisor cluster.
id_unico: IF-VMS-LNX-003
status: Active
ssot_principal: CMDB
relations:
  - type: MEMBER_OF
    target: /infrastructure/IF-SVR-LNX-001.md
---

# VirtualMachine

Infrastructure-level virtual server entity.


## Descripción General

Servidor de aplicaciones **Apache Tomcat**.  

Permite a los distintos clientes y sus correspondientes **Líneas de Negocio (Business Units)** instanciar servidores web/Java listos para producción con una parametrización base centralizada, pero permitiendo personalizar aspectos clave según la carga de trabajo.

---

## Arquitectura y Dependencias

- **Servicio Base Requerido**: `catalog/infrastructure/hypervisor`
- **Gestión de Servicio**: Administrado vía `systemd` (`tomcat.service`)
- **Automatización**: Ansible Playbooks / **Terraform** / Deployment Manager

---

## Configuración Global Estándar (Default Baseline)

### 1. Parámetros
- **vCPUs**: `2`
- **Memory (GB)**: `4` 
- **Disk (GB)**: `50`
- **Operating System**: `Oracle Linux`
