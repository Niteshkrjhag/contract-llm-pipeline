CLAUSE_EXTRACTION_PROMPT = """
You are an expert legal assistant. Your task is to extract the {clause_type} clause from the provided contract text.

If the clause is not present in the text, respond with "Clause not found."

Contract Text:
{contract_text}

Extracted {clause_type} Clause:
"""
