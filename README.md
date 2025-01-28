# Building Your (Local) LLM Second Brain

## Getting Started

### Quick Start

```sh
bash -c "$(curl -fsSL 'https://raw.githubusercontent.com/obuzek/llm-second-brain/main/get-lm-desk.sh')"
```

### Project-by-Project Install (MacOS)

1. Installing Ollama
```
```
2. Installing Granite 3.1
```
```
3. Installing VSCode and Continue
```
```
4. Installing AnythingLLM (alternatively, see OpenWebUI)
```
```
5. Creating a RAG database

## Principles

- **5-Minutes to Happiness**: You should be able to get up and running with these AI tools in 5 minutes or less (as long as you have a fast internet connection!)
- **Meet You Where You Are**: These tools should work seamlessly with the tools you already have installed on your machine without requiring you to change tools you already love.
- **Open Source:** All code is open source and freely available for anyone to use, modify, and distribute. All models have open weights and are freely available for anyone to use.
- **Interoperability:** The tools should be interoperable with each other so that they can be easily integrated into your workflow.
- **Business Friendly Licensing:** The tools should be business friendly licenses so that you can use them, modify them, and distribute them without any legal hurdles.

## Projects

### Local Model Serving

- [Ollama](https://ollama.com/) ([GitHub](https://github.com/ollama/ollama)): Ollama is an engine for managing and running multiple AI models in a local environment. Ollama follows the [OpenAI API spec](https://github.com/openai/openai-openapi), making calls to it compatible with other hosted options, and offers an easy-to-use CLI for managing your models.
- [ollama-bar](https://github.com/IBM/ollama-bar): `ollama-bar` is a bar macOS app that provides a menu-bar interface to manage Ollama and other tools that work with Ollama.

**Why Ollama?**

* Ollama uses [llama.cpp](https://github.com/ggerganov/llama.cpp) under the hood to perform model inference.
* The local-server-and-CLI model makes it very easy to use.
* The API mimicks OpenAI.

### Model - [`granite3.1-dense`](https://registry.ollama.com/library/granite3.1-dense)

Options:
- [IBM Granite Code](https://github.com/ibm-granite) ([HuggingFace](https://huggingface.co/collections/ibm-granite/granite-code-models-6624c5cec322e4c148c8b330), [GitHub](https://github.com/ibm-granite)): IBM Granite Code is a set of open weights AI models with permissive licenses that are tuned for code completion, documentation generation, and other development tasks.

**Why Granite?**

* High performance across a wide number of quality benchmarks, like IFEval, BBH, Math, GPQA, MUSR and MMLU-Pro.
* The latest models are small enough to fit on a single GPU, making running on your laptop a possibility.
* It's open sourced under an [Apache 2.0 License](https://registry.ollama.com/library/granite3.1-dense/blobs/492069a62c25).
* It offers tool-calling abilities.
* It was trained on curated high-quality data.
* Provides strong performance across summarization, classification, text extraction, multi-turn conversations, RAG and code generation and explanation.

For more open source models, check out [models on HuggingFace](https://huggingface.co/models) or in the [Ollama Registry](https://registry.ollama.com/search).
Look at the [Model Openness Tool](https://isitopen.ai/) for more details on the openness of various LLMs.

### AI-Infused Development

Requirement:
- [Visual Studio Code](https://code.visualstudio.com/) ([GitHub](https://github.com/microsoft/vscode)): Visual Studio Code is a free, open-source code editor developed by Microsoft. It can be extended with plugins to add support for generative AI models.

Options:
- [Continue](https://www.continue.dev/) ([GitHub](https://github.com/continuedev/continue)): Continue is an IDE plugin that brings together AI models to power your development workflow. It includes features such as code completion, debugging, and linting.

**Why Continue + VSCode?**


### Local AI Chat Apps

Options:
- [Open WebUI](https://openwebui.com/) ([GitHub](https://github.com/open-webui/open-webui)): Open WebUI provides a rich web interface for prototyping AI applications using the most popular generative AI design patterns (prompt engineering, RAG, tool calling, etc.). It is build to work seamlessly with `ollama` and take advantage of the models you have available locally. OpenWebUI is designed to either be hosted or local, and runs in your browser.
- [AnythingLLM](https://anythingllm.com/)([AnythingLLM]([https://anythingllm.com/](https://github.com/Mintplex-Labs/anything-llm)): AnythingLLM creates a ChatGPT-style UI that lives locally on your machine. It can be configured to connect to both locally hosted models like `ollama`, or to connect to a hosted model service. AnythingLLM is designed to be a personalized local GUI and does not have a web interface.

**Why AnythingLLM?**
* For your second brain, having a chat interface that lives on your laptop is critical.

### Retrieval-Augmented Generation (RAG)

Learn about [Retrieval-Augmented Generation (RAG)](https://towardsdatascience.com/local-rag-from-scratch-3afc6d3dea08).

Options:
- Built-in vector stores in [OpenWebUI]() and [AnythingLLM](https://docs.anythingllm.com/agent/usage#what-is-rag-search-and-how-to-use-it)
    - [ragnardoc](): Allows the user to watch a particular folder on their local machine and constantly update an OpenWebUI or AnythingLLM database.
- [LangChain](https://www.langchain.com/):
- [LlamaIndex.ai](https://www.llamaindex.ai/):

**Why LlamaIndex?**

### Agents

Options:
- [Autogen2](): A framework for developing agents


The agents themselves are developed using Kelly Abuelsaad's [agents + RAG framework](https://developer.ibm.com/tutorials/awb-build-agentic-rag-system-granite/), using the [granite-retrieval-agent](https://github.com/ibm-granite-community/granite-retrieval-agent).

**Why Autogen?**
* 

> [!NOTE]
> Especially when using local models, agent design is critical. Smaller local models are more impacted by small differences in prompting. Using agents and tools designed to work with your specific model will lead to the highest success.

### Tool-calling

Options:
- [LangChain](): Allows tool-calling directly from code

**Why LangChain?**
* 

## References

This project is a fork of `lm-desk`. Thanks to Gabe Goodhart for the install scripts, and Kelly Abuelsaad for the agent work.

## Learning and Tutorials

