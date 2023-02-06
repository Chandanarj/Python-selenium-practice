from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_MouseHover():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://the-internet.herokuapp.com/hovers")

    user_icon = driver.find_element(By.CSS_SELECTOR, '[alt="User Avatar"]')
    element = driver.find_element(By.CSS_SELECTOR, '[href="/users/1"]')
    action = ActionChains(driver)
    action.move_to_element(user_icon).click(element).perform()
    
