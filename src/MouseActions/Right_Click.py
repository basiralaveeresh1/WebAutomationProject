import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_Mouse_Actions():
    driver = webdriver.Chrome()
    driver.get("https://demo.guru99.com/test/simple_context_menu.html")
    driver.maximize_window()
    click_Me_btn = driver.find_element(By.XPATH,"//span[text()='right click me']")
    actions = ActionChains(driver)

    actions.context_click(click_Me_btn).perform() # It will perform the Mouse Right click
    time.sleep(3)
    copy_element = driver.find_element(By.XPATH,"//span[text()='Copy']")
    copy_element.click()
    time.sleep(3)
    print(driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
    time.sleep(3)
    #driver.switch_to.alert.send_keys("veeresh") # NoAlertPresentException
