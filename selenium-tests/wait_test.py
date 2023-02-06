from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_wait():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    explicit(driver)

def facebook(driver):
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    driver.find_element(By.CSS_SELECTOR, '[data-testid="open-registration-form-button"]').click()
    driver.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys("Testing")



def explicit(driver):    
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")  
    driver.find_element(By.XPATH, "//button[text()='Remove']").click()

    #element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Add']")))
    status = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '[id="checkbox-example"] button'), "Add"))
    print(status)

    status_input = driver.find_element(By.CSS_SELECTOR, '[id="input-example"] input').is_enabled()
    print(status_input)
    driver.find_element(By.CSS_SELECTOR, '[id="input-example"] button').click()

    status = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '[id="input-example"] button') ,"Disable"))
    status_input = driver.find_element(By.CSS_SELECTOR, '[id="input-example"] input').is_enabled()
    print(status_input)