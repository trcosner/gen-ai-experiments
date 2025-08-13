#!/usr/bin/env python3
import sys
import os

# Add src root to path (we're in /src inside the container)
sys.path.append('/src')

from langchain_community.llms import FakeListLLM
     
from config import set_environment
        
# Set environment variables (no more print statement to suppress)
set_environment()

# Initialize OpenAi model
fake_model = FakeListLLM(responses=["This is a fake response from the FakeListLLM."])

# Initialize Google Generative AI model

msg = "Say hi fake llm."
print(msg)
response = fake_model.invoke(msg)
print(response)