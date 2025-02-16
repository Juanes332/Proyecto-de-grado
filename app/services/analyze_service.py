from utils.url_input import URLInput
from utils.analyze_with_nmap import analyze_with_nmap
from fastapi import HTTPException
import builtwith


class Analyze:
    @staticmethod
    async def analyze_website(input: URLInput):
        """
        Toma la URL de un sitio web y analiza las tecnologías utilizadas,
        incluyendo servicios detectados con Nmap.
        """
        url: str = str(input.url)
        speed: int = input.speed

        try:
            technologies = builtwith.parse(url)

            nmap_result = await analyze_with_nmap(url, speed)

            return {
                "url": url,
                "technologies": technologies,
                "nmap_analysis": nmap_result,
            }
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error al analizar {url}: {str(e)}"
            )
