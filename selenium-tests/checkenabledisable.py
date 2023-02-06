from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_selenium_demo():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)   
    driver.get("https://the-internet.herokuapp.com/jqueryui/menu")
  
    element1 = driver.find_element(By.ID, 'ui-id-3')
    print(element1.is_displayed())
    assert element1.is_displayed() == True

    element2 = driver.find_element(By.ID, "ui-id-4")
    print(element2.is_displayed())
    assert element2.is_displayed() == False

    element3 = driver.find_element(By.ID, "ui-id-8")
    print(element3.is_displayed())
    assert element3.is_displayed() == False
   