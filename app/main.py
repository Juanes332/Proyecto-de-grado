from fastapi import FastAPI
from routers import health_check, analyze

app = FastAPI()
app.include_router(analyze.router, prefix="/api", tags=["Analyze"])
app.include_router(health_check.router, prefix="/api", tags=["HealthCheck"])
