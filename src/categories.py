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

    def __str__(self):
        """Метод для вывода информации о категории и количестве товаров в ней."""
        products_total = 0
        for item in self.__products:
            products_total += item.quantity
        return f"{self.name}, количество продуктов: {products_total} шт."

    def add_product(self, product: Product):
        """Метод для добавления нового товара."""
        if isinstance(product, Product):
            self.product_count += 1
            self.__products.append(product)

    @property
    def products(self):
        """Геттер для показателя приватного атрибута списка товаров, их цены и остатка."""
        all_products: str = ""
        for one in self.__products:
            all_products += f"{str(one)}\n"

        return all_products


class ProductInterator:

    category: Category

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.category.product_count:
            product = self.category.products.split("\n")[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
