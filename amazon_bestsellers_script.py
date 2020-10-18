from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
BESTSELLER_LINKS = (By.XPATH, "//a[contains(@href, 'zg_bs_tab')]")

# init driver
driver = webdriver.Chrome(executable_path='/Users/eyup/Desktop/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()

driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

links = len(driver.find_elements(*BESTSELLER_LINKS))
assert links == 5, f'expected 5 but got {links}'

