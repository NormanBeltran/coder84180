from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

#________________________________________________
# OpenAI API key

frase = input("Introduce una frase para completar: ")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conversation = [
    {"role": "system", "content": "Eres un escritor que sabe completar frases"},
    {"role": "user", "content": f"Completa la siguiente frase de manera resumida: {frase}"},
]

respuesta = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=conversation,
    max_tokens=400,
    temperature=0,
)

message = respuesta.choices[0].message

print(message.role)
print(message.content)