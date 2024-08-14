
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
def test_Mouse_DragAndDrop():
    driver = webdriver.Chrome()
    #driver.implicitly_wait(5)
    driver.get("https://www.noon.com/uae-en/")
    driver.maximize_window()
    # Scroll down the page by pixel
    #driver.execute_script("window.scrollBy(0,3000)","")
    #value = driver.execute_script("return window.pageYOffset;")
    #print("Number of pixel moved:", value)
    # Scrolldown the page till the element is visible
    #scroll_elemt = driver.find_element(By.XPATH,"//h2[contains(text(),'ready for school')]")
    #driver.execute_script("arguments[0].scrollIntoView();",scroll_elemt)
    # value = driver.execute_script("return window.pageYOffset;")
    # print("Number of pixel moved:", value)
    #time.sleep(3)
    # Scroll down the page till the end
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    # -document.body.scrollHeight --> it will scroll to the starting position
    driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")

    time.sleep(3)
