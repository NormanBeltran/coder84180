from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

texto_largo = """
La teoría cuántica, también conocida como mecánica cuántica, es un área de la física cuyos principales objetos de estudio son los elementos que se encuentran a nivel microscópico. Átomos, electrones y moléculas son ejemplos de estructuras que habitan el mundo subatómico.
“Se trata del estudio de la naturaleza, los materiales, todo lo que conforma nuestro Universo en la escala más pequeña que podemos identificar, que es la escala atómica molecular”, explica el físico Marcelo Knobel, profesor del Departamento de Física de la Materia Condensada y del Instituto de Física Gleb Wataghin, de la Universidad Estadual de Campinas (Unicamp).
Según el profesor, la teoría cuántica también puede considerarse la base de toda la física y tiene profundas implicaciones en muchas áreas, desde la tecnología, con las computadoras cuánticas hasta la cosmología, que estudia la formación del Universo.
"""

respuesta = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content": f"Resumir el siguiente texto en 30 palabras: {texto_largo}"}
    ],
)

print(respuesta.choices[0].message.content)