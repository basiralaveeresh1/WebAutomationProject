import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_Mouse_Actions():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_ondblclick_addeventlistener")
    driver.maximize_window()
    driver.switch_to.frame("iframeResult")
    double_click_text = double_click = driver.find_element(By.XPATH,"//p[text()='Double-click me.']")
    actions = ActionChains(driver)
    actions.double_click(double_click_text).perform()
    time.sleep(3)
    after_double_click_text = driver.find_element(By.XPATH,"//p[text()='I was double-clicked!']")
    assert after_double_click_text.text == "I was double-clicked!"



