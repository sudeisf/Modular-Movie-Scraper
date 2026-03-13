import pandas as pd
import logging
from src.config import LOG_FILE

# Setup professional logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
) 

def clean_movie_data(raw_text):
    """
    Cleans titles and ranks. 
    Example: '1. The Shawshank Redemption' -> 'The Shawshank Redemption'
    """
    if '.' in raw_text:
        return raw_text.split('.', 1)[1].strip()
    return raw_text.strip()

def save_to_csv(data_list, output_path):
    """Saves the final list of dicts to CSV using Pandas."""
    df = pd.DataFrame(data_list)
    df.to_csv(output_path, index=False)
    logging.info(f"Saved {len(data_list)} movies to {output_path}")