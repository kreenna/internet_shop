from unittest.mock import patch

import pytest

from src.products import Product


def test_product_init(product):  # проверяем, что данные корректно вносятся
    assert product.name == "thing"
    assert product.description == "some random thing"
    assert product.price == 10.0
    assert product.quantity == 1


def test_new_product_success(product):  # проверяем, что метод работает корректно
    product_dict = {"name": "thing", "description": "some random thing", "price": 10.0, "quantity": 3}
    product_list = [
        Product(name="thing", description="some random thing", price=10.0, quantity=1),
        Product(name="not thing", description="some random thing", price=10.0, quantity=1),
    ]

    result_no_list = Product.new_product(product_dict)

    # тестируем без наличия списка с товарами
    assert result_no_list.name == "thing"
    assert result_no_list.description == "some random thing"
    assert result_no_list.price == 10.0
    assert result_no_list.quantity == 3

    result_list = Product.new_product(product_dict, product_list)

    # тестируем с наличием списка с товарами
    assert result_list.name == "thing"
    assert result_list.description == "some random thing"
    assert result_list.price == 10.0
    assert result_list.quantity == 4


def test_new_product_fail():  # проверяем, что при некорректных данных возникает ошибка
    product_dict = {"description": "some random thing", "price": 10.0, "quantity": 3}
    with pytest.raises(ValueError):
        Product.new_product(product_dict)


def test_price_setter_success(product):  # успешный тест изменения цены
    product.price = 20.0
    assert product.price == 20.0


def test_price_setter_negative(capsys, product):  # сообщение об ошибке при вводе отрицательной цены
    product.price = -10.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_price_setter_zero(capsys, product):  # сообщение об ошибке при вводе цены 0
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_price_change_confirm(product):  # подтверждение смены цены
    with patch("builtins.input", return_value="y"):
        product.price = 1
    assert product.price == 1.0


def test_price_change_deny(product):  # изменения не были подтверждены
    with patch("builtins.input", return_value="n"):
        product.price = 1
    assert product.price == 10.0
