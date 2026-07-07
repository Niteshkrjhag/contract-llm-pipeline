import re

def clean_text(raw_text: str) -> str:
    """
    Cleans the raw contract text by removing extra whitespaces,
    newlines, and unprintable characters.
    """
    if not raw_text:
        return ""
        
    # Replace multiple newlines with a single newline
    text = re.sub(r'\\n+', '\\n', raw_text)
    
    # Replace multiple spaces with a single space
    text = re.sub(r' +', ' ', text)
    
    # Remove leading and trailing whitespaces
    text = text.strip()
    
    # Optionally, remove special unprintable characters if needed
    # text = re.sub(r'[^\\x00-\\x7F]+', ' ', text)
    
    return text
