
from selenium import webdriver
from selenium.common import NoSuchWindowException, NoSuchElementException, ElementNotVisibleException, \
    ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_implicit_wait():

    driver = webdriver.Chrome()

    myWait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchWindowException,
                                                         NoSuchElementException,
                                                         ElementNotVisibleException,
                                                         ElementNotSelectableException]) # Explicity Declaration Wait

    driver.get("https://www.google.com/")
    driver.maximize_window()
    searchBox = driver.find_element(By.NAME, "q")
    searchBox.send_keys("Selenium")
    searchBox.submit()
    try:
        searchLink = myWait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Slenium']")))
        # The actual value is : Selenium but i mentioned like Slenium
        print(searchLink)
        searchLink.click()
    except:
        print("Test case is falied")
        driver.quit()




