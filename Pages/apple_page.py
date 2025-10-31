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
    button_buy_product_1 = "(//*[normalize-space(text())='В корзину'])[1]"
    name_product_1_catalog = "(//div[@class='caption']//h4/a)[1]"
    price_product_1_catalog = "(//*[@class='price '])[1]"
    elements_for_page = "//*[@class='product-thumb']"
    input_limit = "//*[@id='input-limit']"

    # Getters
    def get_count_elements(self):
        element = self.browser.find_elements(By.XPATH, self.elements_for_page)
        return len(element)

    def get_button_buy_product_1(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_buy_product_1)))

    def get_name_product_1_catalog(self):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, self.name_product_1_catalog)))

    def get_price_product_1_catalog(self):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, self.price_product_1_catalog)))

    def get_input_limit(self):
        return Select(WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_limit))))

    # Action
    def click_button_buy_product_1(self):
        self.get_button_buy_product_1().click()
        print("Нажатие кнопки в корзину первого товара")

    def check_display_limit(self):
        assert self.get_count_elements() == 48, f"На странице отображается {self.get_count_elements()} вместо 48 товаров"
        print("Отображается 48 товаров на странице")

    def select_drop_down(self):
        self.get_input_limit().select_by_visible_text("25")
    # Methods

    def buy_product_1(self):
        print(self.get_text(self.get_input_limit()))
        print(self.get_text(self.get_price_product_1_catalog()))
        print(self.get_text(self.get_name_product_1_catalog()))
        self.click_button_buy_product_1()