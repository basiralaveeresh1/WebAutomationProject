import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Navigetioanl_Commands():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in")
    driver.get("https://www.noon.com/")
    driver.back()
    current_url_a = driver.current_url
    print(current_url_a)
    time.sleep(3)
    driver.refresh()
    time.sleep(3)
    driver.forward()
    current_url_n = driver.current_url
    print(current_url_n)
    time.sleep(3)
