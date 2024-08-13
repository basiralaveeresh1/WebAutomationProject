import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.regression
@allure.title("Verify to select the checkbox")
@allure.description("TC#1: Verify the checkbox to select ")
def test_CSSSelector_Demo():
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com/")
    print(driver.title)
    driver.maximize_window()
    #driver.find_element(By.CSS_SELECTOR,"input#small-searchterms").send_keys("T-shirts")
    #time.sleep(3)
    #Note: You can you follow like this also without using tagname. but "#" should be there for ID
   # driver.find_element(By.CSS_SELECTOR,"#small-searchterms").send_keys("T-Shirts")
    #time.sleep(3)

   # driver.find_element(By.CSS_SELECTOR, "input.search-box-text").send_keys("T-shirts")
   # time.sleep(3)
    # Note:  #You can you follow like this also without using tagname. but "." should be there for class name
    driver.find_element(By.CSS_SELECTOR, ".search-box-text").send_keys("T-shirts")
    time.sleep(3)

    #driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    #time.sleep(3)

    driver.find_element(By.CSS_SELECTOR,"button.button-1[type='submit']").click()
    time.sleep(3)