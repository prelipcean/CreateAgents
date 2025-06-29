"""
This script demonstrates how to interact with a local Large Language Model (LLM)
served by Ollama, using the OpenAI Python client library. This setup allows
developers to leverage the familiar OpenAI API interface for local models.

It performs the following steps:
1. Initializes the OpenAI client, configured to connect to your local Ollama server.
2. Specifies the local model to be used (e.g., "gemma3:27b").
3. Defines a user prompt for the LLM.
4. Sends a chat completion request to the Ollama-served model.
5. Prints the model's generated response.
"""

from openai import OpenAI  # Import the OpenAI library

# --- Configuration for Ollama ---

# Ollama typically runs on localhost:11434 by default.
# The `base_url` parameter of the OpenAI client points to your local Ollama API endpoint.
# The `api_key` can be any string (e.g., 'ollama') as it's required by the OpenAI client
# but not used for authentication by Ollama's local server.
ollama_client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Required by the OpenAI client, but not actually used by Ollama
)

# Specify the model name. This must be a model that you have pulled and is
# available in your local Ollama instance (e.g., by running 'ollama pull gemma3:27b').
model_name = "gemma3:27b"

# --- Define User Prompt ---

# The message to send to the LLM.
user_prompt_content = (
    "What are the key benefits of using local LLMs like Gemma with Ollama?"
)

# Messages are structured as a list of dictionaries, following the OpenAI chat completions format.
# A "user" role is used for the prompt we are sending.
messages = [{"role": "user", "content": user_prompt_content}]

# --- Generate Content using Ollama (via OpenAI client) ---

print(f"--- Sending request to Ollama with model: {model_name} ---")
print(f"User prompt: '{user_prompt_content}'\n")

try:
    # Send the chat completion request to your local Ollama server.
    # The `create` method takes the model name and the list of messages.
    # You can also add other parameters here like:
    # - `temperature`: Controls randomness (e.g., `temperature=0.7`)
    # - `max_tokens`: Limits response length (e.g., `max_tokens=200`)
    # - `top_p`: Nucleus sampling (e.g., `top_p=0.9`)
    # - `stream`: If set to `True`, the response will be streamed back in chunks.
    response = ollama_client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.7,  # Example: Adjust for creativity (0.0 to 1.0)
        max_tokens=500,  # Example: Limit response length
    )

    # Extract and print the model's response.
    # The response structure is the same as for OpenAI's API.
    if response.choices:
        print("Ollama's Response:")
        print(response.choices[0].message.content)
    else:
        print("No response received from Ollama.")

except Exception as e:
    print(f"An error occurred: {e}")
    print("\nTroubleshooting tips:")
    print(
        "1. Ensure Ollama is running in your terminal (`ollama serve` or as a background service)."
    )
    print(
        f"2. Confirm the model '{model_name}' is downloaded (`ollama list` to check, `ollama pull {model_name}` to download)."
    )
    print(
        "3. Verify the `base_url` (`http://localhost:11434/v1`) matches your Ollama setup."
    )
