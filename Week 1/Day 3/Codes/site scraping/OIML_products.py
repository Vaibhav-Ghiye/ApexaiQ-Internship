from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager

class TroemnerScraper:
    """
    A web scraper to extract product data (name, model, description, URL, price) 
    from Troemner's OIML Calibration Weight Sets page.

    Features:
    - Handles lazy loading (infinite scrolling) to load all products
    - Extracts key details for each product
    - Saves data into a CSV file
    """

    def __init__(self, url):
        """
        Initialize the scraper with a target URL.

        Args:
            url (str): The webpage URL to scrape products from.
        """
        self.url = url
        self.driver = None
        self.products = []

    def initialize_driver(self):
        """
        Initialize the Chrome WebDriver in headless mode.
        Uses `webdriver_manager` to automatically fetch ChromeDriver.
        """
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")  # Run Chrome in new headless mode
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def load_page(self):
        """
        Open the given URL and handle lazy loading (infinite scroll).

        The function scrolls down until no new products are loaded.
        """
        self.driver.get(self.url)
        time.sleep(3)  # wait for initial page load

        last_height = self.driver.execute_script("return document.body.scrollHeight")
        
        while True:
            # Scroll to the bottom of the page
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)  # allow new products to load
            
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            
            # If page height does not change, all products are loaded
            if new_height == last_height:
                break
            last_height = new_height

    def extract_data(self):
        """
        Extract product details from the loaded page.

        Captures:
        - Vendor name (static: 'troemner')
        - Product Name
        - Model Number (from product row ID)
        - Description
        - Product URL
        - Price
        """
        vendor = "troemner"
        products = self.driver.find_elements(By.XPATH, "//*[starts-with(@id, 'product-list-row-')]")
    
        for prod in products:
            model = prod.get_attribute("id").replace("product-list-row-", "")
    
            # Product name and URL
            try:
                product_anchor = prod.find_element(By.CSS_SELECTOR, f"a#sendClickEventToGTM_{model}")
                productName = product_anchor.text.strip()
                productURL = product_anchor.get_attribute("href")
            except:
                productName = "N/A"
                productURL = self.url
    
            # Description
            try:
                description = prod.find_element(By.CSS_SELECTOR, "div.description.product-description").text.strip()
            except:
                description = "N/A"
    
            # Price
            try:
                price = prod.find_element(By.CSS_SELECTOR, "span.priceValue").text.strip()
            except:
                price = "N/A"
    
            self.products.append([vendor, productName, model, description, productURL, price])

    def save_to_csv(self, file_name):
        """
        Save extracted product data into a CSV file.

        Args:
            file_name (str): Name of the output CSV file.
        """
        df = pd.DataFrame(self.products, columns=["vendor", "productName", "model", "description", "productURL", "cost"])
        df.to_csv(file_name, index=False, encoding="utf-8")
        print(f"✅ Data saved to {file_name}")
        print(f"📦 Total Products Scraped: {len(df)}")
        print(df.head())

    def close_driver(self):
        """
        Close the Selenium WebDriver.
        """
        if self.driver:
            self.driver.quit()

    def run_scraper(self, file_name):
        """
        Full scraper pipeline:
        - Initialize driver
        - Load page with lazy loading
        - Extract product data
        - Save results into CSV
        - Close driver
        """
        self.initialize_driver()
        self.load_page()
        self.extract_data()
        self.save_to_csv(file_name)
        self.close_driver()


# Run the scraper
scraper = TroemnerScraper("https://www.troemner.com/Calibration-Weights/Balance-Calibration-Weights/OIML-Calibration-Weight-Sets/c/3944")
scraper.run_scraper("troemner_products.csv")
