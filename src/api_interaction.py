import requests

from src.abs_classes import WorkWithApi


class HeadHunterAPI(WorkWithApi):
    """ Класс для подключения к HH.ru """

    def __init__(self, keyword):
        """ Инициализатор """

        self.__url = "https://api.hh.ru/vacancies"
        self._params = {"text": keyword, "page": 0, "per_page": 10}
        self.__keyword = keyword
        self._vacancies_data = []

    def _connecting_to_website(self):
        """ Подключение к HH.ru """

        while self._params.get('page') != 20:
            response = requests.get(self.__url, params=self._params)

            if response.status_code == 200:
                vacancies = response.json()['items']
                self._vacancies_data.extend(vacancies)
                self._params['page'] += 1

            else:
                raise Exception(f"Ошибка подключения: {response.status_code}")

        return self._vacancies_data

    def get_vacancies(self, keyword=None):
        """ Получение данных из приватного метода """

        if keyword:
            self._params["text"] = keyword
        self._connecting_to_website()

        return self._vacancies_data
