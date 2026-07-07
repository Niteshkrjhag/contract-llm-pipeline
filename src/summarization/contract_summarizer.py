from typing import List
from src.prompts.summary_prompt import CONTRACT_SUMMARY_PROMPT
from src.llm.llm_client import generate
from src.utils.logger import get_logger

logger = get_logger(__name__)

def generate_summary(contract_text_or_chunks: str | List[str]) -> str:
    """
    Generates a summary of the contract text.
    If a list of chunks is provided, it combines them up to a certain limit
    to fit within the LLM context window.
    """
    if isinstance(contract_text_or_chunks, list):
        # Naively take the first few chunks to avoid exceeding context limits
        # For a more robust solution, we'd use map-reduce or refine summarization
        contract_text = "\\n\\n".join(contract_text_or_chunks[:5]) 
    else:
        # If it's a single string, we just take the first 10,000 chars roughly
        contract_text = contract_text_or_chunks[:10000]
        
    prompt = CONTRACT_SUMMARY_PROMPT.format(contract_text=contract_text)
    
    logger.info("Generating contract summary...")
    summary = generate(prompt)
    return summary
