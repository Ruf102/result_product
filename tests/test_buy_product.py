import time

from trio import fail_after

from result_product.Pages.main_page import MainPage
from result_product.Pages.apple_page import ApplePage


def test_smoke_by_product(browser):
    mp = MainPage(browser)

    # --- Навигация до каталога с товарами apple

    ap =  mp.maps_to_apple_catalog()

    # --- Проверка корректности URL в каталоге apple

    expected_url = "https://divizion.com/apple-1/"
    actual_url = ap.get_current_url()
    assert actual_url == expected_url, \
        f"ОШИБКА URL: ожидался '{expected_url}', получен '{actual_url}'"

    # --- Проверка корректности заголовка в каталоге apple

    expected_text_header = "Apple — купить в Уфе iPhone, iPad, MacBook и аксессуары"
    actual_header_text = ap.get_header_catalog_text()
    assert actual_header_text == expected_text_header, \
        f"ОШИБКА В HEADERS: ОР: {expected_text_header}, ФР: {actual_header_text}"
    print(f"УСПЕХ: Заголовок '{expected_text_header}' корректен.")

    # --- Проверка фильтра по количеству отображения товаров на странице

    count_product_in_page = ap.get_count_product()
    assert count_product_in_page == 48, \
        f"Количество товаров на странице ОР: 48 != ФР: {count_product_in_page} !"
    print(f"УСПЕХ: По умолчанию количество товаров на странице {count_product_in_page}")

    # установка лимита 25 отображения товаров на старице
    ap.select_drop_down_limit(25)
    count_product_in_page = ap.get_count_product()
    assert count_product_in_page == 25, \
        f"Количество товаров на странице ОР: 25 != ФР: {count_product_in_page} !"
    print(f"УСПЕХ: Количество товаров на странице {count_product_in_page}")

    #  --- Проверка фильтра по цене

    ap.select_drop_down_sort("Цена (высокая > низкая)")
    actual_prices = ap.get_product_prices_as_numbers()
    expected_prices = sorted(actual_prices, reverse=True)
    assert actual_prices == expected_prices, \
        f"Сортировка по убыванию НЕ СРАБОТАЛА! Ожидалось: {expected_prices}, Получено: {actual_prices}"
    print(f"УСПЕХ: Сортировка по цене отработала корректно")

    # Проверка добавления товара в корзину
    expected_price_product_1 = ap.get_price_product_1_catalog_value()
    expected_name_product_1 = ap.get_name_product_1_catalog_value()
    expected_count = f"1 товар(ов) - {expected_price_product_1}"
    ap.click_button_buy_product_1()

    cart_button_text = ap.get_cart_value()
    assert expected_count in cart_button_text and expected_price_product_1 in cart_button_text, \
        "Не найдены и количество, и цена на кнопке перехода в корзину"
    print("УСПЕХ: Цена товара в каталоге и на кнопке перехода в корзину совпадают")

    # Проверка цены в drop-down cart
    ap.click_cart()

    assert expected_name_product_1 == ap.get_name_product_1_dropdown_value(), \
        f"Название товара не совпадает в dropdown ОР: {expected_url}, ФР: {ap.get_name_product_1_dropdown_value()}"

    assert ap.get_price_product_1_dropdown_value() == \
           ap.get_result_price_dropdown_value() == \
           ap.get_total_price_dropdown_value() == \
           expected_price_product_1, (f"Цены не совпадают: "
                                    f"Товар: {ap.get_price_product_1_dropdown_value()}, "
                                    f"Итого: {ap.get_result_price_dropdown_value()}, "
                                    f"Кнопка: {ap.get_total_price_dropdown_value()}, "
                                    f"Ожидаемая: {expected_price_product_1}")
    print("Цены в выпадающем меню корзины совпадают")

    cp = ap.click_button_order()

    expected_url = "https://divizion.com/simplecheckout/"
    actual_url = cp.get_current_url()
    assert actual_url == expected_url, \
        f"ОШИБКА URL: ожидался '{expected_url}', получен '{actual_url}'"

    expected_text_header = "Оформление заказа"
    actual_header_text = cp.get_header_value()
    assert actual_header_text == expected_text_header, \
        f"ОШИБКА В HEADERS: ОР: {expected_text_header}, ФР: {actual_header_text}"
    print(f"УСПЕХ: Заголовок '{expected_text_header}' корректен.")

    assert expected_name_product_1 == cp.get_name_product_order_value(), \
        f"Название товара не совпадает с ОР: {expected_price_product_1}, ФР: {cp.get_name_product_order_value()}"

    assert expected_price_product_1 == \
           cp.get_price_product_order_value() == \
           cp.get_price_product_result_order_value() == \
           cp.get_price_cart_total_value()

    cp.complete_order()
    time.sleep(5)







