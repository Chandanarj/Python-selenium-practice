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
    create_account_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="open-registration-form-button"]')
    create_account_button.click()

    day_element = driver.find_element(By.ID, 'day')
    select = Select(day_element)
    #select.select_by_index(2)
    #select.select_by_visible_text("10")
    #select.select_by_value("4")
    month_element = driver.find_element(By.ID, 'month')
    select_month = Select(month_element)
    #select_month.select_by_value("6")
    #select_month.select_by_visible_text("Jul")
    select_month.select_by_index(3)
