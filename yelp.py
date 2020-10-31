from selenium.webdriver.common.by import By
from behave import when, then, given
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LINK = (By.XPATH, "//a[contains(text(),'thekebabshop.com')]")
COMPANY_NAME = (By.XPATH, "//a[contains(text(),'kebab')]")


@given("Open Yelp page")
def open_yelp(context):
    context.driver.get("https://www.yelp.com/biz/the-kebab-shop-san-diego-4?osq=The+Kebab+Shop")


@when("Click on website link")
def click_link(context):
    context.original_windows = context.driver.window_handles
    context.original_window = context.driver.current_window_handle
    link = context.driver.find_element(*LINK).click
    print(context.original_windows)
    print(context.original_window)


@when("Switch to a new window")
def switch_windows(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.new_windows = context.driver.window_handles
    print(context.new_windows)
    for window in context.original_windows:
        context.new_windows.remove(window)
    print(context.new_windows)
    context.driver.switch_to_window(context.new_windows[0])


@then("The kebab shop website is open")
def check_name(context):
    context.driver.find_element(*COMPANY_NAME)


@then("A user can close the new window and go to the original")
def go_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)
