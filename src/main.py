import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Internal Project Imports
from src.driver_setup import WebDriverFactory
from src.config import IMDB_URL, TIMEOUT, SCROLL_PAUSE, CSV_OUTPUT, POSTER_DIR
from src.utils import download_poster, clean_movie_data, save_to_csv

def scrape_IMDB():
    """
    Main execution function to scrape the IMDb Top 250 list.
    Handles stealth browser initialization, smart scrolling, and data extraction.
    """
    driver = WebDriverFactory.get_driver(headless=False)
    wait = WebDriverWait(driver, TIMEOUT)
    movie_results = []
    
    try:
        logging.info(f"Navigating to IMDb Top 250 page: {IMDB_URL}")
        driver.get(IMDB_URL)
        
        # SMART SCROLLING (Handle Lazy Loading) ---
        last_height = driver.execute_script("return document.body.scrollHeight")
        
        print("Scrolling to load all movies...")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE)
            
            new_height = driver.execute_script("return document.body.scrollHeight") 
            if new_height == last_height:
                break
            last_height = new_height
        
        # --- 2. ELEMENT IDENTIFICATION ---
        # Wait until the list items are present in the DOM
        movies = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
            )
        )
        
        print(f"Detected {len(movies)} movies. Starting extraction...")
        
        # --- 3. DATA EXTRACTION LOOP ---
        for index, movie in enumerate(movies, start=1):
            try:
                # Extract Title
                title_elem = movie.find_element(By.CSS_SELECTOR, "h3.ipc-title__text")
                clean_title = clean_movie_data(title_elem.text)
                
                # Extract Rating (Numeric part only)
                rating_text = movie.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--imdb").text
                rating = rating_text.split()[0] if rating_text else "N/A"
                
                # Extract Poster URL
                poster_url = movie.find_element(By.CSS_SELECTOR, "img.ipc-image").get_attribute("src")
                
                # Download poster image locally
                local_path = download_poster(poster_url, clean_title, POSTER_DIR)
                
                # Store results
                movie_results.append({
                    "rank": index,
                    "title": clean_title,
                    "rating": rating,
                    "poster_path": local_path
                })
                
                if index % 50 == 0:
                    print(f"Progress: {index}/250 movies processed.")
                    logging.info(f"Successfully processed {index} movies.")
                    
            except Exception as e:
                logging.warning(f"Failed to extract movie at rank {index}: {e}")
                continue
        
        # --- 4. EXPORT DATA ---
        if movie_results:
            save_to_csv(movie_results, CSV_OUTPUT)
            print(f"\nSUCCESS: Scraped {len(movie_results)} movies.")
            print(f"Data: {CSV_OUTPUT}")
            print(f"Posters: {POSTER_DIR}")
        else:
            logging.error("No data collected during the scrape.")

    except Exception as e:
        logging.error(f"CRITICAL SCRAPER ERROR: {e}")
        print(f"An error occurred. Check the logs for details.")

    finally:
        driver.quit()
        logging.info("Browser session closed.")
        
if __name__ == "__main__":
    scrape_IMDB()