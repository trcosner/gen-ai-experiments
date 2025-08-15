import sys

sys.path.append('/src')     
from config import set_environment
        
# Set environment variables (no more print statement to suppress)
set_environment()

from langchain_core.messages import AIMessage

class MessagesIterator:
    def __init__(self):
      self._count = 0

    def __iter__(self):
        return self
   
    def __next__(self):
        self._count += 1
        if self._count % 2 == 1:
            raise ValueError("Something went wrong!")
        return AIMessage(content="False")
        
from langchain_core.runnables import RunnableLambda
from langchain_core.language_models import GenericFakeChatModel

chain_fallback = RunnableLambda(lambda _: print("Running fallback."))


fake_llm = GenericFakeChatModel(messages=MessagesIterator())


chain = fake_llm | RunnableLambda(lambda _: print("Running main chain."))

chain_with_fallback = chain.with_fallbacks([chain_fallback])

chain_with_fallback.invoke("Hello, world!")
chain_with_fallback.invoke("Hello world!!")