from unittest.mock import mock_open, patch

from src.utils import read_json_data

# тест read_json_data


@patch("os.path.join")
@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_empty_file(mock_file, mock_os_path_join):  # тест, когда файла нет
    mock_os_path_join.return_value = "fake/path/settings.json"

    # вызываем функцию и записываем результат в переменную
    result = read_json_data("settings.json")
    assert result == []


@patch("os.path.join")
@patch("builtins.open", new_callable=mock_open, read_data="not a json list")
def test_invalid_json_format(mock_file, mock_os_path_join):  # некорректный формат файла
    mock_os_path_join.return_value = "fake/path/settings.json"

    # вызываем функцию и записываем результат в переменную
    result = read_json_data("settings.json")
    assert result == []


@patch("os.path.join")
@patch("builtins.open", new_callable=mock_open, read_data='[{"transaction_id": 1}, {"transaction_id": 2}]')
def test_valid_transactions(mock_file, mock_os_path_join):
    mock_os_path_join.return_value = "fake/path/settings.json"
    expected_data = [{"transaction_id": 1}, {"transaction_id": 2}]

    # вызываем функцию и записываем результат в переменную
    result = read_json_data("settings.json")
    assert result == expected_data


@patch("os.path.join")
@patch("builtins.open")
def test_file_not_found(mock_file, mock_os_path_join):  # файл не найден
    mock_os_path_join.return_value = "fake/path/settings.json"

    # вызываем функцию и записываем результат в переменную
    result = read_json_data("settings.json")
    assert result == []


@patch("os.path.join")
@patch("builtins.open")
def test_other_file_error(mock_file, mock_os_path_join):  # любая другая ошибка
    mock_os_path_join.return_value = "fake/path/settings.json"

    # вызываем функцию и записываем результат в переменную
    result = read_json_data("settings.json")
    assert result == []
