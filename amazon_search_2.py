from behave import when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SEARCH_BAR = (By.ID, "twotabsearchtextbox")
KEY_WORD = (By.CSS_SELECTOR, "span.a-color-state.a-text-bold")
SEARCH_BTN = (By.XPATH, "//input[@value='Go']")


@given
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input Shoes into Amazon search field and click search')
def search_4_product(context):
    search_bar = context.driver.find_element(*SEARCH_BAR).send_keys('Shoes')

    search_btn = context.driver.find_element(*SEARCH_BTN).click()



@then('Verify page contains "Shoes"')
def verify_text(context):
    key_word = context.driver.find_element(*KEY_WORD)
    assert "Shoes" in key_word.text, f'expected "Shoes" but got {key_word.text}'
