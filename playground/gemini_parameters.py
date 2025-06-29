"""
This script demonstrates basic interaction with the Google Gemini AI API,
focusing on generating a single-turn response with customizable parameters.

It performs the following steps:
1. Loads the Google API key from environment variables.
2. Configures the Gemini API client.
3. Defines a system message and a user prompt.
4. Initializes a Gemini GenerativeModel with a system instruction.
5. Sends the user prompt to the model with various generation configurations
   (e.g., temperature, top_p, top_k, max_output_tokens) to control the output.
6. Prints the model's generated response.
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai.types import GenerationConfig, HarmCategory, HarmBlockThreshold

# --- Configuration and API Key Loading ---

# Load environment variables from a .env file.
# This is crucial for securely managing API keys.
load_dotenv()

# Retrieve the Google API key from environment variables.
# It's recommended to store this in a .env file (e.g., GOOGLE_API_KEY="your_api_key_here").
google_api_key = os.getenv("GOOGLE_API_KEY")

# Validate if the Google API Key is set.
if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:8]}********")
else:
    print(
        "Error: Google API Key not set. Please ensure 'GOOGLE_API_KEY' is in your .env file or environment variables."
    )
    # Exit the script if the API key is not found, as it's essential for functionality.
    exit()

# Configure the Google Generative AI client.
# This connects your script to the Google Gemini API services.
genai.configure(api_key=google_api_key)

# --- Define Model Behavior and Prompts ---

# Define a system instruction for the model. This guides the model's overall persona or behavior.
# It acts as a high-level directive that influences all subsequent responses from this model instance.
system_message = "You are an assistant that is great at telling light-hearted jokes, especially for technical audiences."

# Define the user's specific prompt or question.
user_prompt = "Tell a light-hearted joke for an audience of Data Scientists."

# --- Model Initialization and Parameter Customization ---

# Initialize the GenerativeModel.
# 'gemini-1.5-flash' is a fast and efficient model suitable for many tasks.
# The `system_instruction` is passed here to set the model's enduring persona.
gemini_model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", system_instruction=system_message
)

# --- Generation Parameters ---
# These parameters control the creativity, determinism, and length of the model's response.
# Experiment with these values to fine-tune the model's output for your specific needs.

# `temperature`: Controls the randomness of the output.
# A higher temperature (e.g., 0.8 - 1.0) leads to more creative and diverse responses.
# A lower temperature (e.g., 0.1 - 0.4) makes the responses more deterministic and focused.
# Range: 0.0 to 2.0 (default is typically 1.0).
temperature_value = 0.9

# `top_p`: Nucleus sampling. Controls the diversity of the output by sampling from the
# smallest set of most probable tokens whose cumulative probability exceeds `top_p`.
# A lower `top_p` (e.g., 0.5) narrows the choices, leading to less diverse responses.
# A higher `top_p` (e.g., 0.9 or 1.0) allows for more diversity.
# Range: 0.0 to 1.0 (default is typically 1.0).
top_p_value = 0.95

# `top_k`: Top-k sampling. Limits the sampling to the top `k` most probable tokens at each step.
# A lower `top_k` (e.g., 1 or 5) makes the model choose from very few high-probability tokens.
# A higher `top_k` (e.g., 40 or 50) allows for a wider range of token choices, increasing diversity.
# Range: Integer value (default is often not explicitly set or a high value like 40).
top_k_value = 40

# `max_output_tokens`: The maximum number of tokens the model is allowed to generate in its response.
# A token is roughly 4 characters. Adjust this to control the length of the response.
max_output_tokens_value = 150  # Limiting to 150 tokens for a concise joke.

# Create a GenerationConfig object to pass these parameters.
generation_config = GenerationConfig(
    temperature=temperature_value,
    top_p=top_p_value,
    top_k=top_k_value,
    max_output_tokens=max_output_tokens_value,
    # You can also add `stop_sequences` here if you want the model to stop generating
    # when it encounters specific strings (e.g., stop_sequences=["\n\n", "END"]).
    # For example: stop_sequences=["\n\n"]
)

# --- Safety Settings (Optional but Recommended) ---
# These settings allow you to control the types of content the model might generate.
# By default, Gemini models have safety filters enabled. You can adjust thresholds.
# Example: Blocking none for all categories (use with caution, for specific use cases).
safety_settings = [
    {
        "category": HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": HarmCategory.HARM_CATEGORY_HARASSMENT,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
]


# --- Generate Content ---
print(f"\n--- Generating response for: '{user_prompt}' ---")
print(
    f"Using Temperature: {temperature_value}, Top_P: {top_p_value}, Top_K: {top_k_value}, Max Output Tokens: {max_output_tokens_value}\n"
)

# Send the user prompt to the Gemini model with the specified generation configuration and safety settings.
try:
    # Send the user prompt to the Gemini model with the specified generation configuration and safety settings.
    response = gemini_model.generate_content(
        user_prompt, generation_config=generation_config, safety_settings=safety_settings
    )
    # Print the text content of the model's response.
    print(response.text)
except Exception as e:
    print(f"Error generating content: {e}")

# --- Additional Notes on Parameters ---
# Other parameters you might encounter (less common for basic text generation but available):
# - `seed`: For reproducibility. When fixed to a specific value, the model makes a best effort
#           to provide the same response for repeated requests, though determinism is not guaranteed.
#           Example: `seed=1234` in `GenerationConfig`.
# - `response_mime_type`: Specifies the desired output format, e.g., "application/json" for structured output.
#           This is used when you want the model to return JSON directly.
#           Example: `response_mime_type="application/json"` in `GenerationConfig`.
# - `thinking_config`: For models that support "thinking" (e.g., Gemini 2.5 Pro), allows you to
#           control the model's internal reasoning budget.
#           Example: `thinking_config=genai.types.ThinkingConfig(thinking_budget=1024)` in `GenerationConfig`.
#           (Note: Requires `from google.generativeai import types` for `ThinkingConfig`).
