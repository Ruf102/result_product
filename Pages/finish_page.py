from result_product.base.base_page import BasePage


class FinishPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    expected_url = "https://divizion.com/index.php?route=checkout/success"

    # Locators

    # Getters

    # Actions

    # Methods

    def finish(self):
        self.get_screen()