---
title: Contract AI Pipeline
emoji: 📜
colorFrom: purple
colorTo: indigo
sdk: docker
pinned: false
---
# 🏛️ Legal Contract Intelligence AI

An end-to-end, locally-hostable AI pipeline that reads legal contracts (PDFs), semantically extracts crucial clauses (Termination, Confidentiality, Liability), and generates structured Executive Summaries using Large Language Models (LLMs).

This project features a **dynamic multi-LLM fallback architecture** and a **stunning Glassmorphic Web UI**.

---

## ✨ Features

- 🧠 **Multi-LLM Fallback Engine**: Never fail a request due to rate limits. The system seamlessly falls back in sequence: **Gemini 2.5 Flash ➡️ OpenAI ➡️ OpenRouter ➡️ Ollama Cloud**.
- 🔍 **RAG & Semantic Search**: Generates local vector embeddings using `sentence-transformers/all-MiniLM-L6-v2` and searches text instantly using `FAISS`.
- 📊 **Intelligent Extraction**: Uses precise prompt engineering to extract Termination, Confidentiality, and Liability clauses contextually.
- 🎨 **Premium Web UI**: Includes a blazing-fast **FastAPI** backend and a beautiful **Vanilla JS/CSS** dashboard with glassmorphism, animated layouts, and markdown rendering to eliminate text fatigue.
- ⚡ **Batch CLI Tooling**: Includes Python scripts to randomly sample massive document pools and run batch processing autonomously.

---

## 🏗️ Architecture & Technology Stack

The project is highly modular, split between a backend AI pipeline and a minimalist frontend.

### Stack
- **Backend**: Python 3.12+, FastAPI, LangChain, FAISS, Sentence-Transformers.
- **Frontend**: Vanilla HTML/CSS/JavaScript, Marked.js (for Markdown rendering).

### Folder Structure
```text
contract-llm-pipeline/
├── app.py                   # FastAPI backend server (Web UI Entrypoint)
├── main.py                  # CLI pipeline entrypoint for batch processing
├── static/                  # Frontend files (index.html, styles.css, script.js)
├── data/
│   └── raw_contracts/       # Place your PDF contracts here
├── outputs/                 # CSV/JSON exports from batch processing
├── src/
│   ├── loaders/             # PDF and JSON extraction logic
│   ├── preprocessing/       # Text cleaning and LangChain chunking
│   ├── embeddings/          # FAISS vector store & local MiniLM embeddings
│   ├── extraction/          # Semantic extraction and LLM calling
│   ├── summarization/       # Document-level summarization logic
│   ├── prompts/             # Engineering templates for specific clauses
│   ├── llm/                 # LLM Client manager and Fallback Routing
│   └── utils/               # Logging and file management
└── requirements.txt         # Project dependencies
```

---

## 🚀 Setup & Installation (For Technical Users)

### 1. Prerequisites
Ensure you have Python 3.10 or higher installed.

### 2. Clone & Install
```bash
# Clone the repository
git clone https://github.com/your-username/contract-llm-pipeline.git
cd contract-llm-pipeline

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration
Copy the template environment file:
```bash
cp .env.example .env
```
Open `.env` and configure your API keys. **You do not need all of them**—the fallback system will use whichever ones are available:
- `GEMINI_API_KEY`
- `OPENAI_API_KEY`
- `OPENROUTER_API_KEY`
- `OLLAMA_API_KEY` (For Ollama Cloud)

Configure the strict fallback order in `.env`:
```env
LLM_FALLBACK_ORDER="Gemini,OpenAI,OpenRouter,Ollama"
```

---

## 💻 Usage Instructions (Semi-Technical / End Users)

You have two ways to interact with the pipeline: via the **Beautiful Web UI** or the **Command Line (Batch)**.

### Option A: The Web Dashboard (Recommended)
This launches a user-friendly interface in your browser where you can simply drag-and-drop PDFs.

1. Start the server:
   ```bash
   uvicorn app:app --port 8000
   ```
2. Open your web browser and navigate to: **http://localhost:8000**
3. Drag and drop any PDF contract into the upload zone.
4. The AI will process the document and return an Executive Summary alongside interactive tabs for deeply analyzing Termination, Confidentiality, and Liability clauses.

### Option B: Batch CLI Processing
If you have a folder of hundreds of contracts and want to extract data into a massive JSON/CSV file.

1. Place all your PDFs into `data/raw_contracts/`.
2. Run the pipeline script:
   ```bash
   python main.py
   ```
3. The results will be saved automatically in the `outputs/` folder as `contract_results.json` and `contract_results.csv`.

---

## 🎯 How it Works Under the Hood

1. **Ingestion**: The system reads the PDF and chunks the text into overlapping segments to retain context.
2. **Embedding**: It converts these chunks into numbers (vectors) locally using a highly efficient HuggingFace model.
3. **Retrieval**: When searching for "Termination", FAISS mathematically finds the chunks of the contract most relevant to ending the agreement.
4. **Generation**: The retrieved chunks are sent to the LLM via the Fallback Engine. If Gemini refuses due to rate-limiting, the system instantly routes the prompt to OpenAI, then OpenRouter, then Ollama Cloud.
5. **Presentation**: The Web UI receives the Markdown response and securely renders it into a split-pane dashboard, using psychological design principles to prevent text-fatigue.
