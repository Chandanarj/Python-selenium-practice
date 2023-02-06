from selenium import webdriver
from selenium.webdriver.common.by import By


def test_alert():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)   
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = driver.switch_to.alert
    alert.accept()
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert = driver.switch_to.alert
    print(alert.text)
    alert.dismiss()
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    alert = driver.switch_to.alert
    alert.send_keys("Testing")
    alert.accept()
   
   