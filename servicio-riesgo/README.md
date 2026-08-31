# servicio-riesgo — Microservicio de Inteligencia Geoespacial (Módulo 3)

Responsable: Nicolas Saavedra

## Alcance (ver plan completo en `../docs/ViaSegura-Plan-Proyecto.md`)
Python + FastAPI: score de riesgo espacio-temporal, clustering DBSCAN/K-Means para zonas rojas normalizadas por densidad poblacional (dataset simulado + datos censales del INE).

## Setup

```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
cp .env.example .env           # completar rutas de datasets
uvicorn app.main:app --reload
```

Verificar que el servicio responde en `http://localhost:8000/health`.

## Semana 1 — Tareas
- Carga y limpieza del dataset simulado de incidentes delictivos.
- Carga de datos censales del INE por manzana censal.
- Endpoint `/health`.

Rama de trabajo: `nicolas-riesgo`.
