import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def clean_date(date_str: str) -> str:
    """
    Clean date strings by removing ordinal suffixes like 'st', 'nd', 'rd', 'th'.
    """
    cleaned = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
    return cleaned.strip()


def format_date_column(series: pd.Series) -> pd.Series:
    """
    Convert a pandas Series of date strings into standardized 'YYYY-MM-DD' format.
    """
    def parse_and_format(x):
        if not isinstance(x, str):
            return ""
        cleaned = clean_date(x)
        dt = pd.to_datetime(cleaned, errors='coerce', dayfirst=True)
        if pd.isna(dt):
            try:
                dt2 = pd.to_datetime(cleaned, errors='coerce', infer_datetime_format=True)
                if pd.isna(dt2):
                    return ""
                return dt2.strftime('%Y-%m-%d')
            except Exception:
                return ""
        return dt.strftime('%Y-%m-%d')
    return series.apply(parse_and_format)


class PaloAltoEOLScraper:
    """
    Scraper class to extract End-of-Life (EOL) summary data of Palo Alto Networks software.
    """

    def __init__(self, driver_path, url, output_file, software_ids):
        """
        Initialize the scraper with driver, target URL, output path, and software table XPaths.
        """
        self.driver_path = driver_path
        self.url = url
        self.output_file = output_file
        self.software_ids = software_ids
        self.data = []
        self.driver = None


    def setup_driver(self):
        """
        Initialize and start the Chrome WebDriver.
        """
        service = Service(self.driver_path)
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()


    def open_page(self):
        """
        Open the target URL in the browser and wait for 6 seconds for the page to load.
        """
        self.driver.get(self.url)
        time.sleep(6)


    def _clean_text(self, elem):
        """
        Clean text from a WebElement by removing leading/trailing whitespace and newlines.
        """
        return elem.text.strip().replace('\n', ' ')
    

    def scrape_table_by_xpath(self, software_name, xpath):
        """
        Scrape a single software table using its XPath.
        """
        try:
            tables = self.driver.find_elements(By.XPATH, xpath)
        except Exception:
            tables = []
        for table in tables:
            try:
                title_elem = table.find_element(By.XPATH, './/p/b')
                software_actual_name = title_elem.text.strip()
            except Exception:
                software_actual_name = software_name

            try:
                header_row = table.find_element(By.TAG_NAME, "tr")
                header_tds = header_row.find_elements(By.TAG_NAME, 'td')
                headers = [td.text.strip() for td in header_tds if td.text.strip()]
            except Exception:
                headers = []

            if not headers:
                headers = ["Version","Release Date","End-of-Life Date"]

            all_rows = table.find_elements(By.TAG_NAME, 'tr')[2:]  # Skip header rows

            for row in all_rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) < 3:
                    continue
                rec = {
                    "Software Name": software_actual_name,
                    "Version": cells[0].text.strip(),
                    "Release Date": cells[1].text.strip(),
                    "EOL Date": cells[2].text.strip()
                }
                self.data.append(rec)


    def clean_dates(self):
        """
        Convert the 'Release Date' and 'EOL Date' columns to a standardized format.
        """
        df = pd.DataFrame(self.data)
        if df.empty:
            return df
        df['Release Date'] = format_date_column(df['Release Date'])
        df['EOL Date'] = format_date_column(df['EOL Date'])
        return df


    def save_to_csv(self, df):
        """
        Save the DataFrame to a CSV file.
        """
        df.to_csv(self.output_file, index=False, encoding="utf-8")
        print(f"✅ Data saved to {self.output_file}")


    def run(self):
        """
        Run the full scraping process: initialize driver, open page, scrape tables, clean dates, save CSV, and quit browser.
        """
        self.setup_driver()
        self.open_page()
        for software_name, xpath in self.software_ids.items():
            self.scrape_table_by_xpath(software_name, xpath)

        df = self.clean_dates()
        self.save_to_csv(df)
        self.driver.quit()


if __name__ == "__main__":
    DRIVER_PATH = r"C:\Users\ASUS\Desktop\ApexaiQ-Internship\Week 1\Day 3\Codes\site scraping\Paloalto_Networks\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    URL = "https://www.paloaltonetworks.com/services/support/end-of-life-announcements/end-of-life-summary"
    
    SOFTWARE_TABLES_XPATHS = {
        "Prisma Access Browser": "//*[@id='prisma-access-browser']",
        "Threat Management (including QRadar) SaaS Products acquired from IBM": "//*[@id='qradar']",
        "PAN-OS & Panorama": "//*[@id='pan-os-panorama']",
        "Panorama Plugins": "//*[@id='panorama-plugin']",
        "Traps, ESM and Cortex XDR agent": "//*[@id='traps-esm-and-cortex']",
        "Cortex XSOAR": "//*[@id='cortex-xsoar']",
        "GlobalProtect™": "//*[@id='globalprotect']",
        "Prisma Cloud Compute Edition": "//*[@id='prisma-cloud-compute']",
        "LightCyber Magna Virtual Appliances": "//*[@id='lightcyber-magna']",
        "Evident.io™": "//*[@id='evident-io']",
        "Prisma SD-WAN": "//*[@id='cloudgenix']",
        "BRIGHTCLOUD Subscription": "//*[@id='brightcloud-subscription']",
        "VM-Series Models": "//*[@id='vm-series-models']"
    }

    OUTPUT_FILE = r"C:\Users\ASUS\Desktop\ApexaiQ-Internship\Week 1\Day 3\Codes\site scraping\Paloalto_Networks\PaloAlto_EOL_Summary.csv"

    scraper = PaloAltoEOLScraper(DRIVER_PATH, URL, OUTPUT_FILE, SOFTWARE_TABLES_XPATHS)
    scraper.run()
