from Pages.main_page_hw7 import MainPage
from Pages.cart_page_hw7 import CartPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page_hw7 = MainPage(self.driver)
        self.cart_page_hw7 = CartPage(self.driver)
