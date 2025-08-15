from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(
    model="deepseek-r1:1.5b", 
    temperature=0,
    base_url="http://ollama:11434"
)


prompt = PromptTemplate.from_template("Explain {concept} to a fifth grader.")

chain = prompt | llm | StrOutputParser()

result = chain.invoke({"concept": "nuclear fusion"})
print(result)