import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_Get_All_LinkText():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    #get_All_Links = driver.find_elements(By.TAG_NAME, 'a')
    get_All_Links = driver.find_elements(By.XPATH, "//a")
    print(len(get_All_Links))
    for i in get_All_Links:
        print(i.text)
