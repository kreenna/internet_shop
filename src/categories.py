from typing import Optional

from src.products import Product


class Category:
    """Класс для описания категорий товаров."""

    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[list] = None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product):
        """Метод для добавления нового товара."""
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1

    @property
    def products(self):
        """Геттер для показателя приватного атрибута списка товаров, их цены и остатка."""
        all_products: str = ""
        for product in self.__products:
            all_products += f"{product.name}, {int(product.price)} руб. Остаток: {product.quantity} шт.\n"

        return all_products
