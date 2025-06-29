"""
This script demonstrates how to interact with the Google Gemini AI API.

It performs the following steps:
1. Loads API keys from a .env file.
2. Initializes the Gemini GenAI client.
3. Sends a simple arithmetic question to the model.
4. Asks the model to generate a challenging IQ question.
5. Submits the generated IQ question back to the model and displays the answer.
"""

import os
from dotenv import load_dotenv
from google import genai
# from IPython.display import Markdown, display

# --- Configuration and Initialization ---

# Load environment variables from a .env file.
# The 'override=True' argument ensures that existing environment variables are overwritten.
load_dotenv(override=True)

# Retrieve the Gemini API key from environment variables.
gemini_api_key = os.getenv("GOOGLE_API_KEY")

# Validate if the Gemini API key is set.
if gemini_api_key:
    print(
        f"Gemini API Key exists and begins {gemini_api_key[:8]}********"
    )  # Mask part of the key for security
else:
    print(
        "Error: Gemini API Key not set. Please refer to the troubleshooting guide for assistance."
    )
    # Exit or raise an error if the API key is critical for further operations
    exit()

# Initialize the Gemini GenAI client with the retrieved API key.
# This client object will be used to make calls to the Gemini API.
client = genai.Client(api_key=gemini_api_key)

# --- Basic Interaction with Gemini AI ---

# Define a simple list of messages in the format expected by the Gemini GenAI API.
messages = ["What is 2+2?"]

# Send the basic arithmetic question to the Gemini model (gemini-2.0-flash).
# The response object contains the model's answer and other metadata.
response = client.models.generate_content(model="gemini-2.0-flash", contents=messages)

# Print the text content of the model's response to the simple question.
print("\n--- Basic Question Response ---")
print(response.text)

# --- Advanced Interaction: IQ Question Generation and Answering ---

# Define a prompt to ask the model to generate a challenging IQ question.
# We explicitly request only the question in the response.
iq_question_prompt = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question."

# Ask the Gemini model to generate the IQ question.
response_iq_question_gen = client.models.generate_content(
    model="gemini-2.0-flash", contents=iq_question_prompt
)

# Extract the generated IQ question from the model's response.
generated_iq_question = response_iq_question_gen.text

print("\n--- Generated IQ Question ---")
print(generated_iq_question)

# Now, submit the model-generated IQ question back to the same Gemini model to get an answer.
response_iq_answer = client.models.generate_content(
    model="gemini-2.0-flash", contents=generated_iq_question
)

# Extract the answer to the IQ question from the model's response.
iq_answer = response_iq_answer.text

# Print the raw answer for debugging or logging purposes.
print("\n--- Raw Answer to IQ Question ---")
print(iq_answer)

# Display the answer to the IQ question in a nicely formatted Markdown output.
# This is particularly useful in environments like Jupyter notebooks.
# print("\n--- Formatted Answer to IQ Question ---")
# display(Markdown(iq_answer))
