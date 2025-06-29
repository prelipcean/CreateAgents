import time
from dotenv import load_dotenv
import google.generativeai as genai
import gradio as gr

# --- Configuration and Initialization ---

# Load environment variables from a .env file.
# Make sure your GOOGLE_API_KEY is set in this file.
load_dotenv()

# Configure the Google Generative AI client.
# The API key will be automatically picked up from the GOOGLE_API_KEY environment variable.
try:
    genai.configure()
except Exception as e:
    print(f"Error configuring Google Generative AI: {e}")
    print(
        "Please ensure your GOOGLE_API_KEY is correctly set in your .env file or environment variables."
    )
    exit()

# Define the system instruction for the AI model.
# This sets the overall persona or guidelines for the AI.
system_instruction = "You are a helpful and friendly AI assistant."

# Initialize the Generative Model globally.
# We use 'gemini-1.5-flash' for faster responses.
# The system_instruction is set here for the entire chat session.
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", system_instruction=system_instruction
)

# Initialize a chat session.
# The chat history will be managed by this object.
chat = model.start_chat(history=[])

# --- Helper Function for Gradio History Transformation ---


def transform_history_to_gemini_format(gradio_history: list) -> list:
    """
    Transforms Gradio's 'messages' chat history format into Gemini API's message format.
    Gradio history is now a list of dicts with 'role' and 'content'.
    Gemini expects a list of dicts with 'role' and 'parts'.
    """
    gemini_history = []
    for msg in gradio_history:
        if msg.get("role") and msg.get("content"):
            # Map Gradio's 'assistant' role to Gemini's 'model'
            role = "model" if msg["role"] == "assistant" else msg["role"]
            gemini_history.append({"role": role, "parts": [{"text": msg["content"]}]})
    return gemini_history


# --- Gradio Chat Interface Function ---


def respond(message: str, history: list):
    """
    This function is called by Gradio's ChatInterface for each user message.
    It manages the chat history and streams the AI's response.
    """
    global chat

    # Update the Gemini chat object's history with the current Gradio history.
    # This ensures the model has the full context of the conversation.
    chat.history = transform_history_to_gemini_format(history)

    # Send the current user message to the Gemini model in streaming mode.
    # Safety settings are applied here for each message.
    try:
        stream = chat.send_message(
            message,
            safety_settings=[
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_NONE",
                },
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            ],
            stream=True,
        )

        response_text = ""
        # Iterate over the streamed chunks and yield partial responses
        for chunk in stream:
            # Check if chunk.text exists and is not empty
            if chunk.text:
                response_text += chunk.text
                yield response_text
            # Optional: Add a small delay for a more natural typing effect
            time.sleep(0.02)

    except Exception as e:
        error_message = f"An error occurred while generating response: {e}"
        print(error_message)
        yield "I'm sorry, I encountered an error. Please try again."


# --- Launch Gradio Interface ---

# Create the Gradio ChatInterface.
# The 'respond' function handles the AI's logic.
# 'textbox' provides a placeholder for user input.
iface = gr.ChatInterface(
    fn=respond,
    textbox=gr.Textbox(placeholder="Ask me anything!", container=False, scale=7),
    title="Gemini 1.5 Flash Conversational Chatbot",
    description="Chat with a helpful AI assistant powered by Google's Gemini 1.5 Flash model.",
    examples=[
        "What's the capital of France?",
        "Tell me a fun fact about space.",
        "Can you write a short poem?",
    ],
    theme="soft",
    type="messages",
)

# Launch the Gradio web interface.
# debug=True provides more detailed logging in the console.
iface.launch(debug=True)
