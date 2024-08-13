
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select


def test_Alerts_btn():
    driver = webdriver.Chrome()
    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    driver.maximize_window()
    Aut_text = driver.find_element(By.XPATH,"//p")
    assert Aut_text.text == "Congratulations! You must have the proper credentials."
    time.sleep(5)

