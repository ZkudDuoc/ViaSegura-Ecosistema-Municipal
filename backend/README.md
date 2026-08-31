# Backend Core — Módulo 2

Responsable: Joshua Cruz

## Alcance (ver plan completo en `../docs/ViaSegura-Plan-Proyecto.md`)
API RESTful, ciclo de vida del permiso, RBAC/JWT, WebSocket (Socket.io) para el botón de pánico, PostgreSQL/PostGIS, integración HTTP con `servicio-riesgo`.

## Setup

```bash
npm install
cp .env.example .env   # completar DATABASE_URL, JWT_SECRET, RISK_SERVICE_URL
npm run dev
```

Verificar que el servidor responde en `http://localhost:3000/health`.

## Semana 1 — Tareas
- Conectar PostgreSQL/PostGIS (Supabase).
- Migraciones del esquema completo (COMUNA, EMPRESA, USUARIO, PERMISO, etc.).
- RBAC/JWT base.

Rama de trabajo: `feature/modulo2-backend-semana1` (ya creada desde `develop`).
