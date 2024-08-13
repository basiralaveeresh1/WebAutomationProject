import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Find_Single_Element():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    time.sleep(3)
   #  # Scenario1: Locator matching with single webelement
   #  Element = driver.find_element(By.XPATH, "//form[@id='nav-search-bar-form']")
   #  Element.send_keys("Apple MacBook")
   #  time.sleep(3)

   # #Scenario2:
   #  Elemetns = driver.find_element(By.XPATH,"//div[@class='navLeftFooter nav-sprite-v1']//a")
   #  print(Elemetns.text)

    #Senario3: Element is not visible on the webpage. Then it will throw an error like (NoSuchElementException)
    #
    # Elements = driver.find_elements(By.XPATH, "//input[@id='twotabsearchtextbox']")
    # time.sleep(5)
    # print(len(Elements)) #1
    # Elements[0].send_keys("Iphone 15")
    # time.sleep(3)


    Elemetns = driver.find_elements(By.XPATH,"//div[@class='navLeftFooter nav-sprite-v1']//a")
    print(len(Elemetns))
    # print(Elemetns[0].text)
    # print(Elemetns[2].text)
    for ele in Elemetns:
        print(ele.text)

    Sing_in = driver.find_elements(By.XPATH, "//span[text()='Sign i']")
    print(len(Sing_in))


