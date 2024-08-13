
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select


def test_Alerts_btn():
    driver = webdriver.Chrome()
    driver.get("https://mypage.rediff.com/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    driver.switch_to.alert.accept()
    time.sleep(3)


