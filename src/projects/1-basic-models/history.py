import sys

sys.path.append('/src')     
from config import set_environment
        
# Set environment variables (no more print statement to suppress)
set_environment()

from langchain_core.prompts import ChatPromptTemplate

prompt_template = "What can you tell me about {topic}?"

chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("placeholder", "{history}"),
    ("human", prompt_template)
])

print(len(
    chat_prompt_template.invoke(
        {
            "history": [
                {"role": "human", "content": "Hi"},
                { "role" : "ai", "content": "Hello!"}
            ], 
            "topic": "ancient roman history"
        }
    ).messages
))