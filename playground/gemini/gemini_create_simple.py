"""
This script demonstrates how to interact with the Google Gemini 2.5 Flash model
using the LangChain framework. It leverages LangChain's ChatGoogleGenerativeAI
integration to send conversational messages and receive responses.

The script performs the following steps:
1. Loads API keys from a .env file for secure environment setup.
2. Initializes the ChatGoogleGenerativeAI model, specifying 'gemini-2.5-flash'.
3. Defines a list of messages, including a system message to set the AI's persona
   and a human message containing the user's prompt.
4. Invokes the model with the prepared messages.
5. Prints the AI's generated response.
"""

import os
from dotenv import load_dotenv  # For loading environment variables
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)  # Import the Google Generative AI chat model
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)  # Standard LangChain message types
from langchain_core.outputs import Generation  # For type hinting the response structure

# --- Configuration and API Key Loading ---

# Load environment variables from a .env file.
# This makes your Google API Key accessible to the script.
load_dotenv()

# Verify that the Google API Key is set.
# ChatGoogleGenerativeAI will automatically look for GOOGLE_API_KEY.
google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key:
    print(f"Google API Key found (starts with {google_api_key[:8]}********)")
else:
    print("Error: GOOGLE_API_KEY not set in environment variables or .env file.")
    print("Please set your Google API Key before running this script.")
    exit()  # Exit if the API key is not available

# --- Initialize the Gemini Model with LangChain ---

# Initialize the ChatGoogleGenerativeAI model.
# Specify the model name as "gemini-2.5-flash".
# You can also add generation parameters here, such as:
# - `temperature`: Controls randomness (0.0 to 1.0)
# - `max_output_tokens`: Max length of the generated response
# Example: chat = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7, max_output_tokens=500)
print("\n--- Initializing ChatGoogleGenerativeAI with 'gemini-2.5-flash' ---")
chat_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# --- Define Messages for the Conversation ---

# Create a list of messages. LangChain uses a specific format for messages,
# with 'SystemMessage' to provide context/instructions and 'HumanMessage' for user input.
# This structure helps the model understand the conversational turns and roles.
messages_to_send = [
    SystemMessage(
        content="You're a helpful programming assistant that provides concise and correct Python code."
    ),
    HumanMessage(
        content="Write a Python function to calculate the factorial of a non-negative integer."
    ),
]

print("\n--- Sending message to the model ---")
for msg in messages_to_send:
    print(f"{msg.type.capitalize()}: {msg.content}")
print("-" * 30)

# --- Invoke the Model and Get Response ---

# Invoke the chat model with the list of messages.
# The `invoke` method sends the request to the LLM and returns the response.
try:
    response: Generation = chat_model.invoke(messages_to_send)

    # Print the AI's response content.
    # The response object from `invoke` contains the generated message.
    print("\n--- Model's Response ---")
    print(response.content)

except Exception as e:
    print(f"\nAn error occurred during model invocation: {e}")
    print("Ensure you have a valid GOOGLE_API_KEY and active internet connection.")
    print("Also, check the model name and your API usage limits.")
