#!/usr/bin/env python3
import sys
import os

# Add src root to path (we're in /src inside the container)
sys.path.append('/src')

from config import set_environment
        
# Set environment variables (no more print statement to suppress)
set_environment()

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


llm = GoogleGenerativeAI(
    model="gemini-2.5-pro", 
)

poem_prompt = PromptTemplate.from_template(
    ("Write a poem about {topic} in the style of Poe."),
)


outputParser = StrOutputParser()
poem_chain = poem_prompt | llm | outputParser

topic = "cosmic horror in the modern age"

analysis_prompt = PromptTemplate.from_template("Analyze the following poem's mood:\n\n{poem}")

analysis_chain = analysis_prompt | llm | outputParser

poem_with_analysis_chain = poem_chain | {
    "poem": RunnablePassthrough(),
    "analysis": analysis_chain
}

response = poem_with_analysis_chain.invoke({"topic": topic})

print(response)