import os
from src.pipeline import run_pipeline
from src.utils.logger import get_logger
from dotenv import load_dotenv

load_dotenv()
logger = get_logger(__name__)

if __name__ == "__main__":
    try:
        raw_contracts_dir = os.getenv("RAW_CONTRACTS_DIR", "data/raw_contracts")
        output_dir = os.getenv("OUTPUT_DIR", "outputs")
        
        if not os.path.exists(raw_contracts_dir):
            logger.error(f"Data directory {raw_contracts_dir} does not exist.")
            exit(1)
            
        run_pipeline(raw_contracts_dir, output_dir)
        
    except Exception as e:
        logger.error(f"Pipeline failed with error: {e}")
