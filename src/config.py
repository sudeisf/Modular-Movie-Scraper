# src/config.py
from pathlib import Path
import os

# Go UP one level from 'src' to reach the project root
BASE_DIR = Path(__file__).resolve().parent.parent 

DATA_DIR = BASE_DIR / 'data'
POSTER_DIR = DATA_DIR / 'posters'
LOGS_DIR = BASE_DIR / 'logs'

# Ensure these exist
for folder in [DATA_DIR, POSTER_DIR, LOGS_DIR]:
    os.makedirs(folder, exist_ok=True)

IMDB_URL = "https://www.imdb.com/chart/top/"
TIMEOUT = 20
SCROLL_PAUSE = 2.5

CSV_OUTPUT = DATA_DIR / 'imdb_top_250.csv'
LOG_FILE = LOGS_DIR / 'scraping.log'