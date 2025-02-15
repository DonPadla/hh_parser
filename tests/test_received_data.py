from src.received_data import Vacancy
from tests.conftest import salary_none_test


def test_vacancy_init(vacancy_for_test):
    assert vacancy_for_test.name == "JUNIOR+ PYTHON DEVELOPER"
    assert vacancy_for_test.salary == "0"
    assert vacancy_for_test.url == "https://hh.ru/vacancy/117037373"
    assert vacancy_for_test.snippet == "Написание Telegram-ботов, интеграции с маркетплейсами, онлайн-таблицами, ERP"


def test_has_attribute(salary_none_test):
    result = Vacancy._Vacancy__has_attribute(salary_none_test)
    assert result == {"from": 0, "to": 0}


def test_gt(vacancy_with_salary, vacancy_wothout_salary):
    assert vacancy_with_salary > vacancy_wothout_salary
