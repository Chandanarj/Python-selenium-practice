from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)   
driver.get("https://facebook.com/")

element = driver.find_element(By.ID, "email")
element.clear()
element.send_keys("Testing@gmail.com")

element = driver.find_element(By.ID, "pass")
element.clear()
element.send_keys("Password")

element = driver.find_element(By.NAME, "login").click()
element.click()
