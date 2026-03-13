import pandas as pd
import logging
from src.config import LOG_FILE

# Setup professional logging
logging.basicConfig(
    filename=str(LOG_FILE),  # Ensure path is string
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
    
def download_poster(poster_elem, clean_title, save_dir):
    """Downloads the poster image and saves it locally."""
    import requests
    from pathlib import Path
    
    try:
        response = requests.get(poster_elem, stream=True)
        response.raise_for_status()
        
        # Create a safe filename
        safe_title = "".join(c for c in clean_title if c.isalnum() or c in (' ', '_')).rstrip()
        filename = f"{safe_title}.jpg"
        save_path = Path(save_dir) / filename
        
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        
        logging.info(f"Downloaded poster for '{clean_title}'")
        return str(save_path)
    
    except Exception as e:
        logging.error(f"Failed to download poster for '{clean_title}': {e}")
        return None