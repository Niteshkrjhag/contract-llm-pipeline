import faiss
import numpy as np
from typing import List, Tuple
from src.utils.logger import get_logger
from src.embeddings.embedding_generator import model

logger = get_logger(__name__)

def build_index(embeddings: List[List[float]]) -> faiss.IndexFlatL2:
    """
    Builds a FAISS index from a list of embeddings.
    """
    if not embeddings:
        logger.warning("No embeddings provided to build FAISS index.")
        return None
        
    try:
        embedding_matrix = np.array(embeddings).astype('float32')
        dimension = embedding_matrix.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(embedding_matrix)
        logger.info(f"FAISS index built successfully with {index.ntotal} vectors.")
        return index
    except Exception as e:
        logger.error(f"Error building FAISS index: {e}")
        return None

def retrieve_chunks(query: str, index: faiss.IndexFlatL2, chunks: List[str], top_k: int = 5) -> List[str]:
    """
    Retrieves the most relevant chunks for a given query.
    """
    if index is None or not chunks:
        logger.warning("Index or chunks not available for retrieval.")
        return []
        
    if not model:
        logger.error("Embedding model not loaded for retrieval.")
        return []
        
    try:
        # Generate embedding for the query
        query_embedding = model.encode([query]).astype('float32')
        
        # Search the index
        distances, indices = index.search(query_embedding, top_k)
        
        # Retrieve chunks based on indices
        relevant_chunks = []
        for idx in indices[0]:
            if 0 <= idx < len(chunks):
                relevant_chunks.append(chunks[idx])
                
        return relevant_chunks
    except Exception as e:
        logger.error(f"Error retrieving chunks for query '{query}': {e}")
        return []
