---
type: CanonicalEntity
domain: Infrastructure
entity: ApplicationServer
entity_name: TOMCAT-LINUX-002
description: Compute instance configured with web runtime engines (Tomcat).
id_unico: IF-APS-TMC-002
status: Active
ssot_principal: CMDB
relations:
  - type: HOSTS
    target: /workloads/WL-CS1-TM4.md
  - type: RUNS_ON
    target: /infrastructure/IF-VMS-LNX-002.md
---

# WebInstance
Web server runtime instance.

## Descripción General
Servidor de aplicaciones **Apache Tomcat**.  

Permite a los distintos clientes y sus correspondientes **Líneas de Negocio (Business Units)** instanciar servidores web/Java listos para producción con una parametrización base centralizada, pero permitiendo personalizar aspectos clave según la carga de trabajo.

---

## Arquitectura y Dependencias

- **Servicio Base Requerido**: `catalog/infrastructure/oracle-linux-vm`
- **Runtime Java por Defecto**: Eclipse Temurin OpenJDK 17 LTS
- **Versión de Apache Tomcat**: Tomcat 10.1.x
- **Gestión de Servicio**: Administrado vía `systemd` (`tomcat.service`)
- **Automatización**: **Ansible Playbooks** / Terraform / Deployment Manager

---

## Configuración Global Estándar (Default Baseline)

### 1. Parámetros de Red y Puertos
- **Puerto HTTP**: `8080`
- **Puerto HTTPS / TLS**: `8443` (Deshabilitado por defecto hasta adjuntar certificado)
- **Puerto Shutdown**: `8005` (Escuchando únicamente en `127.0.0.1`)

### 2. Memoria y Máquina Virtual Java (JVM)
- **Memory Heap Inicial (`-Xms`)**: `2048m` (2 GB)
- **Memory Heap Máximo (`-Xmx`)**: `4096m` (4 GB)
- **Garbage Collector**: G1GC (`-XX:+UseG1GC`)
- **Parámetros JVM por defecto**: `-Djava.awt.headless=true -XX:+HeapDumpOnOutOfMemoryError`

### 3. Seguridad y Hardening Base
- **Usuario de ejecución**: Usuario no privilegiado `tomcat:tomcat`
- **Visibilidad de Servidor**: Server Header oculta versión (`server="Apache Tomcat"`)
- **Gestor Web / Host Manager**: Deshabilitado por política de seguridad

### 4. Logs y Monitorización
- **Gestión de Logs**: Rotación diaria mediante `logrotate` y exportación centralizada a Google Cloud Logging
- **Métricas**: Agente de Google Cloud Ops Agent habilitado para métricas JMX/JVM

