import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

def test_Mouse_DragAndDrop_Offset():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
    driver.maximize_window()

    min_slider_location = driver.find_element(By.XPATH,"//div[@id='slider-range']/span[1]")
    max_slider_location = driver.find_element(By.XPATH,"//div[@id='slider-range']/span[2]")

    print(min_slider_location.location)
    print(max_slider_location.location)

    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(min_slider_location,100,0).perform()
    actions.drag_and_drop_by_offset(max_slider_location,-50,0).perform()
    # drag_and_drop_by_offset(sourcer_element,X,Y)

    print(min_slider_location.location)
    print(min_slider_location.location)
    time.sleep(3)

