from typing import List
from src.prompts.clause_prompts import CLAUSE_EXTRACTION_PROMPT
from src.llm.llm_client import generate
from src.utils.logger import get_logger

logger = get_logger(__name__)

def extract_clause(clause_type: str, relevant_chunks: List[str]) -> str:
    """
    Extracts a specific clause type from relevant chunks using the LLM.
    """
    if not relevant_chunks:
        logger.warning(f"No relevant chunks provided for {clause_type} extraction.")
        return "Clause not found."
        
    contract_text = "\\n\\n".join(relevant_chunks)
    prompt = CLAUSE_EXTRACTION_PROMPT.format(
        clause_type=clause_type,
        contract_text=contract_text
    )
    
    logger.info(f"Extracting {clause_type} clause...")
    extracted_text = generate(prompt)
    return extracted_text
