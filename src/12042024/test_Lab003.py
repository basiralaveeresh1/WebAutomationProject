import time

from selenium import webdriver

# Selenium 4

def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    print(driver.title)
    assert driver.title == "Login - VWO"
    time.sleep(3)