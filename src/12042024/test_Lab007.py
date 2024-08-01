import time

from selenium import webdriver

def test_Opne_vwo_Login():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    time.sleep(2)
    driver.back()
    print(driver.title)
    time.sleep(2)
    driver.forward()
    print(driver.title)
    time.sleep(2)
    driver.refresh()
    print(driver.title)
    time.sleep(4)
    driver.quit()


