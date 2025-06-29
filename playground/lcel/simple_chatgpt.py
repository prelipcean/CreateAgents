from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# Create components
prompt = PromptTemplate.from_template("Tell me a joke about {topic}")
llm = ChatOpenAI()
output_parser = StrOutputParser()

# Chain them together using LCEL
chain = prompt | llm | output_parser

# Use the chain
result = chain.invoke({"topic": "programming"})
print(result)
