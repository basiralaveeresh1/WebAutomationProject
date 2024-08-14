import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_Date_Picker():
    driver = webdriver.Chrome()
    driver.get("https://jqueryui.com/datepicker/")
    driver.maximize_window()
    #First navigate inot the Iframe
    driver.switch_to.frame(0)
    # or
    # mm/dd/yy
    #driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("08/13/2024")
    year = "2022"
    month = "October"
    day = "15"
    driver.find_element(By.XPATH, "//*[@id='datepicker']").click() # Opens the Date Picker
    while True:
        mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
        yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

        if mon == month and yr == year:
            break
        else:
            driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click() # Prev Arrow
    time.sleep(3)

    # Find the Dates
    dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
    for ele in dates:
        if ele.text == day:
            ele.click()
            break
    time.sleep(4)