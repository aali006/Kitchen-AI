# ---- app/interface.py ----
import gradio as gr
from app.model_loader import load_blip_model
from app.inference import extract_ingredients, generate_recipe_from_caption

def fridge_to_recipe(image):
    processor, model = load_blip_model()
    caption = extract_ingredients(image, processor, model)
    recipe = generate_recipe_from_caption(caption)
    return f"**Detected Ingredients:** {caption}\n\n**Generated Recipe:**\n{recipe}"

def create_interface():
    iface = gr.Interface(
        fn=fridge_to_recipe,
        inputs=gr.Image(type="filepath", label="Upload Image of Your Fridge"),
        outputs="text",
        title="Recipe Generator from Fridge Snapshot",
        description="Upload an image of the inside of your fridge. The model will detect ingredients and generate a creative recipe using Mistral-7B-Instruct via Ollama."
    )
    return iface