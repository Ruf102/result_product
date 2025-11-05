from result_product.Pages.main_page import MainPage


def test_smoke_buy_product(browser):
    mp = MainPage(browser)

    # --- Навигация до каталога с товарами apple
    ap =  mp.maps_to_apple_catalog()

    # --- Проверка корректности URL в каталоге apple
    assert ap.get_current_url() == ap.expected_url, \
        f"ОШИБКА URL: ожидался '{ap.expected_url}', получен '{ap.get_current_url()}'"
    print(f"УСПЕХ: URL '{ap.get_current_url()}' корректен.")


    # --- Проверка корректности заголовка в каталоге apple
    assert ap.get_header_catalog_text() == ap.expected_text_header, \
        f"ОШИБКА В HEADERS: ОР: {ap.expected_text_header}, ФР: {ap.get_header_catalog_text()}"
    print(f"УСПЕХ: Заголовок '{ap.expected_text_header}' корректен.")

    # --- Проверка фильтра по количеству отображения товаров на странице
    assert ap.get_count_product() == ap.default_product_page, \
        f"Количество товаров на странице ОР: 48 != ФР: {ap.get_count_product()} !"
    print(f"УСПЕХ: По умолчанию количество товаров на странице {ap.get_count_product()}")

    # --- Проверка установленного лимита отображение товаров на странице
    ap.set_product_limit(25)

    assert ap.get_count_product() == ap.LIMIT_25, \
        f"Количество товаров на странице ОР: 25 != ФР: {ap.get_count_product()} !"
    print(f"УСПЕХ: Количество товаров на странице {ap.get_count_product()}")

    #  --- Проверка сортировке товаров по убыванию цены.
    ap.sort_by_price_descending()

    assert ap.is_products_sorted_by_price_descending(), \
        f"Сортировка по убыванию НЕ СРАБОТАЛА!"
    print(f"УСПЕХ: Сортировка по цене отработала корректно")

    # --- Проверка добавления товара в корзину
    expected_price_product_1 = ap.get_price_product_1_catalog_value()
    expected_name_product_1 = ap.get_name_product_1_catalog_value()
    ap.click_button_buy_product_1()
    actual_count, actual_price = ap.get_cart_summary_data()

    assert ap.EXPECTED_INITIAL_COUNT == actual_count, \
        f"ОШИБКА КОЛИЧЕСТВА: На кнопке корзины ОР: {ap.EXPECTED_INITIAL_COUNT}, ФР: {actual_count}"
    print(f"УСПЕХ: Количество товаров на кнопке корзины совпадает с ОР")

    assert expected_price_product_1 == actual_price, \
        f"ОШИБКА ЦЕНЫ: На кнопке корзины ОР: {expected_price_product_1}, ФР: {actual_price}"
    print(f"УСПЕХ: Цена товара на кнопке корзины совпадает с ОР")

    # --- Проверка цены в drop-down cart
    ap.click_cart()

    assert expected_name_product_1 == ap.get_name_product_1_dropdown_value(), \
        f"Название товара не совпадает в dropdown ОР: {expected_price_product_1}, ФР: {ap.get_name_product_1_dropdown_value()}"
    print("УСПЕХ: название товара в выпадающем меню корзины совпадают с ОР")

    assert ap.is_dropdown_prices_match(expected_price_product_1), \
        "Цены в выпадающем меню корзины не совпадают с ОР"
    print("УСПЕХ: цены в выпадающем меню корзины совпадают с ОР")

    # --- Переход на страницу оформления заказа (корзина)
    cp = ap.click_button_order()

    # --- Проверка URL на странице корзины
    assert cp.get_current_url() == cp.expected_url, \
        f"ОШИБКА URL: ожидался '{cp.expected_url}', получен '{cp.get_current_url()}'"
    print(f"УСПЕХ: URL '{cp.get_current_url()}' корректен.")

    # --- Проверка заголовка на странице корзины
    assert cp.get_header_value() == cp.expected_text_header, \
        f"ОШИБКА В HEADERS: ОР: {cp.expected_text_header}, ФР: {cp.get_header_value()}"
    print(f"УСПЕХ: Заголовок '{cp.get_header_value()}' корректен.")

    # --- Проверка названия товара добавленного в заказ
    assert expected_name_product_1 == cp.get_name_product_order_value(), \
        f"Название товара не совпадает с ОР: {expected_name_product_1}, ФР: {cp.get_name_product_order_value()}"
    print(f"УСПЕХ: Название товара совпадает с ОР: {expected_name_product_1}, ФР: {cp.get_name_product_order_value()}")

    # --- Проверка цены в корзине
    assert cp.is_cart_prices_match(expected_price_product_1), \
        "Цена товара в корзине совпадает с ценой в каталоге"
    print("УСПЕХ: Цены товаров в корзине совпадают с ценой товара в каталоге")


    # --- Заполнение обязательных полей, и оформление заказа
    fp = cp.complete_order()
    fp.wait_for_url(fp.expected_url)

    # --- Проверка URL на финальной странице
    assert fp.get_current_url() == fp.expected_url, \
        f"URL завершения заказа не совпадает с ОР: {fp.expected_url}, ФР: {fp.get_current_url()}"
    print(f"УСПЕХ: URL на финальной странице '{fp.get_current_url()}' корректен.")

    fp.finish()







