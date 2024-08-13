import time

from selenium import webdriver

from selenium.webdriver.common.by import By

def test_HRM_Title():

    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    get_title = driver.title
    print(get_title)
    print(driver.current_url)
    print(driver.page_source)
    assert driver.title == "OrangeHRM"
    time.sleep(5)
