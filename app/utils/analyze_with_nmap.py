import subprocess
import re
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)


async def analyze_with_nmap(url: str, speed: int):
    """
    Ejecuta Nmap para analizar puertos abiertos y versiones de servicios.
    Genera logs en tiempo real durante el escaneo.
    """
    try:
        domain = re.sub(r"https?://", "", url).rstrip("/")
        command = ["nmap", "-sV", f"-T{speed}", domain]

        logger.info(f"Iniciando escaneo Nmap en {
                    domain} con velocidad T{speed}.")

        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, universal_newlines=True
        )

        output = []
        for line in iter(process.stdout.readline, ""):
            line = line.strip()
            if line:
                logger.info(line)
                output.append(line)

        process.wait()

        if process.returncode != 0:
            error_message = process.stderr.read()
            logger.error(f"Error ejecutando Nmap: {error_message.strip()}")
            raise RuntimeError(f"Error ejecutando Nmap: {
                               error_message.strip()}")

        logger.info("Escaneo Nmap completado.")
        return parse_nmap_output("\n".join(output))

    except Exception as e:
        logger.error(f"Error durante el escaneo: {str(e)}")
        return {"error": str(e)}


def parse_nmap_output(output: str):
    """
    Parsea la salida de Nmap para extraer información de servicios.
    """
    services = []
    lines = output.splitlines()
    capture = False

    for line in lines:
        if line.startswith("PORT"):
            capture = True
            continue
        if capture and line.strip() == "":
            break
        if capture:
            # Parsea cada línea que describe un puerto abierto
            match = re.match(r"(\d+/tcp)\s+(\w+)\s+(.+)", line)
            if match:
                port, state, details = match.groups()
                services.append({
                    "port": port,
                    "state": state,
                    "details": details
                })

    return services
