import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_Click_And_Hold():
    driver = webdriver.Chrome()
    driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')
    clickable = driver.find_element(By.ID, "clickable")
    actions = ActionChains(driver)
    actions.click_and_hold(clickable).perform()
    # or you can use like this also in a single line
    #ActionChains(driver).click_and_hold(clickable).perform()

