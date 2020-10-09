from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SEARCH_FIELD = (By.ID, 'helpsearch')
HEADER = (By.XPATH, "//h1[text()='Cancel Items or Orders']")


@given('Open Amazon help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input cancel order into help search field, hit enter')
def input_cancel_order(context):
    help_input_field = context.driver.find_element(*SEARCH_FIELD)
    help_input_field.send_keys('Cancel order', Keys.ENTER)


@then('Search result Cancel items or orders is shown')
def search_result_shown(context):
    text_result = context.driver.find_element(*HEADER)
    assert text_result.text == 'Cancel Items or Orders', f'Expected Cancel Items or Orders but got {text_result.text}'
