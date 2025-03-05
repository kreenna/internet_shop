import pytest

from src.categories import Category
from src.products import Product


@pytest.fixture(autouse=True)
def reset_category_count():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture()
def first_category():
    result = Category(
        name="cool thing",
        description="cool stuff",
        products=[
            Product(name="cool soda", description="very cool soda", price=100.0, quantity=1),
            Product(name="cool hoop", description="very cool hoop", price=100.0, quantity=1),
            Product(name="cool drink", description="very cool drink", price=100.0, quantity=1),
        ],
    )
    yield result


@pytest.fixture()
def second_category():
    result = Category(
        name="uncool thing",
        description="uncool stuff",
        products=[
            Product(name="uncool ball", description="very uncool ball", price=100.0, quantity=2),
        ],
    )
    yield result


def test_category_init(reset_category_count, first_category, second_category):

    # тестируем первую категорию
    assert first_category.name == "cool thing"
    assert first_category.description == "cool stuff"
    assert len(first_category.products) == 3

    # тестируем вторую категорию
    assert second_category.name == "uncool thing"
    assert second_category.description == "uncool stuff"
    assert len(second_category.products) == 1

    # проверяем счетчик категорий
    assert first_category.category_count == 2
    assert second_category.category_count == 2

    # проверяем счетчик товаров
    assert first_category.product_count == 4
    assert second_category.product_count == 4
