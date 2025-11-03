from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from result_product.Pages.apple_page import ApplePage
from result_product.base.base_page import BasePage


class MainPage(BasePage):

    base_url = "https://divizion.com/"

    def __init__(self, browser):
        super().__init__(browser)

    # Locators
    menu_catalog = "//*[@class='dropdown dropcats']/a[normalize-space(text())='Каталог товаров']"
    apple_catalog = "//*[@class='dropdown dropcats']//a[normalize-space(text())='Apple']"


    # Getters
    def get_menu_catalog(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu_catalog)))

    def get_apple_catalog(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.apple_catalog)))


    # Actions
    def action_menu_catalog(self):
        action_chains = ActionChains(self.browser)
        action_chains.move_to_element(self.get_menu_catalog()).perform()
        print("Курсор наведен на меню каталога")

    def click_phone_catalog(self):
        self.get_apple_catalog().click()
        print("Нажатие кнопки Apple")

    # Metgods
    def maps_to_apple_catalog(self):
        self.browser.get(self.base_url)
        self.browser.maximize_window()
        self.action_menu_catalog()
        self.click_phone_catalog()
        return ApplePage(self.browser)