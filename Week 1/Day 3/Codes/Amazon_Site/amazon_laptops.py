# Import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager


class AmazonScraper:
    """
    A scraper class to extract product details (title, price, rating, reviews)
    from Amazon search results and save them to a CSV file.
    """

    def __init__(self, url):
        self.url = url
        self.driver = None
        self.products = []

    def initialize_driver(self):
        """Initialize the Chrome WebDriver using ChromeDriverManager."""
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in background
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def load_page(self):
        """Open the specified URL in the browser and wait for the page to load."""
        self.driver.get(self.url)
        time.sleep(3)  # wait for Amazon to load

    def extract_data(self):
        """Extract product details from Amazon search results."""
        items = self.driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

        for item in items:
            try:
                title = item.find_element(By.TAG_NAME, "h2").text  
            except:
                title = "N/A"

            try:
                price = item.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
            except:
                price = "N/A"

            try:
                rating = item.find_element(By.XPATH, ".//span[@class='a-icon-alt']").text
            except:
                rating = "N/A"

            try:
                reviews = item.find_element(By.XPATH, ".//span[@class='a-size-base']").text
            except:
                reviews = "N/A"

            self.products.append([title, price, rating, reviews])

    def save_to_csv(self, file_name):
        """Save extracted data into CSV."""
        df = pd.DataFrame(self.products, columns=["Title", "Price", "Rating", "Reviews"])
        df.to_csv(file_name, index=False, encoding="utf-8")
        print(f"✅ Data saved to {file_name}")
        print(df.head())

    def close_driver(self):
        """Close the browser."""
        if self.driver:
            self.driver.quit()

    def run_scraper(self, file_name):
        """Run complete scraper."""
        self.initialize_driver()
        self.load_page()
        self.extract_data()
        self.save_to_csv(file_name)
        self.close_driver()


# Run the scraper
scraper = AmazonScraper("https://www.amazon.in/s?k=laptop&crid=7GH268BP0UT6&sprefix=laptop%2Caps%2C351&ref=nb_sb_noss_2")
scraper.run_scraper("amazon_laptops.csv")
