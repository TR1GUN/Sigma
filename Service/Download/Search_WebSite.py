from Template.Template_BaseClass import IBaseClass


# Хорошо бы создать класс шаблон - WebsiteSearch
class WebsiteSearchMP3UKS(IBaseClass):
    """
    Класс для работы c поиском нужного трека на сайте https://mp3uks.ru/
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

        :param name_soundtrack: Название саундтрека
        """

    # Формируем правильное название
    def _forming_correct_name_for_request(self, name_soundtrack: str) -> str:
        """
        Формируем правильное название трека в форме которая кушает запрос
        :param name_soundtrack: Само название, в форме которую может читать человек
        :return: название для параметра запроса
        """

        return name_soundtrack.replace(" ", "+")

    def _search_soundtrack(self, name_soundtrack):
        """
        Ищем наш саундтрек пол названию
        :param name_soundtrack: - Название саундтрека
        :return:
        """
        # Формируем наш запрос -
