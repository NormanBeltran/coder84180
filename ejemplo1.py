from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

texto_largo = """
La inteligencia artificial (IA) es un campo de la informática que se enfoca en crear sistemas
capaces de realizar tareas que normalmente requieren inteligencia humana. Esto incluye
procesos como el aprendizaje, el razonamiento, la percepción y la comprensión del lenguaje.
En los últimos años, el desarrollo de modelos de lenguaje como GPT ha acelerado el uso de IA
en áreas como atención al cliente, generación de contenido y análisis de datos.
"""

respuesta = client.responses.create(
    model="gpt-4o-mini",
    input=f"Hace un resumen en 30 palabras del siguiente texto: {texto_largo}",
)

print(respuesta.output_text)
