
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_Text_Vs_GetAttribute():

    driver = webdriver.Chrome()

    driver.get("https://www.noon.com/uae-en/")
    Login_Text = driver.find_element(By.XPATH, "//span[@id='dd_header_signInOrUp']")
    print(Login_Text.text) # Inner text

    print(Login_Text.get_attribute("class"))  # returns values of any attribute of web element

    # emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
    #
    # emailbox.clear()
    # emailbox.send_keys("abc@gmail.com")
    #
    # print("result of text:",emailbox.text)  # printed nothing
    # print("result of get_attribute():",emailbox.get_attribute('value')) #abc@gmail.com

    # button=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
    # print("result of text:",button.text)
    # print("result of get_attribute():",button.get_attribute('value'))
    # print("result of get_attribute():",button.get_attribute('type'))
