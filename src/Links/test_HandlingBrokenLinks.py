import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Get_All_LinkText():
    driver = webdriver.Chrome()
    driver.get("http://www.deadlinkcity.com/")
    all_Links = driver.find_elements(By.TAG_NAME, "a")
    count = 0
    for link in all_Links:
        url = link.get_attribute("href")
        res = requests.head(url)
        if res.status_code >= 400:
            print(url, "is broken link")
            count += 1
        else:
            print(url,"is valid link")
    print("Total Number of broken links:", count)
