

class Category:
    name: str
    description: str
    products: list
    category_amount: int = 0
    product_amount: int = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_amount += 1
        Category.product_amount += len(products) if products else 0