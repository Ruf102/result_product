import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from result_product.base.base_page import BasePage


class ApplePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Locator
    header_catalog = "//h1[contains(text(), 'Apple — купить в Уфе iPhone, iPad, MacBook и аксессуары')]"
    button_buy_product_1 = "(//button[normalize-space(.)='В корзину'])[1]"
    name_product_1_catalog = "(//div[@class='caption']//h4/a)[1]"
    price_product_1_catalog = "(//*[@class='price '])[1]"
    elements_for_page = "//*[@class='product-thumb']"
    input_limit = "//*[@id='input-limit']"
    input_sort = "//*[@id='input-sort']"
    all_price = "//*[@class='price ']"
    cart_total = "//span[@id='cart-total']"


    # Getters

    def get_header_catalog(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.header_catalog)))

    def get_header_catalog_text(self):
        return self.get_text(self.get_header_catalog())

    def get_count_product(self):
        element = self.browser.find_elements(By.XPATH, self.elements_for_page)
        return len(element)

    def get_button_buy_product_1(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_buy_product_1)))

    def get_name_product_1_catalog(self):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, self.name_product_1_catalog)))

    def get_price_product_1_catalog(self):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, self.price_product_1_catalog)))

    def get_cart_total(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_total)))

    def get_input_limit(self):
        return Select(WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_limit))))

    def get_input_sort(self):
        return Select(WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_sort))))

    def get_all_price(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_all_elements_located((By.XPATH, self.all_price)))

    def get_product_prices_as_numbers(self):
        price_element = self.get_all_price()
        prices = []

        for element in price_element:
            price_text = element.text
            price_clear = "".join(price_text.split()).replace("₽", "")
            prices.append(int(price_clear))

        return prices

    def get_name_product_value(self):
        return self.get_text(self.get_name_product_1_catalog())

    def get_price_product_value(self):
        return self.get_text(self.get_price_product_1_catalog())

    # Action

    def click_button_buy_product_1(self):
        self.get_button_buy_product_1().click()
        print("Нажатие кнопки в корзину первого товара")

    def select_drop_down_limit(self, count):
        self.get_input_limit().select_by_visible_text(f"{count}")
        print(f"Установлен фильтра на лимит товаров на странице кол-во {count}")

    def select_drop_down_sort(self, text):
        self.get_input_sort().select_by_visible_text(text)
        print(f"Установлен фильтра по {text}")

    def click_cart(self):
        self.get_cart_total().click()

    # Methods

    def add_product_cart(self):
        self.click_button_buy_product_1()
