import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


def test_Select_Checkbox1():

    driver = webdriver.Chrome()

    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    CheckBoxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@value,'day')]")
    #Scenario1:

    for checkbox in CheckBoxes:
        checkbox.click()