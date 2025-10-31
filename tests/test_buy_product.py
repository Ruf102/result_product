from result_product.Pages.main_page import MainPage
from result_product.Pages.apple_page import ApplePage


def test_by_google_pixel(browser):
    mp = MainPage(browser)
    mp.open_catalog_apple()

    ap = ApplePage(browser)
    ap.buy_product_1()