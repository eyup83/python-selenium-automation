from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

CART = (By.ID, 'nav-cart')
CART_EMPTY_HEADER = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")


@given('Open Amazon home page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Cart')
def click_cart(context):
    cart_btn = context.driver.find_element(*CART)
    cart_btn.click()


@then('Your shopping cart is empty is shown')
def cart_empty_shown(context):
    text_result = context.driver.find_element(*CART_EMPTY_HEADER)
    assert text_result.text == 'Your Amazon Cart is empty', f'Your Amazon Cart is empty but got {text_result.text}'
