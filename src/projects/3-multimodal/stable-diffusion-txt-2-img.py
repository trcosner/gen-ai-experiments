#!/usr/bin/env python3
import sys
import requests
import os
from datetime import datetime

from langchain_community.llms import Replicate

# Add src root to path (we're in /src inside the container)
sys.path.append('/src')     
from config import set_environment
        
# Set environment variables (no more print statement to suppress)
set_environment()

# Create output directory if it doesn't exist
output_dir = "/src/generated_output"
os.makedirs(output_dir, exist_ok=True)

text2img = Replicate(
    model="stability-ai/stable-diffusion-3.5-large",
    model_kwargs={
        "prompt_strength": 0.8,      # How closely to follow the prompt (0.1-1.0, higher = more adherence)
        "cfg": 4.0,                  # Classifier-Free Guidance scale (1-20, higher = more prompt adherence)
        "steps": 30,                 # Number of denoising steps (10-50, more steps = higher quality but slower)
        "aspect_ratio": "16:9",      # Output image aspect ratio (e.g., "1:1", "4:3", "16:9", "9:16")
        "output_format": "png",      # Image format ("png", "jpg", "webp")
        "output_quality": 80,        # Image quality for lossy formats (0-100, higher = better quality)
    }
)

prompt = "A futuristic city skyline at sunset"
image_url = text2img.invoke(prompt)

# Generate filename with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"stable_diffusion_{timestamp}_futuristic_city.png"
filepath = os.path.join(output_dir, filename)

# Download and save image
response = requests.get(image_url)
with open(filepath, "wb") as f:
    f.write(response.content)

print(f"Image saved to: {filepath}")
print(f"Prompt used: {prompt}")