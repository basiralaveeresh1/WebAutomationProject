import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_Multiple_Window_Handles():
    driver = webdriver.Chrome()
    myWait = WebDriverWait(driver, 10,)  # Explicity Declaration Wait

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    copy_right_link = myWait.until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']")))
    #driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
    time.sleep(4)
    copy_right_link.click()
    Window_IDs = driver.window_handles
    parentWindowID = Window_IDs[0] # E1D04D86FCE73B3CD6752B1C108E0D90
    childWindowID = Window_IDs[1]  # 6510A1773DF2A968A345CC54DC8F1D54
    print(parentWindowID,childWindowID)
    driver.switch_to.window(childWindowID)
    print("Title of the Child window",driver.title)

    driver.switch_to.window(parentWindowID)
    print("Title of the Child window",driver.title)




    #driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
