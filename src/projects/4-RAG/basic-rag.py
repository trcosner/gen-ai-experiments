import sys
import os

sys.path.append('/src')     
from config import set_environment
        
# Set environment variables (no more print statement to suppress)
set_environment()

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

#load the PDF document
loader = PyPDFLoader("/src/projects/4-RAG/resume.pdf")
documents = loader.load()

# Create a text splitter for better chunking
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        # Size of each chunk in characters
    chunk_overlap=200,      # Overlap between chunks to maintain context
    length_function=len,    # Function to measure chunk length
    separators=["\n\n", "\n", " ", ""]  # Split on paragraphs first, then sentences, then words
)

# Split documents into chunks
chunks = text_splitter.split_documents(documents)

# Create embeddings and vector store
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(chunks, embeddings)

# Create a prompt template
template = """
You are a helpful assistant that extracts information from a resume to answer questions.
Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.  
{context}
Question: {question}
Answer:
"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=template
)

llm = ChatOpenAI(
    model="o3-mini",
    reasoning_effort="high",
)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Define the question
question = "How could this person help me build an agentic ai platform?"

# Get relevant context from vector store (increased to 3 chunks for better coverage)
relevant_docs = vector_store.similarity_search(question, k=3)
context = "\n\n".join([doc.page_content for doc in relevant_docs])

# Get the answer
result = chain.invoke({
    "question": question,
    "context": context
})

print(f"Question: {question}")
print(f"Answer: {result}")