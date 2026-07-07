# CONTRACT_SUMMARY_PROMPT = """
# You are an expert legal assistant. Provide a concise summary of the following contract text.
# The summary should be between 100 and 150 words. Focus on the main purpose of the contract, the key parties involved, and the most critical obligations or terms.

# Contract Text:
# {contract_text}

# Summary:
# """

CONTRACT_SUMMARY_PROMPT = """
Act as an expert legal assistant. Summarize the provided contract in a concise 100 to 150 words.
Strictly structure your summary to highlight:
1. Purpose: The core objective of the agreement.
2. Obligations: The key duties required of each party.
3. Risks & Penalties: Any notable liabilities, financial risks, or penalties for breach.
Contract Text: {contract_text}
"""
