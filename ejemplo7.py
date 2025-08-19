from openai import OpenAI
import os
import requests
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.images.generate(
    model = "dall-e-3",
    prompt = "Un paisaje de montaña al atardecer con un lago reflejando el cielo como si lo hubiese pintado Van Gogh",
    n = 1,
    size = "1024x1024"
)

image_url = response.data[0].url
print(f"Imagen generada: {image_url}")

# Instalar requests: pip install requests
img_data = requests.get(image_url).content
with open('paisaje-vg.png', 'wb') as handler:
    handler.write(img_data)

print("Fin: Imagen generada")    
