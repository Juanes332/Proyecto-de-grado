# 🕵️ FastAPI Web Scanner con Nmap

Este proyecto es una API desarrollada en **FastAPI** que permite:

- 🔍 **Analizar tecnologías web** usando [`builtwith`](https://pypi.org/project/builtwith/)
- 🔎 **Escanear puertos abiertos y servicios** utilizando [`Nmap`](https://nmap.org/)
- 🐳 **Ejecutar en Docker con Nmap preinstalado**

---

## 🛠️ Requisitos previos

### 📌 **Ejecutar en entorno local**

Asegúrate de tener instalado lo siguiente:

- **Python 3.12+**
- **pip** (manejador de paquetes de Python)
- **Nmap** (`nmap --version` debe funcionar en la terminal)

### 📌 **Ejecutar con Docker**

Asegúrate de tener:

- **Docker instalado** → [Descargar aquí](https://www.docker.com/get-started)

### 📌 **Instalar Nmap (si no lo tienes)**

#### 🖥️ **Windows**

1. Descarga e instala desde [Nmap.org](https://nmap.org/download.html)
2. Agrega la carpeta `Nmap` al `PATH` (Ejemplo: `C:\Program Files (x86)\Nmap\`)

#### 🐧 **Linux (Debian/Ubuntu)**

```sh
sudo apt update && sudo apt install nmap -y
```

---

### 🚀 Instalación y uso

1️⃣Clonar el repositorio

```sh

git clone https://github.com/tu_usuario/tu_proyecto.git
cd tu_proyecto


```

2️⃣ Ejecutar en entorno local (sin Docker)
Instala las dependencias

```sh

pip install -r requirements.txt


```

### Ejecuta la API:

```sh

uvicorn main:app --host 0.0.0.0 --port 8000 --reload


```

Las documentaciones estan en en:

📜 Swagger UI: http://localhost:8000/docs
📘 Redoc: http://localhost:8000/redoc

---

### 🐳 Ejecutar con Docker

1️⃣ Construir la imagen

```sh

docker build -t fastapi-nmap-app .

```

2️⃣ Ejecutar el contenedor

```sh

docker run -p 8000:8000 fastapi-nmap-app


```

Ahora la API estará accesible en:

http://localhost:8000/docs

### ❤️‍🩹 Uso del endpoint /health

🔹 Método: GET
🔹 URL: /health
🔹 Descripción: health-check del API

### 📡 Uso del endpoint /analyze

🔹 Método: POST
🔹 URL: /analyze
🔹 Descripción: Analiza una URL, detecta tecnologías y realiza un escaneo con Nmap.

🔹 Ejemplo de Request

```json
{
  "url": "https://www.unad.edu.co/",
  "speed": "5"
}
```

🔹 Ejemplo de Respuesta

```json
{
  "url": "https://www.unad.edu.co/",
  "technologies": {
    "web-servers": ["Apache"],
    "font-scripts": ["Google Font API"],
    "web-frameworks": ["Twitter Bootstrap"],
    "cms": ["Joomla"],
    "programming-languages": ["PHP"]
  },
  "nmap_analysis": [
    {
      "port": "80/tcp",
      "state": "open",
      "details": "http      Apache httpd"
    },
    {
      "port": "443/tcp",
      "state": "open",
      "details": "ssl/http  Apache httpd"
    },
    {
      "port": "8010/tcp",
      "state": "open",
      "details": "ssl/xmpp?"
    }
  ]
}
```

---

⚡ Configuración de speed en Nmap

El parámetro "speed" (o -T) en Nmap controla la velocidad del escaneo, con valores entre 0 y 5:

| 🔢 Valor | 🚀 Descripción                                                                               |
| -------- | -------------------------------------------------------------------------------------------- |
| `0`      | 🐢 **Paranoid Mode** → Extremadamente lento (para evitar detección en IDS)                   |
| `1`      | 🐌 **Sneaky Mode** → Lento, pero con mayor cobertura                                         |
| `2`      | 🚶 **Polite Mode** → Reduce el impacto en la red (modo recomendado para entornos sensibles)  |
| `3`      | 🚲 **Normal Mode** → Balance entre rapidez y precisión (**Valor por defecto de Nmap**)       |
| `4`      | 🚗 **Aggressive Mode** → Escaneo rápido, pero más detectable                                 |
| `5`      | 🚀 **Insane Mode** → Extremadamente rápido (puede saturar la red o generar falsos positivos) |

📌 Recomendaciones:
Usa 4 (Aggressive) para escaneos rápidos en redes seguras.
Usa 2 (Polite) si no quieres afectar el rendimiento de la red.
No uses 5 (Insane) en redes públicas, ya que podría ser detectado como ataque.

---

📜 Notas Importantes
Nmap requiere permisos administrativos en algunos sistemas (especialmente en Linux y Windows con UAC activado).
El escaneo puede ser bloqueado por firewalls dependiendo de la configuración del servidor.
Si Nmap no funciona en Docker, asegúrate de que nmap esté instalado dentro del contenedor.

---

🙌 Contribuciones
¡Cualquier contribución es bienvenida!
Puedes hacer un fork, crear un pull request, o abrir un issue para reportar mejoras.

👩‍💻 Hecho con ❤️ por Juanhez
