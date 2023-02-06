from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_selenium_demo():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.facebook.com")
    driver.implicitly_wait(10) 
    driver.minimize_window()
   
    #print (driver.get_window_size())
    #driver.set_window_size(516, 322)
    #print (driver.get_window_size())

    # maximize window
    #driver.maximize_window()
    #print (driver.get_window_size())

    #element = driver.find_element(By.CSS_SELECTOR, '[data-testid="open-registration-form-button"]')
    #element.click()
    
    
    day_element = driver.find_element(By.ID, "day")
    select = Select(day_element)
    select.select_by_index(2)
    
    
    #select.select_by_index(index)
    #select.select_by_visible_text("text")
    #select.select_by_value(value)
    #month_element = driver.find_element(By.ID, "month")
    #select = Select(month_element)
    #select.select_by_visible_text("Jun")
    #select.select_by_value("3")

    #time.sleep(1000)