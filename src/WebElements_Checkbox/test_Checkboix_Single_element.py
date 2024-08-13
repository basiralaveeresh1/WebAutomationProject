import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_Select_Checkbox_Single_elemt():

    driver = webdriver.Chrome()

    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    CheckBoxe = driver.find_element(By.XPATH,"//input[@id='monday']")
    print(CheckBoxe.is_selected())
    CheckBoxe.click()
    print(CheckBoxe.is_selected())
    time.sleep(3)

