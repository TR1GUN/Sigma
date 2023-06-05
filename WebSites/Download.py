# Здесь опишем класс, чтоб работать с сайтом скачки
from Template.Template_BaseClass import IBaseClass


class DownloadSiteNameMP3UKS(IBaseClass):
    """
    В Этом классе работаем с сайтом https://mp3uks.ru/

    Нам необходимо на этом сайте:
    -Найти файл
    -Скачать файл
    """
    # Само имя сайта с которого скачиваем
    WebSite_name = "https://mp3uks.ru/"
    # Файл, что скачали
    __File = b""
    # Линкуем сам файл
    __Link_to_file = ""
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
        # Пункт второй - скачиванием файл, если все хорошо
        if self.__code == 6:
            self.__File = self._Download_file(link_to_file=link_to_file)
        else:
            self.__File = b""

    def _Download_file(self, link_to_file):
        """
        В этом методе выполняем: Скачивание файла по ссылке
        :param link_to_file:
        :return:
        """
        from Service.Download.Download_WebSite import WebsiteDownloadMP3UKS

        # Ищем ссылку
        Link_to_file, self.__code = WebsiteDownloadMP3UKS(link_soundtrack=link_to_file)

        return Link_to_file

    def _Search_soundtrack(self, name_soundtrack):
        """
        В этом методе выполняем: Поиск нужного трека
        :param name_soundtrack:
        :return:
        """
        from Service.Download.Search_WebSite import WebsiteSearchMP3UKS

        # Ищем ссылку
        Link_to_file, self.__code = WebsiteSearchMP3UKS(name_soundtrack=name_soundtrack)

        return Link_to_file

    # Плохо, но почему бы и нет
    def __call__(self):

        return self.__File, self.__code

    # def Result(self):
    #     """
    #     Получаем результат деятельности
    #     :return:
    #     """
    #     return {"File": self.__File, "code": self.__code}