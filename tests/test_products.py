import pytest

from src.products import Product


@pytest.fixture()
def product():
    return Product(name="thing", description="some random thing", price=10.0, quantity=1)


def test_product_init(product):
    assert product.name == "thing"
    assert product.description == "some random thing"
    assert product.price == 10.0
    assert product.quantity == 1
