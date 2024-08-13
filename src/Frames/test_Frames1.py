import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Frames():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    # driver.switch_to.frame("frame-one796456169")
    # driver.find_element(By.XPATH,"//input[@id='RESULT_TextField-0']").send_keys("Veeresh Basirala")
    # #driver.find_element(By.NAME,"RESULT_TextField-0").send_keys("Veeresh B")
    # time.sleep(3)
    iframe = driver.find_element(By.XPATH, "//iframe[@id='frame-one796456169']")
    driver.switch_to.frame(iframe)
    driver.find_element(By.XPATH,"//input[@type='text' and @id='RESULT_TextField-0']").send_keys("Veeresh")
    time.sleep(4)

    driver.switch_to.frame()
    driver.switch_to.default_content()
    driver.switch_to.parent_frame()
    driver.switch_to.window()
    driver.switch_to.new_window()
    driver.switch_to.active_element
    driver.switch_to.alert