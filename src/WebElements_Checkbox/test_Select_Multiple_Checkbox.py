import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_Check_Box():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    elements = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@value,'day')]")
    print(len(elements))
    for element in elements:
        element.click()

    time.sleep(3)