import os
import random
import shutil
from pathlib import Path

def select_random_contracts(source_dir: str, dest_dir: str, num_samples: int = 50):
    """
    Recursively finds all PDFs in source_dir, randomly selects num_samples,
    and copies them to dest_dir.
    """
    source_path = Path(source_dir)
    dest_path = Path(dest_dir)
    
    # Create destination directory if it doesn't exist
    dest_path.mkdir(parents=True, exist_ok=True)
    
    # Recursively find all PDF files
    all_pdfs = list(source_path.rglob("*.pdf"))
    print(f"Found {len(all_pdfs)} PDFs in {source_dir}")
    
    if len(all_pdfs) == 0:
        print("No PDFs found!")
        return
        
    # Select randomly
    samples_to_select = min(num_samples, len(all_pdfs))
    selected_pdfs = random.sample(all_pdfs, samples_to_select)
    
    print(f"Selecting {samples_to_select} PDFs randomly...")
    
    # Copy selected PDFs
    for idx, pdf_path in enumerate(selected_pdfs):
        dest_file = dest_path / pdf_path.name
        
        # In case there are files with the same name, we can append a number
        if dest_file.exists():
            dest_file = dest_path / f"{pdf_path.stem}_{idx}{pdf_path.suffix}"
            
        shutil.copy2(pdf_path, dest_file)
        
    print(f"Successfully copied {samples_to_select} PDFs to {dest_dir}")

if __name__ == "__main__":
    SOURCE = "data/raw_contracts/full_contract_pdf"
    DEST = "data/selected_contracts"
    select_random_contracts(SOURCE, DEST, 50)
