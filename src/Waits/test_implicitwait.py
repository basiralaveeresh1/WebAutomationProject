import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_implicit_wait():

    driver = webdriver.Chrome()

    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    searchBox = driver.find_element(By.NAME,"q")
    searchBox.send_keys("Selenium")
    searchBox.submit()
    driver.find_element(By.XPATH,"//h3[text()='Selenium']")
