from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_element_demo():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)   
    driver.get("https://www.facebook.com/")

    element_text = driver.find_element(By.TAG_NAME, "h2")
    print(element_text.text)

    element_user_input = driver.find_element(By.CSS_SELECTOR, "input[id='email']")
    element_user_input.send_keys("test@gmail.com")
    
    password_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgotten")
    password_link.click()