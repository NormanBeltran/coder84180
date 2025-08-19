from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

#________________________________________________
# OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conversation = [
    {"role": "system", "content": "Eres un cocinero italiano muy famoso"},
    {"role": "user", "content": "Dame una receta tipica de Sicilia en no mas de 200 palabras."},
]

respuesta = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=conversation,
    max_tokens=400,
    temperature=0.9,
)

message = respuesta.choices[0].message

print(message.role)
print(message.content)