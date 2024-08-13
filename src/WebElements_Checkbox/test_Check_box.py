import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_Select_Checkbox():

    driver = webdriver.Chrome()
    myWait = WebDriverWait(driver,10,ignored_exceptions= [NoSuchElementException])
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    Click_Chekc_Box = myWait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='sunday']")))
    get_Checkbox = driver.find_element(By.XPATH,"//input[@id='sunday']")
    Click_Chekc_Box.click()
    print("Is check box selected : ",Click_Chekc_Box.is_selected())

    CheckBoxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@value,'day')]")
    #Scenario1:
    for checknbox in CheckBoxes:
        weekname =checknbox.get_attribute('id')
        if weekname == 'Tuesday' and weekname == 'Wednesday':
            checknbox.click()
    #print(len(CheckBoxes))

    #Scenario2
    # for j in range(len(All_CheckBoxes)):
    #     All_CheckBoxes[j].click()
    time.sleep(3)
    driver.close()
