from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='/Users/eyup/Desktop/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.amazon.com')
ORDER_BTTN = (By.ID, 'nav-orders')
orders_button = driver.find_element(*ORDER_BTTN).click()

SIGN_IN_PG = (By.XPATH, "//h1[@class='a-spacing-small']")

sign_in_header = driver.find_element(*SIGN_IN_PG)
assert "Sign-In" in sign_in_header.text, f'Expected "Sign-In" but got {sign_in_header.text}'

driver.quit()
