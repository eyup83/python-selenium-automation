from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

BESTSELLER_LINKS = (By.XPATH, "//a[contains(@href, 'zg_bs_tab')]")


@given('Amazon bestsellers page')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify 5 links are displayed')
def verify_links(context):
    links = len(context.driver.find_elements(*BESTSELLER_LINKS))
    assert links == 5, f'expected 5 but got {links}'
