from Pages.base_page_hw7 import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    CART_EMPTY_HEADER = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

    def cart_empty_shown(self, expected_text):
        self.verify_text(expected_text, *self.CART_EMPTY_HEADER)
