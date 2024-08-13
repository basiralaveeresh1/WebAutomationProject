import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_Select_Value_from_DropDown():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    #drp_Country_element = driver.find_element(By.XPATH,"//select[@id='country']")
    #drpcountry = Select(drp_Country_element)
    # you can directly pass the Xpath through Select()
    drpcountry = Select(driver.find_element(By.XPATH,"//select[@id='country']"))
    #drpcountry.select_by_visible_text("United Kingdom")
    #time.sleep(3)
    #drpcountry.select_by_value("canada")
    #time.sleep(3)
    # drpcountry.select_by_index(5) # Australia
    # time.sleep(3)

    # Capture all the options and print it
    alloptions = drpcountry.options
    print(len(alloptions))
    # for i in alloptions:
    #     #print(i.text) or you can give like this also
    #     dropdown_text = i.text
    #     print(dropdown_text)
    print("Without using buildin functions for selecting the dropdown")
    for i in alloptions:
        if i.text == "India":
            i.click()
            #print("The country selected: ",i.is_selected())
            break
    time.sleep(3)