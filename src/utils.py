import json
import os

from config import PATH_HOME

from src.categories import Category
from src.products import Product


def read_json_data(path_file: str) -> list:
    """
    Принимает путь до JSON-файла с информацией и продуктах.
    Читает файл и возвращает его содержимое.
    Возвращает пустой список, если файл некорректный.
    """

    # пробуем открыть файл
    try:
        with open(os.path.join(PATH_HOME, path_file), "r", encoding="utf-8") as file:
            converted_data: list = json.load(file)

    except Exception:  # любые ошибки с файлом
        # при возникновении ошибки, возвращаем пустой словарь.
        return []

    else:
        return converted_data


def create_objects_from_json(data: list) -> list:
    """
    Принимает список категорий товаров, их описания, цены и количества.
    Перебирает содержимое и инициализирует его в соответствующие классы.
    Возвращает список категорий и товаров в них.
    """

    categories: list = []
    for category in data:
        products: list = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
