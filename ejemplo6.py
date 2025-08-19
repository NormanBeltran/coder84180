from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

#________________________________________________
# OpenAI API key

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conversation = [
    {"role": "system", "content": "Eres un coach, personal trainer, que da consejos de manera concisa, no mas de 100 palabras"},
]

print("Coach: Hola! Soy tu personal trainer. ¿En qué puedo ayudarte hoy? (fin para terminar)")

while True:
    user_input = input("Tú: ")
    if user_input.lower() == "fin":
        print("Coach: ¡Hasta luego! Recuerda que estoy aquí para ayudarte.")
        break
    conversation.append({"role": "user", "content": user_input})

    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation,
        max_tokens=400,
        temperature=0,
    )

    message = respuesta.choices[0].message
    print(message.content)