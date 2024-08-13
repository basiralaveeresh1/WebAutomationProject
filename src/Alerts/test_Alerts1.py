import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select


def test_Alerts():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    #driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']")
    #or you can give like this also
    #Thhis will open the Alert window
    driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
    # normalize-space() --> This will remove the space after the text emement
    alert_window = driver.switch_to.alert
    print(alert_window.text) # It will print the Alert text
    alert_window.send_keys("Hello") # It will send the text to the Alert window
    alert_window.accept() # Close alert window by clicking the "OK" button
    time.sleep(3)



