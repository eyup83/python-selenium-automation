from Pages.base_page_hw7 import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    CART = (By.ID, 'nav-cart')

    def open_amazon(self):
        self.open_page('https://www.amazon.com/')

    def click_cart_icon(self):
        self.click(*self.CART)
