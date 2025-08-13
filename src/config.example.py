"""
Configuration file for API keys and environment variables.
This file should NOT be committed to version control.
Copy this file to config.py, then fill in your actual API keys.
"""
import os

def set_environment():
    """
    Set environment variables for various AI service API keys.
    Fill in your actual API keys below.
    """
    
    # OpenAI API Key (most commonly used throughout the book)
    os.environ['OPENAI_API_KEY'] = 'your-openai-api-key-here'
    
    # Anthropic Claude API Key
    os.environ['ANTHROPIC_API_KEY'] = 'your-anthropic-api-key-here'
    
    # Google AI/Gemini API Key
    os.environ['GOOGLE_API_KEY'] = 'your-google-ai-api-key-here'
    
    # Langsmith (for tracing and monitoring)
    os.environ['LANGCHAIN_TRACING_V2'] = 'true'
    os.environ['LANGCHAIN_API_KEY'] = 'your-langsmith-api-key-here'
    os.environ['LANGCHAIN_PROJECT'] = 'langchain-experiments'
    
    # Vector Database API Keys (uncomment and fill as needed)
    # os.environ['PINECONE_API_KEY'] = 'your-pinecone-api-key-here'
    # os.environ['WEAVIATE_URL'] = 'your-weaviate-url-here'
    # os.environ['WEAVIATE_API_KEY'] = 'your-weaviate-api-key-here'
    
    # Azure OpenAI (if using Azure instead of OpenAI directly)
    # os.environ['AZURE_OPENAI_API_KEY'] = 'your-azure-openai-key-here'
    # os.environ['AZURE_OPENAI_ENDPOINT'] = 'your-azure-openai-endpoint-here'
    # os.environ['AZURE_OPENAI_API_VERSION'] = '2024-02-01'
    
    # Other service API keys (uncomment as needed)
    # os.environ['HUGGINGFACE_API_TOKEN'] = 'your-huggingface-token-here'
    # os.environ['COHERE_API_KEY'] = 'your-cohere-api-key-here'
    # os.environ['SERPAPI_API_KEY'] = 'your-serpapi-key-here'  # For web search
    
    print("✅ Environment variables set successfully!")

if __name__ == "__main__":
    set_environment()
