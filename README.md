# VíaSegura

Sistema de gestión de permisos de circulación para transporte de carga, con evaluación de riesgo espacio-temporal.

Ver el plan de proyecto completo en [`docs/ViaSegura-Plan-Proyecto.md`](docs/ViaSegura-Plan-Proyecto.md).

## Estructura del repositorio

```
ViaSegura/
├── app-movil/       # Módulo 1a — App móvil (React Native) — Agustin Cavieres
├── dashboard/       # Módulo 1b — Dashboard web (React.js + MapLibre GL) — Agustin Cavieres
├── backend/         # Módulo 2 — API core (Node.js + Express + PostGIS) — Joshua Cruz
├── servicio-riesgo/ # Módulo 3 — Microservicio de riesgo (Python + FastAPI) — Nicolas Saavedra
└── docs/            # Plan de proyecto y documentación
```

## Integrantes

| Integrante | Módulo | Carpeta |
|---|---|---|
| Agustin Cavieres | Frontend Multicapa | `app-movil/`, `dashboard/` |
| Joshua Cruz | Backend Core | `backend/` |
| Nicolas Saavedra | Microservicio de Inteligencia Geoespacial | `servicio-riesgo/` |

## Flujo de trabajo (Git)

Ver sección 7 del plan de proyecto. Resumen:

- Ramas: `feature/moduloX-nombre-semanaY`, fixes: `fix/moduloX-descripcion-corta`.
- Commits pequeños y frecuentes (`feat:`, `fix:`, `chore:`, `test:`).
- `git pull --rebase origin develop` antes de abrir PR. PR requiere revisión de al menos un compañero. Merge final a `main` solo desde `develop`, validado por los tres.

## Setup rápido por módulo

```bash
# Backend
cd backend && npm install && npm run dev

# Dashboard web
cd dashboard && npm install && npm run dev

# App móvil
cd app-movil && npm install && npm start

# Microservicio de riesgo
cd servicio-riesgo && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && uvicorn app.main:app --reload
```
