from transformers import AutoTokenizer

# Specify the original Hugging Face model name for Llama 3
# This is NOT the Ollama model name, but the original HF model.
hf_llama_model_name = "meta-llama/Llama-3-8B-Instruct"

try:
    # Load the tokenizer for Llama-3-8B-Instruct from Hugging Face Hub
    # This will download the tokenizer files if not already cached.
    llama_tokenizer = AutoTokenizer.from_pretrained(hf_llama_model_name)

    # Text to tokenize
    text_to_tokenize = "This is an example sentence for Llama 3 tokenization."

    # Tokenize the text
    encoded_text = llama_tokenizer(text_to_tokenize)

    print(
        f"--- Tokenization with Hugging Face AutoTokenizer for {hf_llama_model_name} ---"
    )
    print(f"Original Text: '{text_to_tokenize}'")
    print(
        f"Decoded (original form): {llama_tokenizer.decode(encoded_text['input_ids'])}"
    )
    print(f"Token IDs: {encoded_text['input_ids']}")
    # Decode each token ID separately for visualization
    print(
        f"Individual Tokens: {', '.join([llama_tokenizer.decode(t) for t in encoded_text['input_ids']])}"
    )

except Exception as e:
    print(f"Error loading or using tokenizer: {e}")
    print(
        "Ensure you have the 'transformers' library installed: `pip install transformers`"
    )
    print(
        f"Also, confirm '{hf_llama_model_name}' is a valid model on Hugging Face Hub and you have internet access."
    )

# You cannot pass these token IDs directly to Ollama's /api/chat endpoint.
# Ollama expects raw string content.
