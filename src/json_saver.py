import json
from pathlib import Path

from src.abs_classes import AbsSaver


class JSONSaver(AbsSaver):
    """ Kласс для сохранения, чтения, удаления данных """

    def __init__(self, filename="vacancies.json"):
        """ Инициализация экземпляра JSONSaver """

        project_root = Path(__file__).resolve().parent.parent
        self.__filename = project_root / "data" / filename

        if not self.__filename.parent.exists():
            self.__filename.parent.mkdir(parents=True, exist_ok=True)

        if not self.__filename.exists():
            self.__filename.write_text("[]", encoding="utf8")

    def get_read(self):
        """ Метод чтения данных """

        try:
            with open(self.__filename, encoding="utf8") as file:
                to_python_file = json.load(file)

                return to_python_file

        except Exception:

            return []

    def get_add(self, vacancies_data):
        """ Метод записи данных """

        python_file = self.get_read()
        for vacancies in vacancies_data:

            if vacancies not in python_file:
                python_file.extend(vacancies_data)

            else:
                continue

        self.get_save(python_file)

        return python_file

    def get_del(self, vacancies_id):
        """ Метод удаления данных """

        python_file = self.get_read()

        try:
            for vacancies in python_file:
                if vacancies_id in vacancies:
                    python_file.remove(vacancies)
            self.get_save(python_file)

        except KeyError:
            print("Указанный ID не найден")

    def get_save(self, python_file):
        """ Метод сохранения данных в файл """

        with open(self.__filename, "w", encoding="utf8") as file:
            json.dump(python_file, file, ensure_ascii=False, indent=4)

    def get_clear(self, ):
        """ Метод для очистки файла """

        with open(self.__filename, "w"):
            pass
