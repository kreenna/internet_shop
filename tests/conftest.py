import pytest

from src.categories import Category, ProductInterator
from src.products import Product


@pytest.fixture()
def product():
    return Product(name="thing", description="some random thing", price=10.0, quantity=1)


@pytest.fixture()
def product2():
    return Product(name="not thing", description="some random not thing", price=100.0, quantity=3)


@pytest.fixture(autouse=True)
def reset_counts():
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


@pytest.fixture()
def product_iterator(first_category):
    return ProductInterator(first_category)
