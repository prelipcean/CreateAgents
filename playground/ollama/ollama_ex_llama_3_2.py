"""
This script demonstrates how to interact with the 'llama3.2:latest' Large Language Model (LLM)
served by Ollama directly through its REST API using Python's 'requests' library.
This allows for direct communication with Ollama's native API endpoints,
bypassing the OpenAI compatibility layer.

It performs the following steps:
1. Imports the necessary 'requests' and 'json' libraries.
2. Defines the URL for Ollama's local chat completion API endpoint.
3. Specifies the local model to be used: "llama3.2:latest".
4. Crafts a message payload in Ollama's native chat format.
5. Sends an HTTP POST request to the Ollama API.
6. Parses the JSON response and prints the LLM's generated content.
"""

import requests
import json  # Used for properly formatting the JSON payload

# --- Ollama API Configuration ---

# The base URL for your local Ollama instance.
# Ollama typically listens on port 11434 by default.
OLLAMA_API_BASE_URL = "http://localhost:11434"

# The specific endpoint for chat completions.
# Ollama has both /api/generate (for single-turn prompts) and /api/chat (for conversational turns).
# For chat, /api/chat is generally preferred as it supports the 'messages' array.
CHAT_COMPLETIONS_ENDPOINT = f"{OLLAMA_API_BASE_URL}/api/chat"

# Specify the model name. This is the only change from the previous script.
# Make sure you have this model pulled in your local Ollama instance: `ollama pull llama3.2:latest`
MODEL_NAME = "llama3.2:latest"

# --- Define User Prompt and Message Structure ---

# The content of the user's message.
user_message_content = "Considering the current global economic outlook, what are 3 key trends that could significantly impact the tech industry in the next 12-18 months? Provide a brief explanation for each."

# Ollama's `/api/chat` endpoint expects a list of message objects,
# similar to the OpenAI chat completions format.
# Each message should have a 'role' (e.g., "user", "system", "assistant") and 'content'.
messages_payload = [{"role": "user", "content": user_message_content}]

# --- Optional: Generation Parameters ---
# These parameters control the model's behavior and response characteristics.
# They are nested under an 'options' key in the request body for Ollama's native API.
# Experiment with these values to fine-tune the model's output for your specific needs.
# For Llama 3.2, a higher context length (128K tokens) means it can handle much longer inputs.

generation_options = {
    "temperature": 0.6,  # A bit less random for more focused trends
    "num_predict": 700,  # Allow for a more detailed explanation for each trend
    "top_p": 0.9,  # Broaden token selection slightly
    "top_k": 50,  # Consider a larger pool of top tokens
    # "stop": ["\n\nTrend 4:", "\n\nConclusion"], # Example of a stop sequence
    # "seed": 123 # For reproducibility
}

# --- Construct the Request Body ---

# The full JSON payload for the POST request.
request_body = {
    "model": MODEL_NAME,
    "messages": messages_payload,
    "options": generation_options,
    "stream": False,  # Set to True for streaming responses (requires different handling)
}

# --- Send Request and Process Response ---

print(f"--- Sending request to Ollama with model: {MODEL_NAME} ---")
print(f"Request URL: {CHAT_COMPLETIONS_ENDPOINT}")
print(f"User prompt: '{user_message_content}'\n")

try:
    # Send the POST request to the Ollama API.
    # `json=request_body` automatically sets 'Content-Type: application/json' header.
    response = requests.post(CHAT_COMPLETIONS_ENDPOINT, json=request_body)

    # Raise an HTTPError for bad responses (4xx or 5xx status codes)
    response.raise_for_status()

    # Parse the JSON response from Ollama.
    response_data = response.json()

    # The response structure for /api/chat typically has 'message' and 'content' nested.
    if "message" in response_data and "content" in response_data["message"]:
        ollama_response_content = response_data["message"]["content"]
        print("Ollama's Response:")
        print(ollama_response_content)
    else:
        print("Unexpected response format from Ollama:")
        print(
            json.dumps(response_data, indent=2)
        )  # Pretty print the unexpected response

except requests.exceptions.ConnectionError:
    print(f"Error: Could not connect to Ollama server at {OLLAMA_API_BASE_URL}.")
    print(
        "Please ensure Ollama is running (`ollama serve` in your terminal or as a background service)."
    )
    print(
        f"Also, confirm the model '{MODEL_NAME}' is downloaded (`ollama pull {MODEL_NAME}`)."
    )
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
    print(f"Response content: {e.response.text}")
except json.JSONDecodeError:
    print(
        "Error: Could not decode JSON response from Ollama. The response might not be valid JSON."
    )
    print(f"Raw response: {response.text}")  # Print raw response for debugging
except Exception as e:
    print(f"An unexpected error occurred: {e}")
