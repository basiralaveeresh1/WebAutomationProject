import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Choose_Checbox2():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    CheckBoxs = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@value,'day')]")
    print(len(CheckBoxs))
    for CheckBox in CheckBoxs:
        weekname = CheckBox.get_attribute("id")
        if weekname == 'sunday' or weekname == 'monday' or weekname == 'friday':
            CheckBox.click()
        print(CheckBox.is_selected())
    time.sleep(5)
    driver.quit()
