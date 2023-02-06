from selenium import webdriver
from selenium.webdriver.common.by import By

def test_find_element_elements():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)   
    driver.get("https://the-internet.herokuapp.com/challenging_dom")
    driver.implicitly_wait(10)

    text1 = driver.find_element(By.CSS_SELECTOR, '[class="button"]').text
    print(text1)

    text2 = driver.find_element(By.CSS_SELECTOR, '[class="button alert"]').text
    print(text2)

    text3 = driver.find_element(By.CSS_SELECTOR, '[class="button success"]').text
    print(text3)