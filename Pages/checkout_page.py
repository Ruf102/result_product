import time

from faker.proxy import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from result_product.base.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    #Locators

    header = "//h1[text()='Оформление заказа']"
    name_product_order = "//td[@class='name']"
    price_product_order = "//td[@class='price']"
    price_product_result_order = "//td[@class='total']"
    price_cart_total = "(//span[@class='simplecheckout-cart-total-value'])[3]"
    first_name = "//input[@id='customer_firstname']"
    number = "//input[@id='customer_telephone']"
    check_box_rule = "//span[@id='agreement_checkbox']"
    checkout_button = "//a[@id='simplecheckout_button_confirm']"

    #Getters

    def get_header(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, self.header)))

    def get_header_value(self):
        return self.get_header().text

    def get_name_product_order(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, self.name_product_order)))

    def get_price_product_order(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.price_product_order)))

    def get_price_product_result_order(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.price_product_result_order)))

    def get_price_cart_total(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.price_cart_total)))

    def get_first_name(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.first_name)))

    def get_number(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.number)))

    def get_check_box_rule(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.check_box_rule)))

    def get_checkout_button(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.checkout_button)))

    def get_name_product_order_value(self):
        return self.get_name_product_order().text

    def get_price_product_order_value(self):
        return self.get_price_product_order().text

    def get_price_product_result_order_value(self):
        return self.get_price_product_result_order().text

    def get_price_cart_total_value(self):
        return self.get_price_cart_total().text

    # Actions

    def input_first_name(self):
        faker = Faker('ru_RU')
        self.get_first_name().send_keys(faker.first_name())

    def input_telephone(self):
        faker = Faker("ru_RU")
        self.get_number().send_keys(faker.phone_number())

    def click_check_box_rule(self):
        self.get_check_box_rule().click()

    def click_checkout_button(self):
        self.get_checkout_button().click()

    # Methods

    def complete_order(self):
        self.input_first_name()
        time.sleep(5)
        self.input_telephone()
        time.sleep(5)
        self.click_check_box_rule()
        #self.click_checkout_button()