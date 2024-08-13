import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Condtional_Methods():

    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com/register")
    driver.maximize_window()
    searchBox = driver.find_element(By.ID,"small-searchterms")
    print("Display status: ", searchBox.is_displayed())
    print("Enabeld status: ", searchBox.is_enabled())
    register_text = driver.find_element(By.XPATH,"//h1[text()='Register']").is_displayed()
    print("Register_Text: ",register_text)
    radio_male_btn = driver.find_element(By.XPATH,"//input[@id='gender-male']")
    radio_female_btn = driver.find_element(By.XPATH, "//input[@id='gender-female']")

    print("Default radio buttons status")
    print(radio_male_btn.is_selected()) # false
    print(radio_female_btn.is_selected()) # false
    time.sleep(2)
   # radio_male_btn.click()

    print("After selecting male Radio button")
    print(radio_male_btn.is_selected())  # True
    time.sleep(3)
    print(radio_female_btn.is_selected())  # false
    time.sleep(3)

    radio_female_btn.click()

    print("After selecting female Radio button")
    print(radio_male_btn.is_selected())  # True
    time.sleep(3)
    print(radio_female_btn.is_selected())  # false
    time.sleep(3)