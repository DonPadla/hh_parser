import json
import unittest
from unittest.mock import patch, mock_open
from src.json_saver import JSONSaver


class TestJSONSaver(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    def test_get_add(self, mock_file):
        """ Тест записи в файл """

        json_saver = JSONSaver('test_file.json')  # Укажите имя файла в конструкторе
        vacancy = [{"name": "developer"}, {"name": "tester"}]
        json_saver.get_add(vacancy)
        self.assertEqual(mock_file.call_count, 2)

    @patch('builtins.open', new_callable=mock_open, read_data='[{"name": "developer"}, {"name": "tester"}]')
    def test_get_read(self, mock_file):
        """ Тест чтения """

        json_saver = JSONSaver('test_file.json')
        result = json_saver.get_read()
        mock_file.assert_called_once_with(json_saver._JSONSaver__filename, encoding='utf8')
        expected_data = [{"name": "developer"}, {"name": "tester"}]
        self.assertEqual(result, expected_data)

    @patch('builtins.open', new_callable=mock_open,
           read_data='[{"123123123": {"name": "developer"}}, {"234234234": {"name": "tester"}}]')
    def test_get_del(self, mock_file):
        """ Тест удаления данных """

        json_saver = JSONSaver('test_file.json')
        result = json_saver.get_del("123123123")
        expected_data = [{'234234234': {'name': 'tester'}}]
        self.assertEqual(result, expected_data)

        self.assertEqual(mock_file.call_count, 2)
