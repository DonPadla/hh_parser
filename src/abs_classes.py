from abc import ABC, abstractmethod


class WorkWithApi(ABC):
    """ Абстрактный класс для работы с API """

    @abstractmethod
    def __init__(self):
        """ Абстрактный класс инициализации """

        pass

    @abstractmethod
    def _connecting_to_website(self):
        """ Абстрактный метод для подключения к сайту """

        pass


class AbsSaver(ABC):
    """ Абстрактный класс для сохранения, чтения, удаления данных """

    @abstractmethod
    def get_read(self):
        """ Абстрактный метод чтения """

        pass

    @abstractmethod
    def get_save(self):
        """ Абстрактный метод записи """

        pass

    @abstractmethod
    def get_del(self):
        """ Абстрактный метод удаления """

        pass

    @abstractmethod
    def get_add(self):
        """ Абстрактный метод сохранения """

        pass
