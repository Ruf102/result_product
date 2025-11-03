

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    """Возвращает текущий URL"""
    def get_current_url(self):
        return self.browser.current_url
        # assert url == result_url, f"Адрес {url} не совпадает с {result_url}"
        # print("Адрес совпадает")

    # """Метод проверки текста"""
    # def verification_word(self, result_word, word):
    #     value_word = result_word.text
    #     assert  value_word == word, f"ОР: {value_word} != ФР: {word}"
    #     print(f"ОР: {value_word} == ФР: {word}")

    """Метод получения текста из веб-элемента"""
    def get_text(self, element):
        return element.text

