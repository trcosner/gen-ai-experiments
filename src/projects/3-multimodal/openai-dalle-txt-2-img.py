#!/usr/bin/env python3
import sys
import requests
import os
from datetime import datetime

from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper

# Add src root to path (we're in /src inside the container)
sys.path.append('/src')     
from config import set_environment
        
# Set environment variables (no more print statement to suppress)
set_environment()

# Create output directory if it doesn't exist
output_dir = "/src/generated_output"
os.makedirs(output_dir, exist_ok=True)

dalle = DallEAPIWrapper(
    model="dall-e-3",
    size="1024x1024",
    quality="standard",
    n=1
)

prompt = "A futuristic city skyline at sunset"
image_url = dalle.run(prompt)

# Generate filename with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"dalle_{timestamp}_futuristic_city.png"
filepath = os.path.join(output_dir, filename)

# Download and save image
response = requests.get(image_url)
with open(filepath, "wb") as f:
    f.write(response.content)

print(f"Image saved to: {filepath}")
print(f"Prompt used: {prompt}")