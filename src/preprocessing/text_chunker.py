from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

def chunk_contract(cleaned_text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> List[str]:
    """
    Splits the cleaned contract text into smaller chunks for processing.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\\n\\n", "\\n", " ", ""]
    )
    
    chunks = text_splitter.split_text(cleaned_text)
    return chunks
