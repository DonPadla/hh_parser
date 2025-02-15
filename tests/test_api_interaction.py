import unittest
from unittest.mock import patch, Mock

from src.api_interaction import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):

    @patch('src.api_interaction.requests.get')
    def test_connecting_to_website(self, mock_get):
        """ Тест подключения к сайту """

        mock_response = Mock()
        mock_response.json.return_value = {
            'items': [
                {"name": "developer"},
                {"name": "tester"}
            ]
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        api = HeadHunterAPI(keyword='developer')
        result = api._connecting_to_website()

        expected_result = [
                              {"name": "developer"},
                              {"name": "tester"}
                          ] * 20
        self.assertEqual(result, expected_result)

    @patch("requests.get")
    def test_empty_answer(self, mock_get):
        """ Тест пустого ответа """

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"items": [], "pages": 0}
        mock_get.return_value = mock_response
        hh_api = HeadHunterAPI("")
        hh_api._connecting_to_website()
        self.assertEqual(hh_api._vacancies_data, [])
