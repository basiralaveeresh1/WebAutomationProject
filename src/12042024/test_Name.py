import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@allure.title("Verifying the Login page")
@allure.description("TC#1: Please verify the Login Page ")
def test_Login_Page_with_ID():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    Make_Appointment_btn = driver.find_element(By.CLASS_NAME, "btn btn-dark btn-lg")
    Make_Appointment_btn.click()
    login_Text_msg = driver.find_element(By.XPATH, "//*[text()='Please login to make appointment.']")
    # assert login_Text_msg.text == "Please login to make appointment."
    print(login_Text_msg.text == "Please login to make appointment.")
    time.sleep(3)
