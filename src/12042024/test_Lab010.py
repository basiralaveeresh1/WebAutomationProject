import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@allure.title("Verifying the Product Title and Prices")
@allure.description("TC#1: Verify all the listed items Title names and Items Prices ")
def test_Title_Names_Prices():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    #driver.find_element(By.XPATH, "//input[@type='text' and @id='gh-ac']") or
    #driver.find_element(By.ID, "gh-ac")
    SearchBox = (driver.find_element(By.XPATH,"//input[@id='gh-ac']"))
    SearchBox.send_keys("16 gb")
    SearchButton = driver.find_element(By.ID,"gh-btn")
    SearchButton.click()
    time.sleep(3)
    Item_TitleNames = driver.find_elements(By.XPATH,"//span[@role='heading']")
    for title in Item_TitleNames:
        print(title.text)

    Item_Price = driver.find_elements(By.CLASS_NAME, "s-item__price")

    for price in Item_Price:
        print(price.text)
    time.sleep(3)


