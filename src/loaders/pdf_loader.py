import pdfplumber
from src.utils.logger import get_logger

logger = get_logger(__name__)

def extract_text_from_pdf(filepath: str) -> str:
    """
    Extracts text from a given PDF file.
    """
    text = ""
    try:
        with pdfplumber.open(filepath) as pdf:
            for page_num, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\\n"
        logger.info(f"Successfully extracted text from {filepath}")
    except Exception as e:
        logger.error(f"Error extracting text from {filepath}: {e}")
        
    return text
