#!/usr/bin/env python3
import sys
import os

# Add src root to path (we're in /src inside the container)
sys.path.append('/src')

from langchain_openai import OpenAI
from langchain_google_genai import GoogleGenerativeAI
     
from config import set_environment
        
# Set environment variables (no more print statement to suppress)
set_environment()

# Initialize OpenAi model
openai_model = OpenAI()

# Initialize Google Generative AI model (using flash for higher free tier limits)
google_model = GoogleGenerativeAI(model="gemini-2.0-pro")

msg = "Tell me a science fact about quantum physics."
print(msg)
response = google_model.invoke(msg)
print(response)