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
9.  [Code Linting and Formatting with Ruff](#9-code-linting-and-formatting-with-ruff)
10. [Contributing](#10-contributing)
11. [License](#11-license)

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
├── demos/                # Directory for various agent demos
├── playground/           # Experimental scripts, notebooks, and quick tests
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

This project is configured to work with a wide range of LLM providers and models, ensuring flexibility and broad applicability. Our dependency setup facilitates integration with various models through:

  * **Key LLM Families (Direct Integration & LangChain)**:

      * **Anthropic Claude**: Excels in reasoning, long-form content processing, and vision analysis with up to 200K token context windows (via `anthropic`, `langchain-anthropic`).
      * **Mistral models**: Powerful open-source models with strong multilingual capabilities and exceptional reasoning abilities (via `langchain_mistralai`).
      * **Google Gemini**: Advanced multimodal models with industry-leading 1M token context window and real-time information access (via `google-generativeai`, `langchain-google-genai`).
      * **OpenAI GPT-o**: Leading omnimodal capabilities accepting text, audio, image, and video with enhanced reasoning (via `openai`, `langchain-openai`).
      * **DeepSeek models**: Specialized in coding and technical reasoning with state-of-the-art performance on programming tasks.
      * **AI21 Labs Jurassic**: Strong in academic applications and long-form content generation.
      * **Inflection Pi**: Optimized for conversational AI with exceptional emotional intelligence.
      * **Perplexity models**: Focused on accurate, cited answers for research applications (via `langchain-perplexity`).
      * **Cohere models**: Specialized for enterprise applications with strong multilingual capabilities (via `cohere`, `langchain-cohere`).

  * **Cloud Provider Gateways**: These offer managed API access to various models, often with enterprise-grade features and seamless integration within their cloud ecosystems.

      * **Amazon Bedrock**: Unified API access to models from Anthropic, AI21, Cohere, Mistral, and others with deep AWS integration.
      * **Azure OpenAI Service**: Enterprise-grade access to OpenAI and other models with robust security and Microsoft ecosystem integration.
      * **Google Vertex AI**: Access to Gemini and other models with seamless Google Cloud integration (via `google-cloud-aiplatform`, `langchain-google-vertexai`).

  * **Independent Platforms & Local/Open Source**:

      * **Together AI**: Hosts 200+ open-source models with both serverless and dedicated GPU options.
      * **Replicate**: Specializes in deploying multimodal open-source models with pay-as-you-go pricing.
      * **Hugging Face Inference Endpoints**: Provides production deployment of thousands of open-source models with fine-tuning capabilities (via `transformers`, `huggingface-hub`, `langchain_huggingface`).
      * **LiteLLM**: A unified API for interacting with over 100+ LLM providers, offering unparalleled flexibility in switching models (via `litellm`).
      * **Local LLMs (via Ollama)**: Supports running models locally with ease (via `ollama`, `langchain-ollama`, and `autogen-ext`).

### API keys reference table

  | Provider        | Environment Variable         | Setup URL                                        | Free Tier?        |
| :-------------- | :--------------------------- | :----------------------------------------------- | :---------------- |
| **OpenAI**          | `OPENAI_API_KEY`             | [platform.openai.com](https://platform.openai.com/account/api-keys) | No                |
| **Hugging Face**    | `HUGGINGFACE_API_KEY`   | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) | Yes               |
| **Anthropic**       | `ANTHROPIC_API_KEY`          | [console.anthropic.com](https://console.anthropic.com/settings/api-keys) | No                |
| **Google AI**       | `GOOGLE_API_KEY`             | [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) | Yes               |
| **Google Vertex AI** | `GOOGLE_APPLICATION_CREDENTIALS` | [cloud.google.com/vertex-ai](https://cloud.google.com/docs/authentication/application-default-credentials) | Yes (with limits) |
| **Replicate**       | `REPLICATE_API_TOKEN`        | [replicate.com](https://replicate.com/account)    | No                |

### Vector stores reference table

| Database              | Deployment Options     | License                | Notable Features                                                                                                    |
|-----------------------|------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------|
| **Pinecone**              | Cloud-only             | Commercial             | Auto-scaling, enterprise security, monitoring, real-time index updates, purpose-built for high-dimensional data      |
| **Milvus**                | Cloud, Self-hosted     | Apache 2.0             | HNSW/IVF indexing, multi-modal support, CRUD operations, distributed architecture, highly scalable                 |
| **Weaviate**              | Cloud, Self-hosted     | BSD 3-Clause           | Graph-like structure, multi-modal support, semantic search, GraphQL API, built-in vectorization, hybrid search      |
| **Qdrant**                | Cloud, Self-hosted     | Apache 2.0             | HNSW indexing, filtering optimization, JSON metadata, payload filtering, Rust-powered performance, cloud-native     |
| **ChromaDB**              | Cloud, Self-hosted     | Apache 2.0             | Lightweight, easy setup, in-memory or persistent, Python-first, great for prototyping and smaller-to-medium scale |
| **AnalyticDB-V**          | Cloud-only             | Commercial             | OLAP integration, SQL support, enterprise features, optimized for Alibaba Cloud ecosystem                          |
| **pg_vector**             | Cloud, Self-hosted     | PostgreSQL License     | SQL support, PostgreSQL integration, efficient exact and approximate nearest neighbor search within PostgreSQL      |
| **Vertex Vector Search**  | Cloud-only             | Commercial             | Easy setup, low latency, high scalability, Google Cloud integration, managed service                               |
| **Vald** | Self-hosted            | Apache 2.0             | Highly scalable, distributed vector search engine, built on top of Faiss, focuses on stability and operations      |
| **Deep Lake** | Cloud, Self-hosted     | Apache 2.0             | Stores vectors and other data formats (images, audio) in a queryable "tensor database," version control for data    |
| **Elasticsearch** | Cloud, Self-hosted     | Apache 2.0 (basic) / Commercial (advanced features) | Full-text search and analytics, integrates vector search (k-NN) with existing search capabilities, flexible schema |
| **Redis Stack (RedisGears + RediSearch)** | Cloud, Self-hosted | RSALv2 / SSPL (Redis core) / Apache 2.0 (modules) | In-memory data store, vector search as a module, fast for real-time applications, flexible data structures         |
| **MongoDB Atlas Vector Search** | Cloud-only (Atlas) | Commercial             | Integrated with MongoDB Atlas, combines vector search with document database features, simplified development       |
| **Vespa** | Cloud, Self-hosted     | Apache 2.0             | Open-source data serving engine, supports vector, lexical, and structured search, used by Yahoo! for large scale    |
| **LanceDB** | Self-hosted, Cloud (integrations) | Apache 2.0             | Serverless, embedded vector database built with Rust, ideal for edge/local AI applications, integrates with cloud storage |

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

### Model controlling parameters table

| Parameter | Description | Typical Range | Best For |
|---|---|---|---|
| **Temperature** | Controls randomness in text generation | 0.0-1.0 (OpenAI, Anthropic); 0.0-2.0 (Gemini) | Lower (0.0-0.3): Factual tasks, Q&A; Higher (0.7+): Creative writing, brainstorming |
| **Top-k** | Limits token selection to k most probable tokens | 1-100 | Lower values (1-10): More focused outputs; Higher values: More diverse completions |
| **Top-p (Nucleus Sampling)** | Considers tokens until cumulative probability reaches threshold | 0.0-1.0 | Lower values (0.5): More focused outputs; Higher values (0.9): More exploratory responses |
| **Max tokens** | Limits maximum response length | Model-specific | Controlling costs and preventing verbose outputs |
| **Presence/frequency penalties** | Discourages repetition by penalizing tokens that have appeared | -2.0 to 2.0 | Longer content generation where repetition is undesirable |
| **Stop sequences** | Tells model when to stop generating | Custom strings | Controlling exact ending points of generation |
| **Seed** | Initializes the random number generator for reproducible outputs | Integer (e.g., 0, 42) | Reproducibility, A/B testing, debugging |
| **Logit Bias** | Directly influences the probability of specific tokens appearing or being avoided | Model/API specific (e.g., -100 to 100) | Guiding specific vocabulary, preventing unwanted words, enforcing style |
| **Context Window Size** | Maximum number of tokens (input + output) the model can consider | Model-specific (e.g., 4K, 8K, 32K, 128K) | Maintaining coherence over long interactions, processing large inputs |
| **`do_sample`** | Boolean to enable/disable probabilistic sampling (vs. greedy decoding) | `True`/`False` | Ensuring purely deterministic output (set to `False`) |

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

## 9\. Code Linting and Formatting with Ruff

We use [`ruff`](https://docs.astral.sh/ruff/) for fast, comprehensive Python linting and code formatting.

### Installing Ruff

Ruff is included in the `[dev]` dependency group. If you haven't already, install all dev dependencies:

```bash
uv sync
```

### Basic Usage

- **Check code for lint issues:**
  ```bash
  ruff check src playground demos tests
  ```

- **Automatically fix fixable issues:**
  ```bash
  ruff check src playground demos tests --fix
  ```

- **Format code (like `black`):**
  ```bash
  ruff format src playground demos tests
  ```

- **Check the entire project:**
  ```bash
  ruff check .
  ```

### Configuration

You can customize Ruff's behavior in `pyproject.toml` or a `.ruff.toml` file.

### Tips

- Integrate Ruff with your editor for real-time linting.
- Add Ruff to pre-commit hooks for automatic checks before each commit.

For more details, see the [Ruff documentation](https://docs.astral.sh/ruff/).

## 10\. Contributing

We welcome contributions to this project\! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bugfix (`git checkout -b feature/your-feature-name`).
3.  Make your changes and ensure they are well-tested.
4.  Commit your changes (`git commit -m "feat: Add new agent capability"`).
5.  Push to your branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request to the `main` branch of this repository.

Please ensure your code adheres to the existing style and conventions. We use `ruff` for linting and formatting (part of our `dev` dependencies).

## 11\. License

This project is licensed under the MIT License - see the [`LICENSE`](./LICENSE) file for details.

-----