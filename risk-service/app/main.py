from fastapi import FastAPI

app = FastAPI(title="VíaSegura — Microservicio de Inteligencia Geoespacial")


@app.get("/health")
def health():
    return {"status": "ok", "module": "risk-service"}
