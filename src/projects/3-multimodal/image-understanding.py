import base64
import sys
import os
import glob

sys.path.append('/src')     
from config import set_environment
        
# Set environment variables (no more print statement to suppress)
set_environment()

from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Find the most recent stable diffusion image
output_dir = "/src/generated_output"
stable_diff_images = glob.glob(os.path.join(output_dir, "stable_diffusion_*.png"))

if not stable_diff_images:
    print("No stable diffusion images found. Run the stable-diffusion-txt-2-img.py script first.")
    sys.exit(1)

# Get the most recent image (sorted by filename which includes timestamp)
latest_image = sorted(stable_diff_images)[-1]
print(f"Analyzing image: {latest_image}")

# Read and encode the image
with open(latest_image, "rb") as image_file:
    image_bytes = image_file.read()
    base64_bytes = base64.b64encode(image_bytes).decode('utf-8')

prompt = [
    {"type": "text", "text": "Describe the image"},
    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_bytes}"}}
]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    temperature=0
)

response = llm.invoke([HumanMessage(content=prompt)])
print("Response:", response.content)