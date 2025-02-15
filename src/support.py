from src.api_interaction import HeadHunterAPI
from src.json_saver import JSONSaver
from src.received_data import Vacancy


def search(search_request: str) -> None:
    """ Вспомогательная функция для поиска вакансий """

    saver = JSONSaver()
    data_v = (Vacancy.cast_to_object_list(HeadHunterAPI(search_request).get_vacancies()))
    saver.get_add(data_v)
    print("Все, что удалось найти, бережно помещено в \"vacancies.json\" в папке \"data\".")


def sorting(count: int) -> list[dict]:
    """ Вспомогательная функция для сортировки и вывода топ n """

    data = JSONSaver().get_read()
    sorted_key = lambda x: list(x.values())[0].get("salary", {}).get("from", 0) or 0
    sorted_data = sorted(data, key=sorted_key, reverse=True)
    top = sorted_data[:count]

    return top


def get_human_readable(data: list[dict]) -> str:
    """ Перевод списка словарей в читаемый вид """

    human_readable = ""

    for element in data:
        vacancy_data = list(element.values())[0]
        human_readable += f"""Название : {vacancy_data["name"]}
Зарплата : {vacancy_data["salary"]["from"]} - {vacancy_data["salary"]["to"]}
Ссылка : {vacancy_data["url"]}
Описание : {vacancy_data["responsibility"]}\n\n"""

    return human_readable


def search_in_description(keyword: str) -> list[dict]:
    """ Вспомогательная функция для поиска по кдючевому слову """

    search_list = []
    data = JSONSaver().get_read()
    keyword = keyword.lower()

    for element in data:
        vacancy_data = list(element.values())[0]
        responsibility = (vacancy_data.get("responsibility", "") or "").lower()

        if keyword in responsibility:
            search_list.append(element)

    if len(search_list) == 0:
        print("Возможно, \"та самая\" еще не создана")

    return search_list
