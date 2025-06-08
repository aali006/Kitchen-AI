# Kitchen-AI
Recipe from Snap
# KitchenCam-AI-From-Fridge-to-Fork-with-AI
What’s in Your Fridge? Let AI Cook It

This project uses Generative AI to turn a photo of your fridge into a delicious recipe.

It combines:

📸 Image captioning (BLIP) to detect ingredients from a photo

🧠 Mistral-7B-Instruct (via Ollama) to generate creative and detailed recipes

🎛️ Gradio UI for a smooth user experience


 **Features**---
Upload an image of your fridge or ingredients

Detects ingredients using BLIP (image captioning)

Generates a full recipe (name, steps, cook time, etc.) using Mistral LLM

Gradio-based user interface

Runs entirely locally (no need for OpenAI API)

##################🔧 **Installation & Setup**##########################
1. Clone the Repository
2. Install Dependencies
   gradio
   transformers
   torch
   Pillow
   requests
3. Install and Run Ollama
4. ollama pull mistral
   ollama run mistral
5. Run the App
6. Upload your fridge image and get a recipe!

**Example**:-- 🧾 Detected Ingredients: milk, eggs, spinach, and mushrooms

🍽️ Generated Recipe:
- Recipe Name: Creamy Spinach and Mushroom Frittata
- Cook Time: 20 minutes
- Serves: 2
...

**Notes**--
Ollama must be running in the background to generate recipes.

If requests fails to connect, make sure:

Ollama is installed

ollama run mistral is active in another terminal

Port 11434 is not blocked

![Fridge_pic_output](https://github.com/user-attachments/assets/a0a104a1-e0f9-4bc4-a539-7a1f08d27f91)





