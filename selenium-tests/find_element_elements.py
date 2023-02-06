from selenium import webdriver
from selenium.webdriver.common.by import By

def test_find_element_elements():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)   
    driver.get("https://the-internet.herokuapp.com/")
    driver.implicitly_wait(10)

    elements = driver.find_element(By.CSS_SELECTOR, '[id="content"] a1')
    #print(len(elements))

    #for element in elements:
    #    print(element.text)