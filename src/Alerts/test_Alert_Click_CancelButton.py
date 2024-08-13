import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select


def test_Alerts_Click_Cancel_btn():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
    time.sleep(3)
    alert_window = driver.switch_to.alert
    print(alert_window.text)
    alert_window.send_keys("Welcome")
    time.sleep(2)
    alert_window.dismiss()
    time.sleep(3)