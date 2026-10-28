# 🚨 Disaster Recovery & Incident Post-Mortem: Rescate de Datos y Optimización de Producción

Documentación técnica y forense de la resolución de un incidente crítico en plataforma de e-commerce bajo alta concurrencia.

---

## 🛑 1. Resumen Ejecutivo del Incidente (The Incident)
* **Fecha del Incidente:** Simulación de Post-Mortem post-lanzamiento (Cyber Day).
* **Severidad:** Crítica (Caída total del servicio / HTTP 500 en cadena).
* **Impacto de Negocio:** Interrupción de transacciones durante 45 minutos y corrupción de registros relacionales debido a datos sucios heredados (legacy data).

---

## 🔍 2. Análisis Forense: ¿Qué falló?
Tras la auditoría de los registros de servidor y bases de datos, se detectaron dos fallas raíz:
1. **Datos Huérfanos y Sucios:** Registros de usuarios y carritos con nulos, duplicados y desalineación de esquemas que rompían la integridad referencial (Foreign Keys).
2. **Deadlocks en Base de Datos:** Consultas masivas y sin índices adecuados que bloquearon las tablas transaccionales principales durante el pico de tráfico.

---

## 🛠️ 3. Plan de Mitigación y Solución Aplicada
* **Fase 1 (Limpieza Masiva):** Ejecución de scripts de normalización para purgar duplicados, estandarizar formatos de texto y eliminar registros huérfanos.
* **Fase 2 (Reindexación y Optimización):** Creación de índices compuestos en tablas críticas (`orders`, `users`, `logs`) para reducir el tiempo de búsqueda de $O(N)$ a $O(\log N)$.
* **Fase 3 (Prevención):** Implementación de manejo de transacciones seguras (ACID) y validación estricta de esquemas antes de la inserción en base de datos.

---

## 📂 4. Estructura del Repositorio
* `scripts/data_cleanup_pipeline.py`: Pipeline en Python para la limpieza de datos corruptos.
* `sql/index_optimization.sql`: Script de reindexación y resolución de bloqueos en SQL.
