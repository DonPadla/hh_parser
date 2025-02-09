class Vacancy:
    """ Класс, вынимающий необходимую инфориацию из вакансии """

    formated_vacancies_list = []
    __slots__ = ("__vacancies_id", "__vacancies_name", "__salary", "__vacancies_url", "__responsibility")

    def __init__(self, vacancies_id, vacancies_name, vacancies_url, responsibility, salary):
        """ Инициализатор """

        self.__vacancies_id = vacancies_id
        self.__vacancies_name = vacancies_name
        self.__salary = salary
        self.__vacancies_url = vacancies_url
        self.__responsibility = responsibility

        vacancy_dict = {
            self.__vacancies_id: {
                'name': self.__vacancies_name,
                'salary': self.__salary,
                'url': self.__vacancies_url,
                'responsibility': self.__responsibility
            }
        }
        self.formated_vacancies_list.append(vacancy_dict)

    @classmethod
    def cast_to_object_list(cls, vacancies_list):
        """ Создание списка вакансий по параметрам из общего списка """

        for vacancy in vacancies_list:
            cls(
                vacancies_id=vacancy["id"],
                vacancies_name=vacancy["name"],
                salary=cls.__has_attribute(vacancy.get("salary")),
                vacancies_url=vacancy["alternate_url"],
                responsibility=vacancy["snippet"]["responsibility"]
            )

        return cls.formated_vacancies_list

    @staticmethod
    def __has_attribute(salary):
        """ Проверка наличия зарплаты """

        if salary is None:
            return {"from": 0, "to": 0}

        else:
            from_salary = salary.get('from', 0)
            to_salary = salary.get('to', 0)
            return {"from": from_salary, "to": to_salary}

    def __gt__(self, other):
        """ Метод сравнения зарплат """

        return self.__salary["to"] > other.__salary["to"]

    @property
    def name(self):
        return self.__vacancies_name

    @property
    def url(self):
        return self.__vacancies_url

    @property
    def salary(self):
        return self.__salary

    @property
    def snippet(self):
        return self.__responsibility
