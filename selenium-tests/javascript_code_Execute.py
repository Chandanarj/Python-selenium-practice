from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_execute_js_code():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)   
    driver.get("https://the-internet.herokuapp.com/")
    driver.implicitly_wait(10)
    time.sleep(2)   
    #driver.execute_script("window.scrollTo(0, 1000);")
    #driver.execute_script('''document.querySelector('[href="/abtest"]').click()''')
    #text = driver.execute_script('''return document.querySelector('[class="example"] > p').innerText''')
    #print(text)

    element = driver.find_element(By.CSS_SELECTOR, '[href="/shadowdom"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    driver.execute_script("arguments[0].click();", element)



   

    