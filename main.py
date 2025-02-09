from src.json_saver import JSONSaver
from src.support import search, sorting, get_human_readable, search_in_description


def interaction():
    """ Функция для взаимодействия с пользователем """

    try:
        start = input("""Привет, с чего начнем?
                1. Поиск вакансий на HH.RU.
                2. Работа с файлом.
                """)

        if start == "1":
            search_request = input(""" Здесь можно написать все, о чем ты желаешь, а я попробую это найти :3
            """)
            search(search_request)

        elif start == "2":

            while True:
                work_with_file = input("""Поработаем с файлом. Я могу:
                1. Добавить новых вакансий.
                2. Удалить старые (если напишешь ID).
                3. Отсортировать по зарплате и показать столько выгодных вакансий, сколько пожелаешь.
                4. Найти \"ту самую\" по ключевым словам в описании.
                5. Очистить файл.
                0. Выйти.
                """)

                if work_with_file == "1":
                    search(input(""" Здесь можно написать все, о чем ты желаешь, а я попробую это найти :3
                    """))

                elif work_with_file == "2":
                    JSONSaver().get_del(int(input("Впиши сюда девятизначное число, оно же ID вакансии: """)))

                elif work_with_file == "3":
                    print(
                        get_human_readable(
                            sorting(int(input("Сколько желаешь? ")))
                        )
                    )

                elif work_with_file == "5":
                    JSONSaver().get_clear()

                elif work_with_file == "4":
                    print(
                        get_human_readable(
                            search_in_description(
                                input("Введи ключевое слово: ")
                            )
                        )
                    )

                elif work_with_file == "0":
                    break

                else:
                    print("Так не могу, давай по новой.")

        else:
            print("Не шали!")

    except ValueError:
        print("Взаимодействуй корректно!")


interaction()
