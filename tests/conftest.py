import pytest

from src.received_data import Vacancy


@pytest.fixture
def list_for_test():
    return [
        {
            "117037373": {
                "name": "JUNIOR+ PYTHON DEVELOPER",
                "salary": {
                    "from": 80000,
                    "to": 150000
                },
                "url": "https://hh.ru/vacancy/117037373",
                "responsibility": "Написание Telegram-ботов, интеграции с маркетплейсами, онлайн-таблицами, ERP, сервисами доставки и интернет-магазинами. Парсинг веб-сайтов. Взаимодействие с маркетплейсами..."
            }
        },
        {
            "117031978": {
                "name": "Middle QA-инженер",
                "salary": {
                    "from": 0,
                    "to": 0
                },
                "url": "https://hh.ru/vacancy/117031978",
                "responsibility": "Коммуницировать с командой разработки. Разрабатывать тест-кейсы совместно с руководителем проекта. Вести документацию по тестированию. Составлять чек-листы по проектам. "
            }
        },
        {
            "116876598": {
                "name": "Стажер Python Developer",
                "salary": {
                    "from": 0,
                    "to": 0
                },
                "url": "https://hh.ru/vacancy/116876598",
                "responsibility": "Software Development: Design, develop, and maintain high-quality <highlighttext>Python</highlighttext> applications. - Code Review: Conduct thorough code reviews to ensure code quality..."
            }
        }
    ]


@pytest.fixture
def for_human_readable_test():
    return 'Название : JUNIOR+ PYTHON DEVELOPER\nЗарплата : 80000 - 150000\nСсылка : https://hh.ru/vacancy/117037373\nОписание : Написание Telegram-ботов, интеграции с маркетплейсами, онлайн-таблицами, ERP, сервисами доставки и интернет-магазинами. Парсинг веб-сайтов. Взаимодействие с маркетплейсами...\n\nНазвание : Middle QA-инженер\nЗарплата : 0 - 0\nСсылка : https://hh.ru/vacancy/117031978\nОписание : Коммуницировать с командой разработки. Разрабатывать тест-кейсы совместно с руководителем проекта. Вести документацию по тестированию. Составлять чек-листы по проектам. \n\nНазвание : Стажер Python Developer\nЗарплата : 0 - 0\nСсылка : https://hh.ru/vacancy/116876598\nОписание : Software Development: Design, develop, and maintain high-quality <highlighttext>Python</highlighttext> applications. - Code Review: Conduct thorough code reviews to ensure code quality...\n\n'


@pytest.fixture
def vacancy_for_test():
    return Vacancy("117037373",
                   "JUNIOR+ PYTHON DEVELOPER",
                   "https://hh.ru/vacancy/117037373",
                   "Написание Telegram-ботов, интеграции с маркетплейсами, онлайн-таблицами, ERP",
                   "0")


@pytest.fixture
def salary_none_test():
    return None


@pytest.fixture
def vacancy_with_salary():
    return Vacancy(vacancies_id="187263577",
                   vacancies_name="JUNIOR+ PYTHON DEVELOPER",
                   salary={"from": 10, "to": 20},
                   vacancies_url="https://hh.ru/vacancy/117037373",
                   responsibility="Написание Telegram-ботов, интеграции с маркетплейсами, онлайн-таблицами, ERP")


@pytest.fixture
def vacancy_wothout_salary():
    return Vacancy(vacancies_id="189724635",
                   vacancies_name="JUNIOR+ PYTHON DEVELOPER",
                   salary={"from": 0, "to": 0},
                   vacancies_url="https://hh.ru/vacancy/117037373",
                   responsibility="Написание Telegram-ботов, интеграции с маркетплейсами, онлайн-таблицами, ERP")
