import os
from src.loaders.pdf_loader import extract_text_from_pdf
from src.loaders.json_loader import extract_text_from_cuadv1
from src.preprocessing.text_cleaner import clean_text
from src.preprocessing.text_chunker import chunk_contract
from src.embeddings.embedding_generator import create_embeddings
from src.embeddings.vector_store import build_index, retrieve_chunks
from src.extraction.clause_extractor import extract_clause
from src.summarization.contract_summarizer import generate_summary
from src.utils.logger import get_logger
from src.utils.file_manager import get_all_files, save_csv, save_json

logger = get_logger(__name__)

def process_single_document(title: str, raw_text: str) -> dict:
    """
    Processes a single document text through the entire pipeline.
    """
    logger.info(f"Processing document: {title}")
    
    # 1. Clean Text
    cleaned_text = clean_text(raw_text)
    if not cleaned_text:
        logger.warning(f"No text to process for {title}.")
        return None
        
    # 2. Chunk Text
    chunks = chunk_contract(cleaned_text)
    
    # 3. Create Embeddings & Index
    embeddings = create_embeddings(chunks)
    index = build_index(embeddings)
    
    # 4. Extract Clauses
    queries = {
        "Termination": "What are the rules, notice periods, and conditions for terminating, cancelling, or ending this contract?",
        "Confidentiality": "How is confidential information defined, protected, and shared between the parties?",
        "Liability": "What are the limitations of liability, indemnification, and caps on damages?"
    }
    
    extracted_data = {"Title": title}
    
    for clause_name, search_query in queries.items():
        if index:
            # We use the full sentence 'search_query' to search FAISS mathematically
            relevant_chunks = retrieve_chunks(search_query, index, chunks) 
            # But we still tell the LLM to extract the specific 'clause_name'
            extracted_text = extract_clause(clause_name, relevant_chunks)
        else:
            extracted_text = "Error: Index not built."
            
        extracted_data[f"{clause_name} Clause"] = extracted_text
        
    # 5. Summarize
    summary = generate_summary(chunks)
    extracted_data["Summary"] = summary
    
    return extracted_data

def run_pipeline(data_dir: str, output_dir: str):
    """
    Runs the pipeline for all PDFs and JSONs in the data directory.
    """
    logger.info(f"Starting pipeline. Reading from {data_dir}")
    
    all_results = []
    
    # Process PDFs
    pdf_files = get_all_files(data_dir, extension=".pdf")
    for pdf_file in pdf_files:
        title = os.path.basename(pdf_file)
        raw_text = extract_text_from_pdf(pdf_file)
        result = process_single_document(title, raw_text)
        if result:
            all_results.append(result)
            
    # Process JSON (CUADv1)
    json_files = get_all_files(data_dir, extension=".json")
    for json_file in json_files:
        documents = extract_text_from_cuadv1(json_file)
        for title, text in documents.items():
            result = process_single_document(title, text)
            if result:
                all_results.append(result)
                
    # Save Results
    if all_results:
        csv_path = os.path.join(output_dir, "contract_results.csv")
        json_path = os.path.join(output_dir, "contract_results.json")
        
        fieldnames = ["Title", "Termination Clause", "Confidentiality Clause", "Liability Clause", "Summary"]
        save_csv(all_results, csv_path, fieldnames)
        save_json(all_results, json_path)
        logger.info(f"Pipeline completed successfully. Results saved to {output_dir}")
    else:
        logger.warning("No results to save.")

