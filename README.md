# CreateAgents

A repository dedicated to exploring and building versatile AI agents using LangChain and a wide array of supporting tools. This project aims to provide a robust and extensible environment for developing intelligent agents capable of interacting with various models and performing complex tasks.

## Table of Contents

1.  [Introduction](#1-introduction)
2.  [Why `uv`?](#2-why-uv)
3.  [Getting Started with `uv`](#3-getting-started-with-uv)
    * [Installation](#installation)
    * [Project Setup](#project-setup)
    * [Managing Dependencies](#managing-dependencies)
    * [Activating the Virtual Environment](#activating-the-virtual-environment)
4.  [Project Structure](#4-project-structure)
5.  [Supported LLM Models and Providers](#5-supported-llm-models-and-providers)
6.  [Agentic Frameworks Used](#6-agentic-frameworks-used)
7.  [Tools and Capabilities](#7-tools-and-capabilities)
8.  [Running Demos](#8-running-demos)
9.  [Contributing](#9-contributing)
10. [License](#10-license)

-----

## 1\. Introduction

This repository is your starting point for building sophisticated AI agents. We leverage the power of [LangChain](https://www.langchain.com/) as our primary framework, enabling seamless integration with Large Language Models (LLMs), external tools, and memory components. Our goal is to create agents that are not only powerful but also adaptable to the ever-evolving landscape of AI models and data sources.

We prioritize a clean, efficient development workflow, and to achieve this, we rely on `uv` for lightning-fast and reliable dependency management.

## 2\. Why `uv`?

`uv` is a modern, Rust-based Python package and project manager developed by Astral (the creators of `ruff`). It offers significant advantages over traditional tools like `pip` and `pip-tools`, making our development experience smoother and faster:

  * **Blazing Fast Performance**: `uv` is 10-100x faster than `pip` for package installation and dependency resolution, dramatically reducing setup and build times.
  * **Unified Tooling**: It combines functionalities of `pip`, `pip-tools`, `virtualenv`, and more into a single, intuitive CLI.
  * **Reproducible Environments**: `uv` generates `uv.lock` files that precisely pin all direct and transitive dependencies, ensuring consistent environments across different machines and deployments.
  * **Built-in Virtual Environment Management**: Simplifies environment creation and activation.
  * **Compatibility**: Designed to be a drop-in replacement for `pip` and compatible with existing `requirements.txt` workflows.
  * **Low Resource Footprint**: Efficiently uses memory and disk space, especially beneficial for large projects.

By using `uv`, we aim to spend less time managing dependencies and more time building intelligent agents.

## 3\. Getting Started with `uv`

Follow these steps to set up your development environment and get started with `CreateAgents`.

### Installation

First, you need to [install](https://docs.astral.sh/uv/getting-started/installation/) `uv` on your system.

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (using PowerShell):**

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

After installation, verify that `uv` is properly installed:

```bash
uv --version
```

### Project Setup

Navigate to the root of this repository in your terminal. `uv` will automatically detect the `pyproject.toml` file.

### Managing Dependencies

This project uses `pyproject.toml` for dependency management. To install all the required dependencies (both `[project].dependencies` and `[dependency-groups].dev`), use `uv sync`:

```bash
uv sync
```

This command will:

1.  Create a virtual environment (if one doesn't exist).
2.  Resolve all dependencies declared in `pyproject.toml`.
3.  Install them into the virtual environment.
4.  Generate or update the `uv.lock` file, ensuring exact dependency versions for reproducibility.

To install only the core project dependencies (excluding `dev` dependencies), you can run:

```bash
uv sync --no-dev
```

### Activating the Virtual Environment

To ensure your Python commands (like `python` and `pip`) use the packages installed by `uv`, activate the virtual environment:

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```powershell
.venv\Scripts\activate
```

You'll know it's active when your terminal prompt changes (e.g., `(.venv) yourusername@yourmachine:~/CreateAgents$`).

## 4\. Project Structure

(This section is a placeholder for when you define your project's code structure.)

```
.
├── .uv/                  # uv's cache and internal files (managed by uv)
├── .venv/                # Python virtual environment (managed by uv)
├── demos/                # Directory for various agent demos (e.g., `web_research_agent`, `email_agent`)
│   ├── web_research_agent/
│   │   ├── main.py
│   │   └── config.py
│   └── email_agent/
│       ├── agent.py
│       └── tools.py
├── src/                  # Core modules, reusable components, and custom tools
│   ├── agents/
│   ├── tools/
│   └── utils/
├── tests/                # Unit and integration tests
├── .env.example          # Example file for environment variables (API keys, etc.)
├── pyproject.toml        # Project metadata and dependency definitions (managed by uv)
├── uv.lock               # Locked dependency versions (generated and managed by uv)
└── README.md             # This file
```

## 5\. Supported LLM Models and Providers

This project is configured to work with a wide range of LLM providers and models, ensuring flexibility and broad applicability:

  * **OpenAI**: GPT-3.5, GPT-4, etc. (via `openai`, `langchain-openai`)
  * **Anthropic**: Claude models (via `anthropic`, `langchain-anthropic`)
  * **Google Generative AI**: Gemini models (via `google-generativeai`, `langchain-google-genai`)
  * **Google Cloud Vertex AI**: Access to Gemini, Codey, and custom models hosted on Google Cloud's AI platform (via `google-cloud-aiplatform`, `langchain-google-vertexai`)
  * **Hugging Face**: Numerous open-source models (via `transformers`, `langchain-huggingface`)
  * **Cohere**: Various Cohere models (via `cohere`, `langchain-cohere`)
  * **Perplexity AI**: Online LLMs known for real-time search and citations (via `langchain-perplexity`)
  * **LiteLLM**: A unified API for interacting with over 100+ LLM providers, offering unparalleled flexibility in switching models (via `litellm`).
  * **Local LLMs (via Ollama)**: Support for running models locally using Ollama (via `ollama` and `autogen-ext`).

## 6\. Agentic Frameworks Used

We primarily leverage these powerful frameworks for agent orchestration:

  * **LangChain**: The foundational framework for building LLM-powered applications, providing core abstractions for models, prompts, chains, and agents.
  * **LangGraph**: Built on LangChain, `LangGraph` allows building stateful, multi-actor applications with cyclical graphs, ideal for complex agentic reasoning and human-in-the-loop workflows.
  * **AutoGen**: A framework for enabling development of LLM applications using multiple agents that can converse with each other to solve tasks.
  * **CrewAI**: A framework for orchestrating role-playing autonomous AI agents for collaborative task execution.
  * **LlamaIndex**: While primarily focused on data indexing and retrieval for RAG, it also offers strong agentic capabilities and is often used in conjunction with LangChain.

## 7\. Tools and Capabilities

Our agents can leverage a diverse set of tools to interact with the world:

  * **Web Scraping & Data Extraction**: `Beautiful Soup 4` (`bs4`), `lxml`, `Playwright`, `Unstructured` (for parsing various document types).
  * **Document Handling**: `PyPDF`, `PyPDF2`, `python-docx`, `openpyxl` for PDF, Word, and Excel files.
  * **Google Services**: `google-api-python-client`, `google-auth` for interacting with various Google APIs.
  * **Financial Data**: `polygon-api-client`.
  * **Communication**: `SendGrid` for email.
  * **Information Retrieval**: `Wikipedia` for general knowledge.
  * **System Utilities**: `psutil`, `speedtest-cli`.
  * **Data Manipulation**: `pandas`, `numpy` for powerful data processing.
  * **Visualization**: `Plotly` for interactive charts.
  * **Microsoft Ecosystem**: `Semantic Kernel` for integration with Microsoft AI services.
  * **Robustness**: `Tenacity` for resilient API calls with retries.
  * **UI/Demo**: `Gradio` for quickly building interactive web demos of agents.
  * **Foundational Packaging**: `setuptools` for core Python packaging mechanisms.

## 8\. Running Demos

This section will contain instructions on how to run specific agent demos within the `demos/` directory.

### Example: Running the `Web Research Agent` Demo

(Placeholder: Detailed instructions will go here once the demos are created. This could include):

```bash
# Example: Navigate to a specific demo directory
cd demos/web_research_agent

# Ensure you have your .env file configured with necessary API keys (e.g., OPENAI_API_KEY, GOOGLE_API_KEY, PERPLEXITY_API_KEY)
cp ../.env.example .env
# Open .env and fill in your keys

# Run the demo script
python main.py
```

We will provide clear, step-by-step guides for each demo, including any specific environment variables or configurations required.

## 9\. Contributing

We welcome contributions to this project\! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bugfix (`git checkout -b feature/your-feature-name`).
3.  Make your changes and ensure they are well-tested.
4.  Commit your changes (`git commit -m "feat: Add new agent capability"`).
5.  Push to your branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request to the `main` branch of this repository.

Please ensure your code adheres to the existing style and conventions. We use `ruff` for linting and formatting (part of our `dev` dependencies).

## 10\. License

This project is licensed under the MIT License - see the [`LICENSE`](./LICENSE) file for details.

-----