import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

def test_Mouse_DragAndDrop():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")
    driver.maximize_window()
    source_element = driver.find_element(By.ID,"draggable")

    target_element = driver.find_element(By.ID,"droppable")

    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()

    time.sleep(3)

