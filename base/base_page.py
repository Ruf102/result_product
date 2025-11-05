from datetime import datetime

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    """Возвращает текущий URL"""
    def get_current_url(self):
        return self.browser.current_url
        # assert url == result_url, f"Адрес {url} не совпадает с {result_url}"
        # print("Адрес совпадает")

    """Метод создания скриншота"""
    def get_screen(self):
        now_date = datetime.now().strftime("%d.%m.%Y_%H-%M-%S")
        name_screen = "screen" + now_date + ".png"
        self.browser.save_screenshot(f"result_product\\Screen\\{name_screen}")

    """Метод ожидания загрузки страницы"""
    def wait_for_url(self, expected_url):
        WebDriverWait(self.browser, 10).until(EC.url_to_be(expected_url))
