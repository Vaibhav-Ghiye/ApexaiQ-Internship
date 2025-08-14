from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
query = "laptop"
file = 0

if not os.path.exists("data"):
    os.mkdir("data")

for i in range(1, 3):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=2X8156INMXKC0&qid=1755165288&sprefix=laptop%2Caps%2C222&xpid=yrK7B-_Iv7B2C&ref=sr_pg_3")
    time.sleep(3)  # wait for page load

    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found on page {i}.")

    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
        file += 1

driver.close()
