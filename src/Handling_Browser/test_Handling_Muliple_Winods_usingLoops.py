
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Single_Window_Handles():
    driver = webdriver.Firefox()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    #driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
    driver.find_element(By.XPATH,"//button[text()='New Browser Window']").click()
    windowsIds = driver.window_handles
    # for winId in windowsIds:
    #     driver.switch_to.window(winId)
    #     print(driver.title)

    for winId in windowsIds:
        driver.switch_to.window(winId)
        if driver.title == "Automation Testing Practice":
            driver.close()

