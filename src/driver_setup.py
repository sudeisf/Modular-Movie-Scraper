from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverFactory:
    
    @staticmethod
    def get_driver(headless = False):
        chrome_options  =  Options()
        
        if headless:
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--disable-gpu")
        
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--window-size=1920,1080")
            
        #Stealth & Anti-Bot Measures
        chrome_options.experimental_options("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Initialize with WebDriver Manager (Automates driver updates)
        service = Service(ChromeDriverManager().install())  
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        
        # Remove the 'webdriver' flag from the browser's JavaScript
        # This is a major detection point for sites like IMDb
        driver.execute_cdp_cmd(
            "page.addScriptToEvaluateOnNewDocument",
            {
                "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                        get: () => undefined
                    });
                """
            }
        )
        
        return driver
        
        