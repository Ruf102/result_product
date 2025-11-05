import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from result_product.Pages.cart_page import CartPage
from result_product.base.base_page import BasePage


class ApplePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)


    expected_url = "https://divizion.com/apple-1/"
    expected_text_header = "Apple — купить в Уфе iPhone, iPad, MacBook и аксессуары"
    default_product_page = 48
    LIMIT_25 = 25
    EXPECTED_INITIAL_COUNT = 1

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
    name_product_1_dropdown = "//*[@id='cart']/ul/li[1]/table/tbody/tr/td[2]"
    price_product_1_dropdown = "//*[@id='cart']/ul/li[1]/table/tbody/tr/td[4]"
    result_price_dropdown = "//*[@id='cart']/ul/li[2]/div/table/tbody/tr[1]/td[2]"
    total_price_dropdown = "//*[@id='cart']/ul/li[2]/div/table/tbody/tr[2]/td[2]"
    button_order = "//a[@class='btn btn-primary']"



    # Getters

    def get_header_catalog(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.header_catalog)))

    def get_header_catalog_text(self):
        return self.get_header_catalog().text

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

    def get_name_product_1_catalog_value(self):
        return self.get_name_product_1_catalog().text

    def get_price_product_1_catalog_value(self):
        return self.get_price_product_1_catalog().text

    def get_cart_value(self):
        return self.get_cart_total().text

    def get_price_product_1_dropdown(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, self.price_product_1_dropdown)))

    def get_result_price_dropdown(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, self.result_price_dropdown)))

    def get_total_price_dropdown(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, self.total_price_dropdown)))

    def get_name_product_1_dropdown(self):
        return  WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, self.name_product_1_dropdown)))

    def get_price_product_1_dropdown_value(self):
        return self.get_price_product_1_dropdown().text

    def get_result_price_dropdown_value(self):
        return self.get_result_price_dropdown().text

    def get_total_price_dropdown_value(self):
        return self.get_total_price_dropdown().text

    def get_name_product_1_dropdown_value(self):
        return self.get_name_product_1_dropdown().text

    def get_button_order(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_order)))

    def get_cart_summary_data(self):
        full_text = self.get_cart_value()
        parts = full_text.split('-')
        count = parts[0].split(' ')[0]
        price = parts[1].strip()
        return int(count),price

    # Action

    def click_button_buy_product_1(self):
        self.get_button_buy_product_1().click()
        print("Клик кнопки в корзину первого товара")

    def set_product_limit(self, count):
        self.get_input_limit().select_by_visible_text(f"{count}")
        print(f"Установлен фильтра на лимит товаров на странице кол-во {count}")

    def sort_by_price_descending(self):
        self.get_input_sort().select_by_visible_text("Цена (высокая > низкая)")
        print(f"Установлен фильтра по Цена (высокая > низкая)")

    def click_cart(self):
        self.get_cart_total().click()
        print("Открытие выпадающего списка корзины")

    def click_button_order(self):
        self.get_button_order().click()
        print("Клик на кнопку оформление заказа")
        return CartPage(self.browser)

    # Methods

    """Проверяет, отсортированы ли товары на странице по убыванию цены."""
    def is_products_sorted_by_price_descending(self):
        actual_prices = self.get_product_prices_as_numbers()
        expected_prices = sorted(actual_prices, reverse=True)

        return actual_prices == expected_prices

    """Проверка цены в выпадающем меню каталога"""
    def is_dropdown_prices_match(self, expected_price):
        product_price = self.get_price_product_1_dropdown_value()
        result_price = self.get_result_price_dropdown_value()
        total_price = self.get_total_price_dropdown_value()
        return product_price == result_price == total_price == expected_price

