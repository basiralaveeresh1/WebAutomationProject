import time

from selenium import webdriver

def test_demologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    time.sleep(3)  #You are telling to wait for 3 to Python Interpreter
    driver.get("https://google.com")
    time.sleep(3)
    print(driver.title)