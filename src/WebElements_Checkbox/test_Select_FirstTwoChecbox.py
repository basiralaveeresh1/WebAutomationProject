import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_Select_First_twoChekbox():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()

    CheckBoxs = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@value,'day')]")
    for i in range(len(CheckBoxs)):
        if i<2:
            CheckBoxs[i].click()

    time.sleep(3)