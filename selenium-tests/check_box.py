from selenium import webdriver
from selenium.webdriver.common.by import By


def test_check_box():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)   
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    driver.implicitly_wait(10)
    
    checkbox1_element = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')
    print(checkbox1_element.is_selected())
    checkbox1_element.click()
    checkbox1_element = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')
    print(checkbox1_element.is_selected())

    checkbox2_element = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')
    print(checkbox2_element.is_selected())
    checkbox2_element.click() 
    checkbox2_element = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')
    print(checkbox2_element.is_selected())