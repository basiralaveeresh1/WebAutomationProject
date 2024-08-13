import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select


def test_Select_Value_from_DropDown_without_selectClass():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    allOptions = driver.find_elements(By.XPATH, "//*[@id='country']/option")
    print(len(allOptions))
    for i in allOptions:
        print(i.text)
