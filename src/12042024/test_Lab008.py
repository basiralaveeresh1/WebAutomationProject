import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Opne_vwo_Login_page():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    #element = driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']").click()

   # < a
   # id = "btn-make-appointment"
   # href = "./profile.php#login"
   # class ="btn btn-dark btn-lg" xpath="1" > Make Appointment < / a >

    # Locators
    # ID, Name, Classname, tagname, linktext, Partial Link text
    # driver.find_element(By.NAME,value="btn btn-dark btn-lg")
    # driver.find_element(By.TAG_NAME,value='a')
    # driver.find_element(By.XPATH, value="//a[@id='btn-make-appointment']").click()
    #driver.find_element(By.ID,'btn-make-appointment').click()
    #driver.find_element(By.LINK_TEXT,'Make Appointment').click()
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Make').click()
    time.sleep(3)