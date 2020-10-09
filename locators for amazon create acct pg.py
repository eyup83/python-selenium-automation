from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/eyup/Desktop/Automation/python-selenium-automation/chromedriver')

# Amazon logo, xpath, $x("//i[@class='a-icon a-icon-logo']")
Amazon_logo = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Create account, xpath, $x ("//h1[@class='a-spacing-small']")
Create_acct = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")

# Your name field, id, 'ap_customer_name'
Your_name = driver.find_element(By.ID, 'ap_customer_name')

# Email field, id, 'ap_email'
Email_field = driver.find_element(By.ID, 'ap_email')

# Password field, id, 'ap_password'
Passwd_field = driver.find_element(By.ID, 'ap_password')

# Password text, ("//*[contains(text),'Passwords must be at least 6 characters.']")
Passwd_text = driver.find_element(By.XPATH, "//*[contains(text),'Passwords must be at least 6 characters.']")

# Re-enter passwd, id, 'ap_password_check'
Passwd_reenter = driver.find_element(By.ID, 'ap_password_check')

# Create acct button, id, 'continue'
Create_acct_button = driver.find_element(By.ID, 'continue')

# Conditions link, xpath, "//a[contains(@href, 'Conditions of Use')]"
Conditions_link = driver.find_element(By.XPATH, "//a[contains(@href, 'Conditions of Use')]")

# Privacy link, xpath, "//a[contains(@href, 'Privacy Notice')]"
Privacy_link = driver.find_element(By.XPATH, 'Privacy Notice')

# Sign in button, xpath, "//a[@class='a-link-emphasis']"
Sign_in_link = driver.find_element(By.XPATH, "//a[@class='a-link-emphasis']")
