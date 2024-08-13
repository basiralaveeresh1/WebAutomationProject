import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_Select_All_Chekbox():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()

    CheckBoxs = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@value,'day')]")
    for CheckBox in CheckBoxs:
        CheckBox.click()
    time.sleep(5)
    for checkbox in CheckBoxs:
        if checkbox.is_selected():
            checkbox.click()
    time.sleep(3)