
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
    expected_price_product_1 = ap.get_price_product_value()
    expected_name_product_1 = ap.get_name_product_value()




