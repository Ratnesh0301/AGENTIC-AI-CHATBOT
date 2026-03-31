# LangGraph Agentic AI Chatbot

Welcome to the **LangGraph Agentic AI Chatbot** project! This is an interactive Streamlit-based web application that leverages LangGraph, LangChain, and state-of-the-art Large Language Models (LLMs) to provide an advanced, agentic conversational AI experience.

## ✨ Features

- **Multi-Model Support**: Currently integrates robust large language models natively via the Groq API (e.g., `qwen/qwen3-32b`, `openai/gpt-oss-120b`).
- **Flexible Use Cases**: Choose from an array of pre-configured agentic workflows:
  - Basic Chatbot
  - Chatbot with Tools
  - AI News
  - Blog Generator
- **Interactive UI**: Clean, feature-rich interface powered by Streamlit, complete with real-time feedback and dynamic configurations.
- **Agentic Capabilities**: Built on LangGraph, making it easy to model cyclic graphs for complex AI reasoning and tool-use tasks.

## 🛠️ Technology Stack

- **[LangGraph](https://python.langchain.com/docs/langgraph/)**: For building stateful, multi-actor applications with LLMs.
- **[LangChain](https://python.langchain.com/)**: As the core framework for developing LLM-powered operations.
- **[Streamlit](https://streamlit.io/)**: For the frontend user interface.
- **[Groq API](https://groq.com/)**: Fast, efficient inference for supported LLMs.
- **[Tavily](https://tavily.com/) & FAISS**: Tools and integrations spanning search, vector stores (`faiss-cpu`), and multi-provider endpoints.

## 🚀 Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites

- Python 3.9+
- A valid [Groq API Key](https://console.groq.com/keys) (can be provided directly in the UI).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ratnesh0301/AGENTIC-AI-CHATBOT.git
   cd "AGENTIC AI CHATBOT"
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Change directory to the `src` folder:
   ```bash
   cd src
   ```

2. Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Open your browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

## ⚙️ Configuration

The UI layout, model choices, and use case options are driven by a central configuration file located at:

```
src/langgraphagenticai/ui/uiconfig.ini
```

You can modify this file to change the default page title, add new models or LLM providers, and update the list of supported use cases.

## 📂 Project Structure

```
AGENTIC AI CHATBOT/
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
└── src/                     # Source Code
    ├── app.py               # Main Streamlit Application Entrypoint
    └── langgraphagenticai/  # Core application package
        ├── graph/           # LangGraph state graph definitions
        ├── llms/            # LLM initialization and configs
        ├── nodes/           # LangGraph node functions
        ├── state/           # State schemas for the graphs
        ├── tools/           # Custom AI tools (e.g., Search, API tools)
        ├── ui/              # Streamlit UI layouts and components
        └── main.py          # Application loader
```

## 🤝 Contributing

Contributions to enhance the chatbot architecture or add new tools and use cases are welcome! Please feel free to open a Pull Request or create an Issue.
