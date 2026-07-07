import json
from src.utils.logger import get_logger

logger = get_logger(__name__)

def extract_text_from_cuadv1(filepath: str) -> dict:
    """
    Extracts text and metadata from the CUADv1.json file.
    Returns a dictionary mapping document titles to their text content.
    """
    documents = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if 'data' in data:
            for item in data['data']:
                title = item.get('title', 'Unknown_Title')
                paragraphs = item.get('paragraphs', [])
                
                # Combine all context from paragraphs
                doc_text = ""
                for p in paragraphs:
                    context = p.get('context', '')
                    if context:
                        doc_text += context + "\\n\\n"
                        
                documents[title] = doc_text
        logger.info(f"Successfully loaded {len(documents)} documents from {filepath}")
    except Exception as e:
        logger.error(f"Error loading JSON from {filepath}: {e}")
        
    return documents
