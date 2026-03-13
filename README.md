# Modular Movie Scraper

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.4.0-green.svg)
![Pandas](https://img.shields.io/badge/Pandas-3.0.1-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A Selenium-based web scraper that extracts the top 250 movies from IMDb, including titles, ratings, and poster images.

## Features

- Scrapes IMDb Top 250 movie list
- Extracts movie titles, ratings, and poster URLs
- Downloads poster images locally
- Saves data to CSV format
- Configurable via `config.py`
- Professional logging system

## Project Structure

```
Modular-Movie-Scraper/
├── src/
│   ├── config.py        # Configuration settings
│   ├── driver_setup.py  # Selenium WebDriver setup
│   ├── main.py          # Main scraper logic
│   ├── utils.py         # Utility functions
│   ├── data/
│   │   ├── posters/     # Downloaded poster images
│   │   └── imdb_top_250.csv  # Output CSV file
│   └── logs/
│       └── scraping.log # Application logs
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Requirements

- Python 3.8+
- Google Chrome browser
- ChromeDriver (automatically managed by webdriver-manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Modular-Movie-Scraper
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the scraper:
```bash
python -m src.main
```

The scraper will:
1. Open Chrome browser and navigate to IMDb Top 250
2. Scroll through the page to load all movies
3. Extract title, rating, and poster for each movie
4. Download posters to `src/data/posters/`
5. Save data to `src/data/imdb_top_250.csv`
6. Log all activity to `src/logs/scraping.log`

## Configuration

Edit `src/config.py` to customize:

| Setting | Description | Default |
|---------|-------------|---------|
| `TIMEOUT` | WebDriver wait timeout (seconds) | 20 |
| `SCROLL_PAUSE` | Pause between scrolls (seconds) | 2.5 |
| `IMDB_URL` | Target IMDb URL | IMDb Top 250 |

## Output

- **CSV File**: `src/data/imdb_top_250.csv` containing:
  - rank (1-250)
  - title (movie name)
  - rating (IMDb rating)
  - poster_path (local file path)

- **Poster Images**: `src/data/posters/<movie_title>.jpg`

- **Logs**: `src/logs/scraping.log`

## Troubleshooting

### Log file not found
Logs are saved to `src/logs/scraping.log` (not `logs/` at root level).

### ChromeDriver issues
The project uses `webdriver-manager` to automatically download and manage ChromeDriver. Ensure you have Google Chrome installed.

### Element not found errors
- Increase `TIMEOUT` in `config.py`
- Check your internet connection
- IMDb may have changed their HTML structure (selector updates may be needed)

## License

MIT License
