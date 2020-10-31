from time import sleep

from selenium.webdriver.common.by import By
from behave import when, then, given
from selenium.webdriver.support import expected_conditions as EC

APP_LINK = (By.XPATH, "//a[contains(text(),'Amazon applications')]")
APP_PAGE = (By.XPATH, "//a[contains(text(),'AmazonApps')]")


@given("Open Amazon T&C page")
def open_yelp(context):
    context.driver.get(
        "https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when("Store original windows")
def store_windows(context):
    context.original_windows = context.driver.window_handles
    context.original_window = context.driver.current_window_handle


@then("Click on Amazon applications link")
def click_apps(context):
    app_link = context.driver.find_element(*APP_LINK).click


@then("Switch to the newly opened window")
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    #sleep(5)
    context.new_windows = context.driver.window_handles
    print(context.new_windows)
    for window in context.original_windows:
        context.new_windows.remove(window)
    print(context.new_windows)
    context.driver.switch_to_window(context.new_windows[0])


@then("Amazon app page is opened")
def check_name(context):
    context.driver.find_element(*APP_PAGE)


@then("User can close new window and switch back to original")
def go_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)
