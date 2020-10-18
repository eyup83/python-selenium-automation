from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/eyup/Desktop/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.amazon.com/')

input_field = driver.find_element(By.ID, 'twotabsearchtextbox')
input_field.send_keys('watch')
search_icon = driver.find_element(By.XPATH, "//input[@value='Go']")
search_icon.click()


result = driver.find_element(By.XPATH, "//span[text()='25']").click()
driver.find_element(By.ID, 'add-to-cart-button').click()
#driver.find_element(By.ID, 'hlb-view-cart-announce').click()
ADDED_TO_CART_HEADER = (By.XPATH, "//h1[@class='a-size-medium a-text-bold']")
text_result = driver.find_element(*ADDED_TO_CART_HEADER)
assert text_result.text == 'Added to Cart', f'Added to Cart but got {text_result.text}'

#driver.quit()
