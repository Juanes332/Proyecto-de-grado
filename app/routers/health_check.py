from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def root():
    return {"message": "Bienvenido a la API de análisis ampliado con BuiltWith, Nmap Nikto y Whatweb"}
