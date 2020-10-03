from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='/Users/eyup/Desktop/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')
help_input_field = driver.find_element(By.ID, 'helpsearch')
help_input_field.send_keys('Cancel order')
help_input_field.send_keys(Keys.ENTER)

text_result = driver.find_element(By.XPATH, "//*[contains(text(),'" + 'Cancel Items or Orders' + "')]")
assert text_result.text == 'Cancel Items or Orders', f'Expected Cancel Items or Orders but got {text_result.text}'

driver.quit()

