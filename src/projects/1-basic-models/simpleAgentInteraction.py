#!/usr/bin/env python3
import sys
import os

# Add src root to path (we're in /src inside the container)
sys.path.append('/src')

from config import set_environment
        
# Set environment variables (no more print statement to suppress)
set_environment()

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage

chat = ChatAnthropic(model="claude-sonnet-4-20250514")
messages = [SystemMessage(content="You are a principle software engineer in applied AI LLM technologies"),
            HumanMessage(content="What is LangChain?")]

response = chat.invoke(messages)
print(response)