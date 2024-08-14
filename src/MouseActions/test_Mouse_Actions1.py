import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_Mouse_Actions():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    act= ActionChains(driver)
    first_ele = driver.find_element(By.XPATH,"//span[@id='nav-link-accountList-nav-line-1']")
    singn_in = driver.find_element(By.XPATH,"//span[text()='Sign in']")
    # second_ele = driver.find_element(By.XPATH,"//span[text()='Baby Wishlist']")
    # third_ele = driver.find_element(By.XPATH,"//span[text()='Wish from Any Website']")

    act.move_to_element(first_ele).move_to_element(singn_in).click().perform()
    time.sleep(5)
