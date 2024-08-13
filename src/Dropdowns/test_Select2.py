import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_Select_Value_from_DropDown():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    drpcountry = Select(driver.find_element(By.XPATH,"//select[@id='country']"))
    drpcountry.select_by_visible_text("United Kingdom")
    currently_selected_option = drpcountry.first_selected_option.text
    if "United Kingdom" in currently_selected_option:
        print("The selected value is available in the dropdown")
    else:
        print("The selected value is not available in the dropdown")
    #time.sleep(3)
    #print(drpcountry.first_selected_option)
    print(drpcountry.first_selected_option.text)
