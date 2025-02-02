# Building Your (Local) LLM Second Brain

## Getting Started

### Quick Start

Running the following command will install all of the core components:

* Ollama
* Granite
* OpenWebUI
* VSCode
* Continue.dev

Since OpenWebUI mainly allows agent and tool configuration through the GUI, that work will be done there.

```sh
bash -c "$(curl -fsSL 'https://raw.githubusercontent.com/obuzek/llm-second-brain/main/get-lm-desk.sh')"
```

After this you can jump to Step 6 - Adding Agents.

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

### Model - [`granite3.1-dense:8b`](https://registry.ollama.com/library/granite3.1-dense)

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

* Code chat in your IDE
* Code completions
* Easy add-selection-to-context

### Local AI Chat Apps

Options:
- [Open WebUI](https://openwebui.com/) ([GitHub](https://github.com/open-webui/open-webui)): Open WebUI provides a rich web interface for prototyping AI applications using the most popular generative AI design patterns (prompt engineering, RAG, tool calling, etc.). It is build to work seamlessly with `ollama` and take advantage of the models you have available locally. OpenWebUI is designed to either be hosted or local, and runs in your browser.
- [AnythingLLM](https://anythingllm.com/)([AnythingLLM]([https://anythingllm.com/](https://github.com/Mintplex-Labs/anything-llm)): AnythingLLM creates a ChatGPT-style UI that lives locally on your machine. It can be configured to connect to both locally hosted models like `ollama`, or to connect to a hosted model service. AnythingLLM is designed to be a personalized local GUI and does not have a web interface.

**Why OpenWebUI?**
* For your second brain, having a chat interface that lives on your laptop is critical.
* Multi-user, enterprise-adaptable
* Pipeline extensions allow more complex workflows

### Retrieval-Augmented Generation (RAG)

Learn about [Retrieval-Augmented Generation (RAG)](https://towardsdatascience.com/local-rag-from-scratch-3afc6d3dea08).

Options:
- Built-in collections interfaces in [OpenWebUI](https://docs.openwebui.com/) and [AnythingLLM](https://docs.anythingllm.com/agent/usage#what-is-rag-search-and-how-to-use-it)
    - both LangChain-based! with limitations based on particular 
- [LangChain](https://www.langchain.com/):
- [LlamaIndex.ai](https://www.llamaindex.ai/):

**Why use built-in collections?**

* All the flexibility of LangChain in an easily accessible package

### Agents

Options:
- [Autogen2](https://github.com/ag2ai/ag2): A framework for developing agents

The agents themselves are developed using @kellyaa's [agents + RAG framework](https://developer.ibm.com/tutorials/awb-build-agentic-rag-system-granite/), using the [granite-retrieval-agent](https://github.com/ibm-granite-community/granite-retrieval-agent).

**Why Autogen?**
* Ease of building multi-agent solutions, particularly useful when working with small models
* Better agent error-handling

## Full Installation Instructions

#### **1. Installing Ollama**

See [Ollama's README](https://github.com/ollama/ollama) for full installation instructions. However it is as simple as:

On OSX:

```
brew install ollama
```

On Linux:

```
curl -fsSL https://ollama.com/install.sh | sh
```

To run:

```
ollama serve
```
Now you are up and running with Ollama and Granite

#### **2. Installing Granite 3.1**

```
ollama pull granite3.1-dense:8b
```

#### **3. Installing VSCode and Continue**

If you don't already have VSCode, you can install it through Homebrew for the purposes of this experiment:
```
brew install --cask visual-studio-code
```

Open VSCode.

Open the extensions panel (shortcut: Ctrl+shift+X).

Search for: "Continue"

Click `Install` to add the extension for [Continue.dev](https://www.continue.dev/).

#### **4. Installing OpenWebUI**

```
pip install open-webui
open-webui serve
```

Visit your local OpenWebUI instance: [https://127.0.0.1:8080](https://127.0.0.1:8080)

#### **5. Adding knowledge**

Click the hamburger menu in the top left corner.

Select "Workspace" from the menu.

On the right, click "Knowledge" in the headers.

Click the "+" sign to the right of the search box.

You should be on the page entitled "Create a Knowledge Base".

Enter a name and description for your collection:

Name: `My Notes`
Description: `Access to my notes`

This metadata may be made available to the model, so ensure it has some relevance.

Click "Create Knowledge".

You are now viewing your collection.

To add something new, click the "+" sign to the right of the search bar.

Select "Sync Directory" for ongoing access to the knowledge base.

Select "Confirm" when it asks you if you want to reset your (currently empty) knowledge base.

Choose a folder of documents - e.g. PDF, docx, Markdown, plaintext.

Click "Select".

Your collection should now be made available.

#### **6. Adding search agent**

> [!NOTE]
> Especially when using local models, agent design is critical. Smaller local models are more impacted by small differences in prompting. Using agents and tools designed to work with your specific LLM will lead to the highest success.

We're going to use @kellyaa's `granite-retrieval-agent` to give our second brain the ability to respond to task requests by searching the web for information.

Follow the README here: [./granite-retrieval-agent/README.md](./granite-retrieval-agent/README.md)

Don't forget to flip the toggle switch on in the Admin Panel -> Functions section.

Keep track of the name of your new Function (perhaps "RAG Agent"), since you'll need it in the next step.

#### **7. Adding the todo list tool**

Click the hamburger menu in the top left corner.

Click "Workspace" from the dropdown.

Click "Tools" in the top headers.

Click the "+" sign to the right of the search bar.

Paste the contents of [./add-task-tool.py](./add-task-tool.py) in the main code box.

This is a simple script - it will make a folder called `./tasks` wherever your OpenWebUI instance is running from, and put tasks in the folder by creating a file `{title}.md` for each one, with the contents being the `{description}`.

You can modify this as you see fit to dump tasks to your preferred task manager.

Make the tool name "Add Task".

Make the tool description "Adds a task to an external todo list manager."

Click "Save" at the bottom.

Your tool is now ready to use!

Let's make it available to our LLM.

#### **8. Optimizing model to use todo list tool**

Since the model has been fine-tuned on data indicating that it can't access outside resources, we need to add a system prompt that allows the model to better respond to questions involving our new todo list tool.

Click the hamburger menu in the top left corner.

Click "Workspace" from the dropdown.

Click "Models" from the top headers.

Click the "+" sign to the right of the search bar.

In "Model Name", type "LLM Second Brain".

In "Description", write "Second brain interface to access notes and add TODO lists."

In "Base Model", select either "granite3.1-dense:8b" - or, if you want to experiment with using all of the "second brain" parts together, select "RAG Agent" (your agent from the previous step). Note that the prompting may come into conflict.

In "System Prompt", put the contents of the [./second-brain-prompt.txt](./second-brain-prompt.txt) file.

The "second brain" system prompt is designed to summarize your notes, break down tasks, or store tasks in external storage.

Under "Tools", tick the checkbox for "Add Task".

Scroll to the bottom and click "Save & Update".

#### **9. Try it out!**

Go back to the hamburger menu in the top left corner and click "New Chat".

At the top of the page, to the right of the hamburger menu, you will see a model listed. Click there to select a model.

Select your tool model ("Second Brain") or your agent model ("RAG Agent"), and start prompting it to see its behavior.

Try:

```
#My-Notes
What were my action items from the last project meeting? Can you break them down for me?
```

See how it responds!

## Published At

* FOSDEM '25: Building Your (Local) LLM Second Brain ([talk](https://fosdem.org/2025/schedule/event/fosdem-2025-6542-building-your-local-llm-second-brain/)) ([slides](https://docs.google.com/presentation/d/19zAWdGB1h_2ZkBXXRl0flYa4YRxsV1-RtKJxRtteksg/edit?usp=sharing))

## References

This project is a fork of `lm-desk`. Thanks to Gabe Goodhart (@gabe-l-hart) for the install scripts, and Kelly Abuelsaad (@kellyaa) for the agent work.

## Learning and Tutorials

