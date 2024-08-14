import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_Mouse_Actions():
    driver = webdriver.Chrome()
    driver.get("https://demo.guru99.com/test/simple_context_menu.html")
    driver.maximize_window()
    double_click = driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']")
    actions = ActionChains(driver)
    actions.double_click(double_click).perform()
    time.sleep(2)
    print(driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
    time.sleep(1)
