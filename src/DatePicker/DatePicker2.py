
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_Date_Picker():
    driver = webdriver.Chrome()
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//input[@id='dob']").click()

    datepicker_Month = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
    datepicker_Month.select_by_visible_text("Nov")
    time.sleep(3)
    datepicker_Year = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
    datepicker_Year.select_by_visible_text("1990")
    time.sleep(3)
    dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

    for date in dates:
        if date.text == "15":
            date.click()
            break

    time.sleep(3)
