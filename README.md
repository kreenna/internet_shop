# Internet_shop

Проект по домашним заданиям для Skypro.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/kreenna/internet_shop
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd internet_shop
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```
   
## Тестирование

Функции по чтению JSON-файлов, а также функциональность созданных классов, были протестированы.

## Обработка файлов

Созданы функции для обработки файла с категориями и товарами в формате JSON и их конвертация в объекты.

Примеры использования функций:

```python
from src.utils import read_json_data, create_objects_from_json

# Пример использования read_json_data
path_json = "data/file.json"
converted_json_file = read_json_data(path_json)

# Пример использования create_objects_from_json
converted_excel_file = create_objects_from_json(converted_json_file)
```

## Классы

Были созданы классы Category и Product, в которые можно записывать полученные категории товаров и их описания, 
а также описания товаров и их стоимость. Производится счетчик всех категорий и товаров.


```

## Вклад

Если вы хотите внести свой вклад, пожалуйста, создайте форк репозитория и отправьте pull request.