from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_selenium_demo():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)   
    driver.get("http://www.facebook.com")
    print(driver.get_window_size())
    
    #driver.set_window_size(1225, 1025)
    driver.maximize_window()
    
    #driver.minimize_window()
    #time.sleep(2000)

    element = driver.find_element(By.ID, "email")
    element.clear()
    element.send_keys("Test@gmail.com")

    element_pass = driver.find_element(By.ID, "pass")
    element_pass.clear()
    element_pass.send_keys("Password")

    login_button_element = driver.find_element(By.NAME, "login")
    login_button_element.click()

    #driver.quit()


