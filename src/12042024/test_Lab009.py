import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@allure.title("Verifying the Login page")
@allure.description("TC#1: Please verify the Login Page ")
def test_Login_Page():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    listof_a_tags = driver.find_elements(By.TAG_NAME, 'a')
    mak_Appointment_button = listof_a_tags[5].click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login" , "TC#1: THe URL is not Correct "
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='txt-username']").send_keys("Veeres123")
    driver.find_element(By.XPATH, "//input[@id='txt-password']").send_keys("123456")
    driver.find_element(By.ID,"btn-login").click()
    time.sleep(3)
    Login_Faield_Text_Element = driver.find_element(By.XPATH, "//p[text()='Login failed! Please ensure the username and password are valid.']")
    #print(Login_Fild_Text_Element.is_displayed())
    assert Login_Faield_Text_Element.text == "Login failed! Please ensure the username and password are valid."
    print("The login failed text is displayed : ",Login_Faield_Text_Element.is_displayed())
    allure.attach(driver.get_screenshot_as_png(),name="Failed Login description",attachment_type=AttachmentType.PNG)
    #print(driver.save_screenshot("Failed Login description.png"))
    print("Test case is passed")
    time.sleep(3)
