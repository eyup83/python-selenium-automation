from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

ADDED_TO_CART_HEADER = (By.XPATH, "//h1[@class='a-size-medium a-text-bold']")
INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.XPATH, "//input[@value='Go']")
WATCH_BTN = (By.XPATH, "//span[text()='25']")
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')


@given('Open Amazon home page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input watch into search field')
def input_watch(context):
    context.driver.find_element(*INPUT_FIELD)
    INPUT_FIELD.send_keys('watch')


@when('click on amazon search button')
def click_search(context):
    context.driver.find_element(*SEARCH_BTN)
    SEARCH_BTN.click()


@when('Click on the watch')
def click_on_watch(context):
    context.driver.find_element(*WATCH_BTN).click()


@when('Click on add to cart button')
def click_on_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@then('Verify added to cart is shown')
def verify_added_shown(context):
    text_result = context.driver.find_element(*ADDED_TO_CART_HEADER)
    assert text_result.text == 'Added to Cart', f'Added to Cart but got {text_result.text}'
