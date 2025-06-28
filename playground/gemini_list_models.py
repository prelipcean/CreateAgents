"""
Google Gemini AI Model Demo

This script demonstrates how to use Google's Gemini AI model through the google-generativeai Python package.
It covers:
1. Setting up the environment and API key
2. Listing available Gemini models
3. Making a simple query to the model

Prerequisites:
- A Google API key (set in .env file as GOOGLE_API_KEY)
- Required packages installed: google-generativeai, python-dotenv, requests, beautifulsoup4
- Python 3.12 or later

Usage:
    1. Ensure your .env file contains GOOGLE_API_KEY.
    2. Install dependencies:
        pip install google-generativeai python-dotenv requests beautifulsoup4
    3. Run this script:
        python playground/gemini_list_models.py
"""

# Standard library imports
import os
import logging
from typing import Optional

# Third-party imports
from dotenv import load_dotenv

# Google Generative AI import
import google.generativeai as genai

# Configure logging to suppress gRPC and TensorFlow warnings
logging.basicConfig(level=logging.ERROR)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # Suppress TensorFlow logging

# Suppress specific gRPC warnings (optional, for cleaner output)
try:
    import absl.logging

    absl.logging.set_verbosity(absl.logging.ERROR)
except ImportError:
    pass


def setup_gemini_api() -> None:
    """
    Set up the Gemini API with the API key from environment variables.

    Raises:
        ValueError: If the GOOGLE_API_KEY environment variable is not set
    """
    # Load environment variables from .env file
    load_dotenv(override=True)
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not set. Please set it in your environment or .env file."
        )
    genai.configure(api_key=api_key)


def display_available_models() -> None:
    """
    Display all available Gemini models that support content generation.

    Lists models with their names, display names, and supported methods.
    Useful for choosing the appropriate model for your use case.
    """
    print("Available models that support 'generateContent':")
    print("-" * 50)
    for model in genai.list_models():
        if "generateContent" in model.supported_generation_methods:
            print(f"Model: {model.name}")
            print(f"Display Name: {model.display_name}")
            print(f"Supported Methods: {', '.join(model.supported_generation_methods)}")
            print("-" * 50)


def interact_with_gemini(
    message: str, model_name: str = "gemini-1.5-flash-latest", temperature: float = 0.7
) -> Optional[str]:
    """
    Send a message to Gemini and get the response.

    Args:
        message (str): The message to send to Gemini
        model_name (str): The name of the Gemini model to use
        temperature (float): Controls response randomness (0.0 to 1.0)

    Returns:
        Optional[str]: The model's response text, or None if an error occurs

    Example:
        >>> response = interact_with_gemini("Tell me about Python programming")
        >>> print(response)
    """
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(
            message, generation_config={"temperature": temperature}
        )
        return response.text
    except Exception as e:
        print(f"Error interacting with Gemini: {str(e)}")
        return None


def main():
    """
    Main function to demonstrate Gemini API usage:
    - Loads API key
    - Lists available models
    - Sends a test message to Gemini and prints the response
    """
    try:
        setup_gemini_api()
        print("\n=== Available Gemini Models ===\n")
        display_available_models()

        print("\n=== Testing Gemini Interaction ===\n")
        message_to_gemini = "Hello, Gemini! This is my first ever message to you! Hi!"
        response = interact_with_gemini(message_to_gemini)

        if response:
            print("Gemini's response:")
            print("-" * 20)
            print(response)
            print("-" * 20)
        else:
            print("No response received from Gemini.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
