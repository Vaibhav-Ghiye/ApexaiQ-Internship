import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def clean_date(date_str: str) -> str:
    cleaned = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
    return cleaned.strip()


def format_date_column(series: pd.Series) -> pd.Series:
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
    def _init_(self, driver_path, url, output_file, software_ids):
        """
        Args:
            driver_path (str): Path to chromedriver.
            url (str): URL to scrape.
            output_file (str): CSV output path.
            software_ids (dict): Dict mapping software display name -> xpath or table id for tables.
        """
        self.driver_path = driver_path
        self.url = url
        self.output_file = output_file
        self.software_ids = software_ids
        self.data = []
        self.driver = None

    def setup_driver(self):
        service = Service(self.driver_path)
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()

    def open_page(self):
        self.driver.get(self.url)
        time.sleep(6)

    def _clean_text(self, elem):
        return elem.text.strip().replace('\n', ' ')

    def scrape_table_by_xpath(self, software_name, xpath):
        try:
            tables = self.driver.find_elements(By.XPATH, xpath)
        except Exception:
            tables = []
        for table in tables:
            # Software name is inside table's first <p><b> tag
            try:
                title_elem = table.find_element(By.XPATH, './/p/b')
                software_actual_name = title_elem.text.strip()
            except Exception:
                software_actual_name = software_name

            # Find headers
            header_elements = table.find_elements(By.TAG_NAME, 'td')
            # The header row in this table is actually the first row with three bold td elements - Version, Release Date, End-of-Life Date
            # So let's fetch first tr, then its td elements
            try:
                header_row = table.find_element(By.TAG_NAME, "tr")
                header_tds = header_row.find_elements(By.TAG_NAME, 'td')
                headers = [td.text.strip() for td in header_tds if td.text.strip()]
            except Exception:
                headers = []

            # Fallback headers
            if not headers:
                headers = ["Version","Release Date","End-of-Life Date"]

            # Rows start after header row
            all_rows = table.find_elements(By.TAG_NAME, 'tr')[2:]  # skip first two rows with empty row and header row

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
        df = pd.DataFrame(self.data)
        if df.empty:
            return df
        df['Release Date'] = format_date_column(df['Release Date'])
        df['EOL Date'] = format_date_column(df['EOL Date'])
        return df

    def save_to_csv(self, df):
        df.to_csv(self.output_file, index=False, encoding="utf-8")
        print(f"✅ Data saved to {self.output_file}")

    def run(self):
        self.setup_driver()
        self.open_page()
        for software_name, xpath in self.software_ids.items():
            self.scrape_table_by_xpath(software_name, xpath)

        df = self.clean_dates()
        self.save_to_csv(df)
        self.driver.quit()


if __name__ == "_main_":
    DRIVER_PATH = r"C:\Users\ASUS\Desktop\ApexaiQ-Internship\Week 1\Day 3\Codes\site scraping\Paloalto_Networks\chromedriver-win64.zip\chromedriver-win64chromedriver.exe"
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

    OUTPUT_FILE = r"C:\Users\hp\Desktop\ApexaIQ\New\Day 4\Codes\a_software_palto.csv"

    scraper = PaloAltoEOLScraper(DRIVER_PATH, URL, OUTPUT_FILE, SOFTWARE_TABLES_XPATHS)
    scraper.run()