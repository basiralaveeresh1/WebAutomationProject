import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Cl_Qu():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
    driver.close()
    time.sleep(5)
    #driver.quit()
