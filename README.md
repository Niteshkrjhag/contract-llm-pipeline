# Contract LLM Pipeline

An end-to-end pipeline for reading legal contracts, extracting specific clauses (Termination, Confidentiality, Liability), and summarizing the contracts using a Large Language Model (LLM).

## Features

- **Multi-format Support**: Extracts text from PDF contracts and JSON datasets (like CUADv1).
- **Text Preprocessing**: Cleans and chunks the text using LangChain's `RecursiveCharacterTextSplitter`.
- **Local Embeddings**: Generates embeddings using `sentence-transformers/all-MiniLM-L6-v2` locally to avoid embedding costs.
- **Vector Search**: Uses `FAISS` for fast retrieval of relevant chunks.
- **LLM Integration**: Interacts with the OpenAI API for clause extraction and summarization.
- **Export**: Outputs extracted clauses and summaries to CSV and JSON formats.

## Architecture

The project is structured modularly emphasizing readability and ease of testing.

```text
contract-llm-pipeline/
├── data/
│   └── raw_contracts/       # Place your PDFs or CUADv1.json here
├── outputs/                 # CSV and JSON results will be saved here
├── src/
│   ├── loaders/             # pdf_loader.py, json_loader.py
│   ├── preprocessing/       # text_cleaner.py, text_chunker.py
│   ├── embeddings/          # embedding_generator.py, vector_store.py
│   ├── extraction/          # clause_extractor.py
│   ├── summarization/       # contract_summarizer.py
│   ├── prompts/             # clause_prompts.py, summary_prompt.py
│   └── utils/               # logger.py, file_manager.py
├── main.py                  # Entry point for the pipeline
├── requirements.txt         # Project dependencies
└── .env.example             # Template for API keys
```

## Setup Instructions

1. **Clone the repository** (if applicable) and navigate to the project directory:
   ```bash
   cd contract-llm-pipeline
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Copy the `.env.example` file to `.env` and add your OpenAI API key:
   ```bash
   cp .env.example .env
   ```
   Open `.env` and set `OPENAI_API_KEY=your_actual_key_here`.

5. **Add Data**:
   Place your PDF contracts or the `CUADv1.json` file inside the `data/raw_contracts/` directory.

6. **Run the Pipeline**:
   ```bash
   python main.py
   ```

## Output

The extracted data will be saved in the `outputs/` directory as:
- `contract_results.csv`
- `contract_results.json`

## Future Improvements
- Add support for other open-source LLMs via Ollama or HuggingFace.
- Implement more robust summary chunking (Map-Reduce strategy).
- Add unit tests.
