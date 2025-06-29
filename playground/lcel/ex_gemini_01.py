"""
This script demonstrates a LangChain Expression Language (LCEL) chain
that generates a short story and then analyzes its mood.

It uses two sequential LLM calls:
1. Generates a story based on a given topic.
2. Analyzes the mood of the generated story.
Finally, it combines and prints both the story and its analyzed mood.
"""

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# --- Configuration and API Key Loading ---

# Load environment variables from a .env file.
# Ensures your GOOGLE_API_KEY is securely loaded for API authentication.
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    print("Error: GOOGLE_API_KEY not set in environment variables or .env file.")
    exit()  # Exit the script if the API key is not available

# --- Initialize the LLM (Large Language Model) ---

# Initialize the ChatGoogleGenerativeAI model.
# Using "gemini-1.5-flash-latest" for a fast and capable LLM.
chat = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

# First chain generates a story
story_prompt = PromptTemplate.from_template("Write a short story about {topic}")
story_chain = story_prompt | chat | StrOutputParser()

# Second chain analyzes the story
analysis_prompt = PromptTemplate.from_template(
    "Analyze the following story's mood:\n{story}"
)
analysis_chain = analysis_prompt | chat | StrOutputParser()

output_prompt = PromptTemplate.from_template(
    "Here's the story: \n{story}\n\nHere's the mood: \n{mood}"
)
# Combine chains
story_with_analysis = story_chain | analysis_chain

# Run the combined chain
result = story_with_analysis.invoke({"topic": "a rainy day"})
print(result)
