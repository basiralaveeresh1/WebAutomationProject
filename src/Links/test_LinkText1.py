import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Get_All_LinkText():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    Link_Text = driver.find_element(By.LINK_TEXT,"orange HRM")
    print(Link_Text)
    Link_Text.click()
    time.sleep(3)