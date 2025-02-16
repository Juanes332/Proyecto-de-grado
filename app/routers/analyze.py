from fastapi import APIRouter
from services.analyze import Analyze
from utils.url_input import URLInput

router = APIRouter()


@router.post("/analyze")
async def analyze_endpoint(input: URLInput):
    """
    Endpoint que recibe una URL y devuelve el análisis de tecnologías y Nmap.
    """
    return await Analyze.analyze_website(input)
