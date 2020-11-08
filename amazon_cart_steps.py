from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

CART = (By.ID, 'nav-cart')
CART_EMPTY_HEADER = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")


@given('Open Amazon home page2')
def open_amazon_help(context):
    context.app.main_page_hw7.open_amazon()


@when('Click on Cart')
def click(context):
    context.app.main_page_hw7.click(*CART)


@then('Your shopping cart is empty is shown')
def verify_text(context):
    context.app.cart_page_hw7.verify_text('"Your shopping cart is empty"')
    # text_result = context.driver.find_element(*CART_EMPTY_HEADER)
    # assert text_result.text == 'Your Amazon Cart is empty', f'Your Amazon Cart is empty but got {text_result.text}'
