from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/eyup/Desktop/Automation/python-selenium-automation/chromedriver')

# Amazon logo, search by Xpath, $x("//i[@class='a-icon a-icon-logo']")
Amazon_logo = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Continue button, search by ID, "continue"
Continue_button = driver.find_element(By.ID, 'continue')

# Need help link, search by Xpath, $x("//span[@class='a-expander-prompt']")
Need_help = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link, search by ID, "auth-fpp-link-bottom"
Forgot_password = driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other issues with sign in link, search by ID, "ap-other-signin-issues-link"
Other_issues = driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create your Amazon account button, search by ID, "createAccountSubmit"
Create_account = driver.find_element(By.ID, 'createAccountSubmit')


