def test_category_init(reset_counts, first_category, second_category):

    # тестируем первую категорию
    assert first_category.name == "cool thing"
    assert first_category.description == "cool stuff"
    assert len(first_category.products.split("\n")) == 4

    # тестируем вторую категорию
    assert second_category.name == "uncool thing"
    assert second_category.description == "uncool stuff"
    assert len(second_category.products.split("\n")) == 2

    # проверяем счетчик категорий
    assert first_category.category_count == 2
    assert second_category.category_count == 2

    # проверяем счетчик товаров
    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_add_product_success(reset_counts, second_category, product):  # проверяем добавление товара
    assert second_category.product_count == 1

    second_category.add_product(product)  # добавляем товар

    assert len(second_category.products.split("\n")) == 3
    assert second_category.product_count == 2


def test_products(first_category):  # проверяем вывод списка товаров
    assert len(first_category.products.split("\n")) == 4
    assert first_category.products.split("\n")[0] == "cool soda, 100 руб. Остаток: 1 шт."
