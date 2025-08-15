#!/usr/bin/env python3
import sys
import os

# Add src root to path (we're in /src inside the container)
sys.path.append('/src')

from config import set_environment
        
# Set environment variables (no more print statement to suppress)
set_environment()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful coding assistant with the skill of a senior software engineer."),
    ("human", "{input}")
])

llm = ChatAnthropic(
    model="claude-sonnet-4-20250514", 
    max_tokens=6000,
    thinking={"type": "enabled", "budget_tokens": 2000},
)

# llm = ChatOpenAI(
#     model="o3-mini",
#     reasoning_effort="high",
# )
outputParser = StrOutputParser()
chain = prompt | llm | outputParser

input = """
Design and implement a function that finds the shortest path between any two nodes in a weighted directed graph, but with the constraint that the path cannot use more than K edges, and must avoid nodes that are in a given "forbidden" set. The function should handle negative edge weights (but no negative cycles) and return both the shortest distance and the actual path.

Requirements:
- Handle graphs with up to 1000 nodes
- Support negative weights (detect negative cycles)
- Avoid forbidden nodes
- Limit path to K edges maximum
- Return both distance and path
- Optimize for time complexity

Provide the complete implementation with test cases.
"""

response = chain.invoke({"input": input})

print(response.content)