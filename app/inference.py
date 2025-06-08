# ---- app/inference.py ----
from PIL import Image
import requests
import torch

def extract_ingredients(image_path, processor, model):
    image = Image.open(image_path).convert('RGB')
    inputs = processor(image, return_tensors='pt')
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption

def generate_recipe_from_caption(caption):
    prompt = f"""
    You are a professional chef. Create a creative and tasty recipe using the ingredients mentioned in this caption: "{caption}".

    Provide the following:
    - Mouth-watering Recipe Name
    - Ingredients Required
    - Step-by-Step Instructions
    - Estimated Cook Time
    - Serving Suggestion
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Error: Could not connect to Mistral API. Please ensure Ollama is running."