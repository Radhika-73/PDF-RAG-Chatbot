# 🤖 PDF RAG Chatbot

A local Retrieval-Augmented Generation (RAG) chatbot built with **Streamlit**, **LangChain**, **ChromaDB**, and **Ollama**. This application allows you to ask questions and receive accurate answers grounded strictly in the content of your indexed PDF documents.

## ✨ Features
* **Local & Private:** Runs completely locally using Ollama and local HuggingFace embeddings—no external API keys required.
* **Context-Aware Answers:** Uses ChromaDB vector search to retrieve the top 3 most relevant document chunks before generating a response.
* **Source Transparency:** Includes an expandable "Retrieved Context" section in the UI so you can verify the exact text used to generate each answer.

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io)
* **Framework:** [LangChain](https://langchain.com) (`langchain-huggingface`, `langchain-community`, `langchain-ollama`)
* **Vector Database:** [ChromaDB](https://trychroma.com)
* **Embeddings:** `BAAI/bge-small-en-v1.5` (via HuggingFace)
* **LLM:** `gemma3` (via [Ollama](https://ollama.com))

## 📋 Prerequisites

1. **Python 3.9+** installed on your machine.
2. **Ollama** installed and running locally. Download it from [ollama.com](https://ollama.com).
3. **Pull the Gemma 3 model** in your terminal before running the app:
   ```bash
   ollama pull gemma3
   ```
4. **Vector Database:** Ensure your PDF documents have already been processed and stored in the local `chroma_db/` directory.

## 🚀 Installation & Setup

1. **Clone the repository** (or navigate to your project folder):
   ```bash
   cd RAG
   ```

2. **Create and activate a virtual environment:**
   * **Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   * **macOS/Linux:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If you don't have a `requirements.txt` yet, install them directly:)*
   ```bash
   pip install streamlit langchain langchain-huggingface langchain-community langchain-ollama chromadb sentence-transformers
   ```

## 💻 Usage

1. Make sure the Ollama background service is running.
2. Start the Streamlit web application:
   ```bash
   streamlit run app.py
   ```
3. Open your browser to the local URL shown in the terminal (usually `http://localhost:8501`).
4. Type your question into the input box and click **Ask**.

## 📁 Project Structure

```text
RAG/
├── app.py              # Main Streamlit chatbot application
├── chroma_db/          # Persisted Chroma vector database (generated from your PDFs)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```
