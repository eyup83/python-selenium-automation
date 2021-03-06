from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.XPATH, "//input[@value='Go']")
SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input Dress into Amazon search field')
def input_search_word(context):
    context.driver.find_element(*SEARCH_INPUT).send_keys('Dress')


@when('Click on Amazon search icon')
def click_search_icon(context):
    search_icon = context.driver.find_element(*SEARCH_ICON)
    search_icon.click()


@then('Search result Dress is shown')
def verify_search_result(context):
    result = context.driver.find_element(*SEARCH_RESULT)
    assert result.text == '"Dress"', f'Expected Dress but got {result.text}'
