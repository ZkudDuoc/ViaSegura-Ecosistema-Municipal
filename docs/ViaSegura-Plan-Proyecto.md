# VíaSegura — Plan de Proyecto: WBS y Cronograma de Ejecución (4 semanas, Waterfall paralelo)

## 1. Introducción y Objetivo del Proyecto

VíaSegura es un sistema de gestión de permisos de circulación para transporte de carga, con evaluación de riesgo espacio-temporal para restringir o autorizar rutas según zonas de peligrosidad. El proyecto se ejecuta en 4 semanas bajo un modelo Waterfall paralelo: cada uno de los 3 subsistemas avanza por las mismas fases (Setup → Core + Integración → Feature Freeze → E2E y Despliegue) en simultáneo, sincronizándose en dos hitos transversales — la integración funcional de Semana 2 y el release final de Semana 4 — en vez de que un módulo espere a que el anterior termine por completo.

Este documento es el plan de proyecto para efectos de evaluación del curso: define la arquitectura de módulos, el WBS, el cronograma semanal por integrante, los criterios de éxito verificables por hito, los riesgos identificados con su mitigación, y el protocolo de trabajo en GitHub que sostiene la ejecución paralela sin bloquear a ningún integrante.

## 2. Arquitectura de Módulos

La división en 3 módulos independientes-pero-integrables se mapea directamente a los 3 subsistemas ya definidos en el diseño — no es una división artificial, es la misma frontera de responsabilidad que sostiene toda la arquitectura:

| Módulo | Nombre técnico | Alcance |
|--------|-----------------|---------|
| Módulo 1 | Frontend Multicapa | App móvil (React Native): registro de solicitud con polígono GeoJSON, geofencing + foto, botón de pánico, escaneo QR e infracciones (Inspector). Dashboard web (React.js + MapLibre GL): bandeja de decisiones (Operador Central) y reportería de solo lectura (Supervisor). |
| Módulo 2 | Backend Core | Node.js + Express: API RESTful, ciclo de vida completo del permiso, RBAC/JWT, WebSocket (Socket.io) para el botón de pánico, PostgreSQL/PostGIS con la restricción de exclusión geoespacial, integración HTTP con el microservicio de riesgo. |
| Módulo 3 | Microservicio de Inteligencia Geoespacial | Python + FastAPI: score de riesgo espacio-temporal, clustering DBSCAN/K-Means para zonas rojas normalizadas por densidad poblacional (dataset simulado + datos censales del INE). |

**Asignación:** Agustin Cavieres → Módulo 1 (Frontend) · Joshua Cruz → Módulo 2 (Backend Core) · Nicolas Saavedra → Módulo 3 (Microservicio de Riesgo).

## 3. Work Breakdown Structure

```
VíaSegura
├── M1 Frontend (Agustin Cavieres)
│   ├── S1 Setup + esqueleto de pantallas
│   ├── S2 Registro de solicitud + geofencing/foto + pánico (conectado a M2)
│   ├── S3 Bandeja operador, vista supervisor, QR/infracciones — feature freeze
│   └── S4 E2E, build de producción, demo
├── M2 Backend Core (Joshua Cruz)
│   ├── S1 Setup + esquema completo PostGIS + RBAC base
│   ├── S2 Ciclo de vida del permiso + WebSocket + integración con M3
│   ├── S3 Reglas de negocio restantes (colas, revocación, bitácora) — feature freeze
│   └── S4 E2E, despliegue, tag de release
└── M3 Microservicio de Riesgo (Nicolas Saavedra)
    ├── S1 Setup FastAPI + carga de datasets (incidentes + INE)
    ├── S2 Score de riesgo + clustering expuestos vía API (conectado a M2)
    ├── S3 Calibración de parámetros + pruebas de escenarios — feature freeze
    └── S4 E2E, despliegue, soporte a la demo integrada
```

## 4. Cronograma y Matriz de Asignación Semanal

| Integrante / Módulo | Semana 1 — Setup | Semana 2 — Core + Integración | Semana 3 — Feature Freeze | Semana 4 — E2E y Despliegue |
|---|---|---|---|---|
| **Agustin Cavieres — Módulo 1 (Frontend)** | Setup React Native + React.js; estructura de navegación por rol (Chofer/Logística, Inspector, Operador, Supervisor); integración inicial de MapLibre GL con tiles OSM; mockups de solicitud y dashboard.<br>**Entregable:** commit en `agustin-frontend` con esqueleto de ambas apps. | Formulario de solicitud (polígono, tipo de actividad, altura estimada); pantalla de geofencing + foto; botón de pánico conectado por WebSocket; consumo real de la API del Backend.<br>**Entregable:** PR de `agustin-frontend` → develop; demo de solicitud creada extremo a extremo. | Bandeja del Operador, vista de reportería del Supervisor, escáner QR e infracciones del Inspector; congelamiento de features; pruebas de UI.<br>**Entregable:** push de Release Candidate del módulo Frontend. | Pruebas E2E del ciclo completo desde la app; build de producción de app y dashboard; corrección de bugs críticos.<br>**Entregable:** merge a main, participa del tag final. |
| **Joshua Cruz — Módulo 2 (Backend Core)** | Setup Node.js/Express; conexión a PostgreSQL/PostGIS en Supabase; migraciones del esquema completo (COMUNA, EMPRESA, USUARIO, PERMISO, etc.); RBAC/JWT base.<br>**Entregable:** commit en `joshua-backend` con migraciones y esqueleto de API. | Endpoints del ciclo de vida del permiso (evaluación, riesgo bajo/medio/alto); servidor WebSocket para pánico; integración HTTP con el microservicio de riesgo (Axios); constraint de exclusión geoespacial.<br>**Entregable:** PR de `joshua-backend` → develop; demo de integración Node↔Python funcionando — este es el hito del Modelo Funcional/MVP. | Reglas de negocio restantes: cola de espera con prioridad y reprogramación automática, revocación, cascada de resiliencia del pánico (WebSocket→SMS→cola local), bitácora append-only; pruebas unitarias e integración.<br>**Entregable:** push de Release Candidate del módulo Backend. | Pruebas E2E de la API completa; despliegue del backend (Render u equivalente); resolución de bugs de integración.<br>**Entregable:** merge a main, ejecuta el tag de release. |
| **Nicolas Saavedra — Módulo 3 (Microservicio de Riesgo)** | Setup FastAPI; carga y limpieza del dataset simulado de incidentes delictivos y de los datos censales del INE por manzana censal; endpoint `/health`.<br>**Entregable:** commit en `nicolas-riesgo` con esqueleto del servicio y datasets cargados. | Endpoint de score de riesgo (recibe polígono/fecha/tipo, devuelve score de riesgo y congestión); clustering DBSCAN normalizado por densidad poblacional para zonas rojas.<br>**Entregable:** PR de `nicolas-riesgo` → develop; demo del score respondiendo en tiempo real al Backend. | Calibración de parámetros del clustering; pruebas con distintos escenarios de riesgo (bajo/medio/alto); congelamiento de features.<br>**Entregable:** push de Release Candidate del microservicio. | Pruebas E2E del pipeline de riesgo dentro del flujo completo; despliegue del microservicio; soporte a la demo integrada.<br>**Entregable:** merge a main, participa del tag final. |

**Hito transversal de Semana 2:** con los tres PRs mergeados a develop, el equipo debe poder ejecutar el flujo real: solicitud desde la app → evaluación de riesgo consultando al microservicio → respuesta con score y estado desde el Backend — ese es el Modelo Funcional exigido por el plan.

**Hito transversal de Semana 4:** merge final develop → main, tag de versión (ej. v1.0.0), aplicación desplegada y estable para la presentación.

## 5. Criterios de Éxito y Entregables por Hito

| Hito | Criterio de éxito verificable |
|------|--------------------------------|
| Fin de Semana 1 | Los tres módulos tienen su esqueleto corriendo localmente (app, dashboard, API, microservicio) y cada uno hizo su commit de setup en su rama personal (`agustin-frontend`, `joshua-backend`, `nicolas-riesgo`). |
| Hito transversal de Semana 2 (Modelo Funcional/MVP) | Una solicitud creada desde la app llega al Backend, este consulta al Microservicio de Riesgo y recibe un score real (no mockeado), y el estado de la solicitud se refleja correctamente — demostrable en vivo, sin intervención manual en la base de datos. |
| Fin de Semana 3 (Feature Freeze) | Cada módulo publica su Release Candidate; no se agregan features nuevas después de este punto, solo corrección de bugs vía ramas `fix/nombre-descripcion-corta`. |
| Hito transversal de Semana 4 (Release final) | Merge `develop → main` validado por los tres integrantes, aplicación desplegada (app buildeada, dashboard, backend y microservicio accesibles), y demo end-to-end ejecutable sin errores críticos frente al evaluador. |

## 6. Riesgos y Plan de Contingencia

| # | Riesgo | Mitigación / Contingencia |
|---|--------|----------------------------|
| 1 | Atraso individual de un integrante en su módulo | Cualquiera de los otros dos compañeros puede cubrir las tareas críticas del módulo atrasado, dado que la matriz de asignación semanal deja claro qué se debe entregar cada semana. |
| 2 | Fallo o retraso en la integración transversal de Semana 2 (Frontend ↔ Backend ↔ Microservicio) | Se contempla un margen de hasta unos días antes de que el retraso afecte el inicio de Semana 3. Si el hito no se logra en ese margen, se prioriza dejar funcionando el flujo mínimo entre los tres módulos antes de sumar features nuevas. |
| 3 | Caída o indisponibilidad de servicios externos (Supabase/Render) durante la demo en vivo | Se graba con antelación un video de respaldo que muestra el sistema funcionando de extremo a extremo, para usar en caso de que la demo en vivo falle por causas externas. |
| 4 | Conflictos de merge no resueltos a tiempo para los PRs de Semana 2 y 4 | Se espera que el protocolo de `git pull --rebase` y PRs pequeños y frecuentes (ver sección 7) mantenga los conflictos resueltos antes de cada deadline semanal. |
| 5 | Dataset de incidentes delictivos o datos censales del INE no disponibles o incompletos a tiempo para el Módulo 3 | Se utiliza un dataset simulado como respaldo, permitiendo que el Microservicio de Riesgo funcione de forma independiente a la disponibilidad de datos reales. |

## 7. Protocolo de GitHub (3 pasos)

**Paso 1 — Nomenclatura de ramas.** Cada integrante trabaja sobre una rama personal fija durante todo el proyecto, con el patrón `nombre-abreviomodulo` (ej. `agustin-frontend`, `joshua-backend`, `nicolas-riesgo`), en vez de crear una rama nueva cada semana. En la Semana 3, los fixes de bugs usan `fix/nombre-descripcion-corta` en vez de seguir commiteando directo en la rama personal, para dejar claro en el historial qué se corrigió y por qué.

**Paso 2 — Commits frecuentes y descriptivos.** Se usa la convención tipo: descripción (`feat:`, `fix:`, `chore:`, `test:`), con commits pequeños y frecuentes durante la semana — no un solo commit gigante el día del entregable. Esto es lo que evita los conflictos masivos en los merges de Semana 2 y 4: un PR con 15 commits pequeños es fácil de revisar y de resolver si hay conflicto; uno con un solo commit de 2.000 líneas no.

**Paso 3 — Pull Request y merge disciplinado.** Antes de abrir el PR hacia develop, cada estudiante hace `git pull --rebase origin develop` en su propia rama para traer los cambios de los otros dos módulos y resolver conflictos localmente, donde es más fácil entenderlos. El PR requiere revisión de al menos un compañero antes de aprobar — nunca auto-merge. En la Semana 4, el único merge permitido hacia main es `develop → main`, ya validado por los tres, cerrado con el tag de release final.

## 8. Roles y Responsabilidades

| Integrante | Módulo | Responsabilidad técnica principal |
|------------|--------|-------------------------------------|
| Agustin Cavieres | Módulo 1 — Frontend Multicapa | App móvil (React Native) y dashboard web (React.js + MapLibre GL); UI/UX de los 4 roles del sistema (Chofer/Logística, Inspector, Operador Central, Supervisor). |
| Joshua Cruz | Módulo 2 — Backend Core | API RESTful en Node.js + Express, ciclo de vida del permiso, RBAC/JWT, WebSocket del botón de pánico, esquema PostgreSQL/PostGIS, e integración con el microservicio de riesgo. |
| Nicolas Saavedra | Módulo 3 — Microservicio de Inteligencia Geoespacial | Servicio Python + FastAPI para score de riesgo espacio-temporal y clustering de zonas rojas, incluyendo carga y normalización de los datasets de incidentes e INE. |

Cada integrante es responsable de su Release Candidate en Semana 3 y de participar en la revisión de PRs de los otros dos módulos antes de cada merge a `develop`.

## 6. Riesgos y Plan de Contingencia

| # | Riesgo | Mitigación / Contingencia |
|---|--------|----------------------------|
| 1 | Atraso individual de un integrante en su módulo | Cualquiera de los otros dos compañeros puede cubrir las tareas críticas del módulo atrasado, dado que la matriz de asignación semanal deja claro qué se debe entregar cada semana. |
| 2 | Fallo o retraso en la integración transversal de Semana 2 (Frontend ↔ Backend ↔ Microservicio) | Se contempla un margen de hasta unos días antes de que el retraso afecte el inicio de Semana 3. Si el hito no se logra en ese margen, se prioriza dejar funcionando el flujo mínimo entre los tres módulos antes de sumar features nuevas. |
| 3 | Caída o indisponibilidad de servicios externos (Supabase/Render) durante la demo en vivo | Se graba con antelación un video de respaldo que muestra el sistema funcionando de extremo a extremo, para usar en caso de que la demo en vivo falle por causas externas. |
| 4 | Conflictos de merge no resueltos a tiempo para los PRs de Semana 2 y 4 | Se espera que el protocolo de `git pull --rebase` y PRs pequeños y frecuentes (ver sección 7) mantenga los conflictos resueltos antes de cada deadline semanal. |
| 5 | Dataset de incidentes delictivos o datos censales del INE no disponibles o incompletos a tiempo para el Módulo 3 | Se utiliza un dataset simulado como respaldo, permitiendo que el Microservicio de Riesgo funcione de forma independiente a la disponibilidad de datos reales. |

## 7. Protocolo de GitHub
[Por escribir]

## 8. Roles y Responsabilidades
[Por escribir]
