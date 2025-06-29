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
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
import os
from dotenv import load_dotenv
from operator import itemgetter  # Used for extracting values from dictionaries

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

# --- Define Individual Chain Components ---

# First chain: Generates a story based on a provided topic.
# - `PromptTemplate.from_template`: Defines how the input {topic} is formatted for the LLM.
# - `| chat`: Passes the formatted prompt to the LLM.
# - `| StrOutputParser()`: Parses the LLM's raw output into a plain string.
story_prompt = PromptTemplate.from_template("Write a short story about {topic}")
story_chain = story_prompt | chat | StrOutputParser()

# Second chain: Analyzes the mood of a given story.
# - `PromptTemplate.from_template`: Defines how the input {story} is formatted for the LLM.
# - `| chat`: Passes the formatted story to the LLM for analysis.
# - `| StrOutputParser()`: Parses the LLM's raw output into a plain string.
analysis_prompt = PromptTemplate.from_template(
    "Analyze the following story's mood:\n{story}"
)
analysis_chain = analysis_prompt | chat | StrOutputParser()

# Output formatter prompt: Combines the generated story and its mood into a final display format.
# This prompt expects both `story` and `mood` as input variables.
output_prompt = PromptTemplate.from_template(
    "Here's the story: \n{story}\n\nHere's the mood: \n{mood}"
)

# --- Combine Chains using LangChain Expression Language (LCEL) ---

# This complex chain orchestrates the flow:
# 1. Initial Input: Receives a dictionary with 'topic' (e.g., {"topic": "a lonely astronaut"}).
# 2. First Branch (`{ "story": story_chain, "topic": RunnablePassthrough(), }`):
#    - `"story": story_chain`: Runs `story_chain` using the `topic` from the initial input
#      and assigns its output (the generated story) to the `story` key.
#    - `"topic": RunnablePassthrough()`: Passes the original `topic` input through,
#      making it available in the subsequent steps (though not directly used until `output_prompt` implicitly).
#    Result of this step: A dictionary like `{"story": "...", "topic": "..."}`.
# 3. Parallel Execution (`| RunnableParallel(...)`):
#    This takes the dictionary from the previous step and creates new keys:
#    - `story=itemgetter("story")`: Simply extracts the `story` value from the incoming dictionary.
#      `itemgetter` is a concise way to create a runnable that extracts a key.
#    - `mood=({"story": itemgetter("story")} | analysis_chain)`:
#      - `{"story": itemgetter("story")}`: Creates a new dictionary, explicitly mapping the
#        extracted `story` to the `story` input expected by `analysis_chain`.
#      - `| analysis_chain`: Runs the `analysis_chain` with this `{"story": ...}` input.
#    Result of this step: A dictionary like `{"story": "...", "mood": "..."}`.
# 4. Final Formatting (`| output_prompt | chat | StrOutputParser()`):
#    - `| output_prompt`: The dictionary `{"story": "...", "mood": "..."}` is passed to `output_prompt`,
#      which formats it.
#    - `| chat | StrOutputParser()`: The formatted text is sent to the LLM for final rendering
#      (though it might just pass through if the prompt is purely for formatting) and then parsed to a string.
story_with_analysis = (
    {
        "story": story_chain,
        "topic": RunnablePassthrough(),
    }
    | RunnableParallel(
        story=itemgetter("story"),
        mood=({"story": itemgetter("story")} | analysis_chain),
    )
    | output_prompt
    | chat
    | StrOutputParser()
)

# --- Run the Combined Chain ---

print("--- Running combined chain ---")
# Invoke the final chain with the initial 'topic' input.
result = story_with_analysis.invoke({"topic": "a lonely astronaut"})
print(result)
