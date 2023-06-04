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


