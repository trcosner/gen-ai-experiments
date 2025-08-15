import base64
import sys
import os
import glob

sys.path.append('/src')     
from config import set_environment
        
# Set environment variables (no more print statement to suppress)
set_environment()

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

def analyze_image(image_url: str, question: str) -> str:
    chat = ChatOpenAI(
        model="gpt-4o-mini",
        max_tokens=256
    )

    message = HumanMessage(
        content = [
            {
                "type": "text",
                "text": question
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                    "detail": "auto"
                }
            }
        ]
    )

    response = chat.invoke([message])
    return response.content


questions = [
    "What is the main subject of the image?",
    "Describe the colors and mood of the image.",
    "What objects or elements are present in the image?",
    "Is there any text visible in the image? If so, what does it say?",
    "What emotions does the image convey?"
]

# Find the most recent stable diffusion image
output_dir = "/src/generated_output"
stable_diff_images = glob.glob(os.path.join(output_dir, "stable_diffusion_*.png"))

if not stable_diff_images:
    print("No stable diffusion images found. Run the stable-diffusion-txt-2-img.py script first.")
    sys.exit(1)

latest_image = sorted(stable_diff_images)[-1]

# Read and encode the image to create a data URL
with open(latest_image, "rb") as image_file:
    image_bytes = image_file.read()
    base64_bytes = base64.b64encode(image_bytes).decode('utf-8')

image_url = f"data:image/png;base64,{base64_bytes}"


for question in questions:
        print(f"\nQ: Question: {question}")
        print(f"\nA: {analyze_image(image_url, question)}")
