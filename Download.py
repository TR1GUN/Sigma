# Здесь опишем класс, чтоб работать с сайтом скачки
from Template.Template_BaseClass import IBaseClass


class SiteNameMP3UKS(IBaseClass):
    """
    В Этом классе работаем с сайтом https://mp3uks.ru/

    Нам необходимо на этом сайте:
    -Найти файл
    -Скачать файл
    """

    # Файл, что скачали
    __File = b""
    # Результат работы
    __result = ""
    # Код состояния
    __code = 6

    def __init__(self, name_soundtrack: str):
        """
        Что принимаем:
        :param name_soundtrack: название песени
        """

        # Пункт первый - Ищем нашу ссылку на файл для скачивания
        link_to_file = self._Search_soundtrack(name_soundtrack=name_soundtrack)
        # Пункт второй - скачиванием файл
        self.__result = self._Download_file(link_to_file=link_to_file)

    def _Download_file(self, link_to_file):
        """
        В этом методе выполняем: Скачивание файла по ссылке
        :param link_to_file:
        :return:
        """
        #
        return {"File": self.__File, "code": self.__code}

    def _Search_soundtrack(self, name_soundtrack):
        """
        В этом методе выполняем: Поиск нужного трека
        :param name_soundtrack:
        :return:
        """
        #
        return {"File": self.__File, "code": self.__code}


class WebsiteSearch(IBaseClass):
    """
    Класс для работы c поиском нужного трека
    """
    #
    # Файл, что скачали
    __File = b""
    # Код состояния
    _code = 6

    # def __init__(self, link_soundtrack: str):
    #     """
    #     Что принимаем:
    #
    #     :param Sound_list: Список из названий. песен
    #     """

    def __call__(self):
        # Лезем в рефлексию - не очень хорошо
        return {"File": self.__File, "code": self._code}


class WebsiteSearchMP3UKS(WebsiteSearch):
    """
    Класс для работы c поиском нужного трека на сайте https://mp3uks.ru/
    """

    # Код состояния
    _code = 6

    def __init__(self, name_soundtrack: str):
        """
        Что принимаем:

        :param name_soundtrack: Название саундтрека
        """

    def _search_soundtrack(self, name_soundtrack):
        """
        Ищем наш саундтрек пол названию
        :param name_soundtrack: - Название саундтрека
        :return:
        """
        # Формируем наш запрос -


class WebsiteDownload(IBaseClass):
    """
    Класс работы со скачиванием
    """
    #
    # Файл, что скачали
    __File = b""
    # Код состояния
    __code = 6

    def __init__(self, link_soundtrack: str):
        """
        Что принимаем:

        :param Sound_list: Список из названий. песен
        """

    def _Download_mp3_file(self):

        #
        data = ""
        #

        # Провеляем что что то  получили
        if data:

            # формируем файл
            mp3_File = b""

            return mp3_File

        else:
            # Логируем, что не скачали
            error = "Не удалось скачать файл - "
            self._LOG(Text=error, Type_error=2)

            return None

    def _Read_Binary_file(self, answer_to_site):
        """
        В этом методе
        :param answer_to_site:
        :return:
        """

    def __call__(self):

        # Лезем в рефлексию - не очень хорошо
        return {"File": self.__File, "code": self.__code}



