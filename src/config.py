import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / 'data'
POSTS_DIR = DATA_DIR / 'posters'
LOGS_DIR = BASE_DIR / 'logs'

for folder in [DATA_DIR, POSTS_DIR, LOGS_DIR]:
    os.makedirs(folder, exist_ok=True)

IMDB_URL = "https://www.imdb.com/chart/top/"
TIMEOUT = 20  # How long to wait for elements to load
SCROLL_PAUSE = 2.5  # Time to wait for lazy-loading to trigger

CSV_FILE = DATA_DIR / 'imdb_top_250.csv'
LOGS_FILE = LOGS_DIR / 'scraping.log'