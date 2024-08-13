import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Inner_Frames():
    driver = webdriver.Chrome()
    driver.get("https://demo.automationtesting.in/Frames.html")
    driver.maximize_window()
    #driver.find_element(By.XPATH,"//a[text()='Iframe with in an Iframe']").click() # it will throw an error message because there is spaces between the words
    # or
    driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
    outer_frame = driver.find_element(By.XPATH,"//div[@id='Multiple']//iframe")
    driver.switch_to.frame(outer_frame)
    innerframe = driver.find_element(By.XPATH,"//div[@class='iframe-container']/iframe")
    driver.switch_to.frame(innerframe)
    driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Veeeresh")
    time.sleep(3)
    #driver.switch_to.parent_frame() it will directly switch to parent window
    #driver.switch_to.default_content() # It will directly switch to default page



