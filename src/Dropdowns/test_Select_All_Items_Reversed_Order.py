import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_Select_Value_from_DropDown():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    lst_box = driver.find_element(By.XPATH,"//select[@id='country']")
    select = Select(lst_box)
    all_options = select.options
    #lst_box.select_by_visible_text("United Kingdom")

    for item in reversed(all_options):
        get_all_value = select.select_by_visible_text(item.text)
        print(get_all_value)
    time.sleep(3)