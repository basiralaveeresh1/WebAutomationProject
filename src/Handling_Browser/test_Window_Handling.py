import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Single_Window_Handles():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    winsow_ID = driver.current_window_handle
    print(winsow_ID)