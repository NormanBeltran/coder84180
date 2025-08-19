import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    provider="auto",
    api_key=os.getenv("HF_TOKEN"),
)

# output is a PIL.Image object
image = client.text_to_image(
    "Astronaut riding a horse",
    model="Qwen/Qwen-Image",
)

# Guardar con nombre fijo
image.save("astronaut_horse.png")