from sentence_transformers import SentenceTransformer
from typing import List
from src.utils.logger import get_logger

logger = get_logger(__name__)

# Initialize the model once
MODEL_NAME = "all-MiniLM-L6-v2"
try:
    logger.info(f"Loading SentenceTransformer model: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)
except Exception as e:
    logger.error(f"Failed to load SentenceTransformer model: {e}")
    model = None

def create_embeddings(chunks: List[str]) -> List[List[float]]:
    """
    Generates embeddings for a list of text chunks using sentence-transformers.
    """
    if not model:
        logger.error("Embedding model is not loaded. Cannot generate embeddings.")
        return []
        
    try:
        logger.info(f"Generating embeddings for {len(chunks)} chunks...")
        embeddings = model.encode(chunks, show_progress_bar=False)
        return embeddings.tolist()
    except Exception as e:
        logger.error(f"Error generating embeddings: {e}")
        return []
