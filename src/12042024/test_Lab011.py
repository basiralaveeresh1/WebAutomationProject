import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.regression
@allure.title("Verify to select the checkbox")
@allure.description("TC#1: Verify the checkbox to select ")
def test_Select_Checkbox():
    driver = webdriver.Chrome()
    driver.get("https://www.hyrtutorials.com/p/add-padding-to-containers.html")
    print(driver.title)
    print(driver.current_url)
    #driver.find_element(By.XPATH, "//input[@type='text' and @id='gh-ac']") or
    #driver.find_element(By.ID, "gh-ac")
    driver.maximize_window()
    driver.execute_script('window.scrollBy(0,1000)')
    time.sleep(3)
    select_checkbox = (driver.find_element(By.XPATH,"//td[text()='Roland Mendel']/preceding-sibling::td/child::input[@type='checkbox']"))
    select_checkbox.click()
    time.sleep(3)

    if select_checkbox.is_selected():
        print(" --> Chebox is selected Successfully")
    else:
        print("The checkbox is not selected")

    assert driver.current_url == "https://www.hyrtutorials.com/p/add-padding-to-containers.html"
    assert select_checkbox.is_selected() == True