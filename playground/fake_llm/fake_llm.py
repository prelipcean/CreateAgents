from langchain_community.llms.fake import FakeListLLM

# Create a fake LLM that always returns "Hello"
fake_llm = FakeListLLM(responses=["Hello"])

# Invoke the fake LLM with any input
result = fake_llm.invoke("Any input will return Hello")

print(result)  # Output: Hello
