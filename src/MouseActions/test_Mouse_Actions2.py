
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_Mouse_Actions():
    driver = webdriver.Chrome()
    driver.get("https://omayo.blogspot.com/")
    driver.maximize_window()
    act= ActionChains(driver)
    main_menu = driver.find_element(By.XPATH,"//span[text()='Blogs']")
    list_menu = driver.find_element(By.XPATH,"//span[text()='SeleniumOneByArun']")

    act.move_to_element(main_menu).move_to_element(list_menu).click().perform()
    time.sleep(3)
    assert driver.current_url == "https://seleniumone-by-arun.blogspot.com/"
    time.sleep(3)

