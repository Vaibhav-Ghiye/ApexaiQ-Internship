# Import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime


class JavaVersionScraper:
    """
    A scraper class to extract Java version history from Wikipedia,
    process the data (format dates and versions), and save it to a CSV file.
    """

    def __init__(self, url):
        """
        Initialize the scraper with the target URL.

        Args:
            url (str): The webpage URL to scrape data from.
        """
        self.url = url
        self.driver = None
        self.headers = []
        self.list_of_rows = []
        self.df = None

    def initialize_driver(self):
        """
        Initialize the Chrome WebDriver using ChromeDriverManager.
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def load_page(self):
        """
        Open the specified URL in the browser and wait for the page to load.
        """
        self.driver.get(self.url)
        time.sleep(1)

    def extract_data(self):
        """
        Extract table headers and rows from the page's HTML table body.
        Stores headers in self.headers and rows in self.list_of_rows.
        """
        tables = self.driver.find_element(By.XPATH, "//tbody")
        all_table_rows = tables.find_elements(By.XPATH, ".//tr")

        for i, each_row in enumerate(all_table_rows):
            list_of_data = []

            if i == 0:
                # Extract headers from <th> or <td> in the first row
                all_headers = each_row.find_elements(By.XPATH, ".//th")
                if not all_headers:
                    all_headers = each_row.find_elements(By.XPATH, ".//td")

                self.headers = [header.text for header in all_headers]

            else:
                # Extract data from each table row
                all_data = each_row.find_elements(By.XPATH, ".//td")
                for data in all_data:
                    list_of_data.append(data.text)

                if list_of_data:
                    self.list_of_rows.append(list_of_data)

    def format_dates_and_versions(self):
        """
        Format date columns to dd-mm-yyyy and append '.x' to version numbers.
        """
        for col in self.df.columns:
            # Convert date-like columns to dd-mm-yyyy
            try:
                converted = pd.to_datetime(self.df[col], errors='coerce')
                if converted.notna().any():
                    self.df[col] = converted.dt.strftime('%d-%m-%Y').fillna(self.df[col])
            except:
                pass

            # Append '.x' to version columns
            if "version" in col.lower():
                new_values = []
                for value in self.df[col]:
                    if value and not value.endswith(".x"):
                        new_values.append(value + ".x")
                    else:
                        new_values.append(value)
                self.df[col] = new_values

    def save_to_csv(self, file_name):
        """
        Save the extracted and formatted data to a CSV file.

        Args:
            file_name (str): Name of the CSV file to save.
        """
        self.df = pd.DataFrame(self.list_of_rows, columns=self.headers)
        self.format_dates_and_versions()
        self.df.to_csv(file_name, index=False)
        print(f"Data saved to {file_name}")

    def close_driver(self):
        """
        Close the browser and quit the WebDriver session.
        """
        if self.driver:
            self.driver.quit()

    def run_scraper(self, file_name):
        """
        Run the complete scraping process:
        - Initialize browser
        - Load the page
        - Extract table data
        - Save data to CSV
        - Close the browser

        Args:
            file_name (str): Name of the CSV file to save.
        """
        self.initialize_driver()
        self.load_page()
        self.extract_data()
        self.save_to_csv(file_name)
        self.close_driver()
        print(self.df)


# Create an instance and run the scraper
scraper = JavaVersionScraper("https://en.wikipedia.org/wiki/Java_version_history")
scraper.run_scraper("java_version.csv")