from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"

for i in range(1, 5):
    driver.get("https://www.amazon.in/s?k={query}&page={i}&crid=2X8156INMXKC0&qid=1755165288&sprefix=laptop%2Caps%2C222&xpid=yrK7B-_Iv7B2C&ref=sr_pg_3")

    elems = driver.find_elements(By.CLASS_NAME, "puisg-row")
    print(f"{ len(elems)} items found.")
    print(elems)
    # print(elem.get_attribute("outerHTML"))

    for elem in elems:
        print(elem.text)

    time.sleep(2)
    driver.close()