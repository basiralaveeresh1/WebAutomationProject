import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_Select_last_twoChekbox():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    CheckBoxs = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@value,'day')]")

    for CheckBox in range(len(CheckBoxs)-3,len(CheckBoxs)):
        CheckBoxs[CheckBox].click()


    time.sleep(4)
