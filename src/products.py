class Product:
    """Класс для описания товара, его стоимости и количества."""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product: dict, products_list: list = None):
        """Метод для добавления нового товара. Принимает словарь с данными, возвращает класс Product."""

        # проверяем корректность внесенных данных
        if list(new_product.keys()) == ["name", "description", "price", "quantity"]:
            name, description, price, quantity = new_product.values()

            # если данные корректны, проверяем нахождение товара в списке
            if products_list:
                for product in products_list:
                    if product.name == name:
                        quantity += product.quantity
                        if product.price > price:
                            price = product.price

            # возвращаем класс с данными
            return cls(name, description, price, quantity)

        else:
            # данные некорректны
            raise ValueError("Входные данные некорректны")

    @property
    def price(self) -> float:
        """Геттер для показателя приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для проверки введенной цены и ее обновления, если она выше предыдущей."""

        # проверяем, чтобы цена не была отрицательная или нулевая
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")

        else:
            # если цена положительная, проверяем, ниже ли она предыдущей
            if new_price < self.__price:

                # получаем подтверждение о снижении ценыЮ если его не дано, не меняем
                confirmation: str = input("Вы уверены, что желаете снизить цену? y/n:\n")
                if confirmation == "y":
                    self.__price = new_price

            else:
                # если новая цена выше, меняем ее
                self.__price = new_price
