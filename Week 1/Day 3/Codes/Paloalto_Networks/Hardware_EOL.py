from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import datetime
import re


class PaloAltoEOLScraper:
    """
    Scrapes the Palo Alto Networks hardware end-of-life table
    and outputs a CSV of the desired columns using XPATH only.
    """
    def __init__(self, url):
        self.url = url
        self.driver = None
        self.products = []  

    def initialize_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def load_page(self):
        self.driver.get(self.url)
        time.sleep(3)  # Wait for page to load

    def format_date(self, date_str):
        """
        Convert date string (e.g., "December 31, 2028", "August 1st, 2029") into "yyyy-mm-dd" format.
        Returns empty string if parsing fails.
        """
        # Remove ordinal suffixes (st, nd, rd, th) from day
        clean_date_str = re.sub(r'(\d{1,2})(st|nd|rd|th)', r'\1', date_str)

        for fmt in ("%B %d, %Y", "%b %d, %Y", "%Y-%m-%d"):  # Trying common formats
            try:
                dt = datetime.datetime.strptime(clean_date_str, fmt)
                return dt.strftime("%Y-%m-%d")
            except ValueError:
                continue
            
        # If parsing fails, return original string or empty string as required
        return ""

    def extract_data(self):
        # Locate table rows excluding the header
        rows = self.driver.find_elements(By.XPATH, '//table//tr[position()>1]')
        vendor = "Palo Alto"
        for row in rows:
            try:
                # Columns: 1=productName, 3=EOL Date, 4=resource, 6=Recommended replacement
                productName = row.find_element(By.XPATH, './td[1]').text.strip()
                raw_eolDate = row.find_element(By.XPATH, './td[3]').text.strip()
                eolDate = self.format_date(raw_eolDate)
                resource = row.find_element(By.XPATH, './td[4]').text.strip()
                recommended = row.find_element(By.XPATH, './td[6]').text.strip()
                self.products.append([vendor, productName, eolDate, resource, recommended])
            except Exception:
                continue

    def save_to_csv(self, file_name):
        df = pd.DataFrame(self.products, columns=["vendor", "productName", "EOL Date", "resource", "Recommended replacement"])
        df.to_csv(file_name, index=False, encoding="utf-8")
        print(f"✅ Data saved to {file_name}")
        print(f"📦 Total Products Scraped: {len(df)}")
        print(df.head())

    def close_driver(self):
        if self.driver:
            self.driver.quit()

    def run_scraper(self, file_name):
        self.initialize_driver()
        self.load_page()
        self.extract_data()
        self.save_to_csv(file_name)
        self.close_driver()


# Run the scraper
scraper = PaloAltoEOLScraper("https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware-end-of-life-dates")
scraper.run_scraper("Hardware_EOL_products.csv")
