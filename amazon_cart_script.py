from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/eyup/Desktop/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.amazon.com')

driver.find_element(By.ID, 'nav-cart').click()

CART_EMPTY_HEADER = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")
text_result = driver.find_element(*CART_EMPTY_HEADER)
assert text_result.text == 'Your Amazon Cart is empty', f'Your Amazon Cart is empty but got {text_result.text}'
