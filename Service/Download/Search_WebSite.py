from Template.Template_BaseClass import IBaseClass


# Хорошо бы создать класс шаблон - WebsiteSearch
class WebsiteSearchMP3UKS(IBaseClass):
    """
    Класс для работы c поиском нужного трека на сайте https://mp3uks.ru/
    """

    # Само имя сайта с которого скачиваем
    WebSite_name = "https://mp3uks.ru/"
    # Параметр поиска
    _search_param = "index.php?do=search&subaction=search&story="

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
        Формируем правильное название трека в форме, которая кушает запрос.
        :param name_soundtrack: Само название, в форме которую может читать человек
        :return: название для параметра запроса
        """
        # Формируем наш параметр поиска
        search_param = self._search_param + name_soundtrack.replace(" ", "+")
        return search_param

    def _search_soundtrack(self, search_param):
        """
        Ищем наш саундтрек пол названию
        :param name_soundtrack: - Название саундтрека
        :return:
        """
        # Формируем наш запрос -
        from Request.Request_GET import GET

        # Необходимые данные для этого:

        # Сайт и его URL
        url = self.WebSite_name
        # параметры запроса
        params = search_param
        # Хедер
        headers = None
        # Куки
        cookies = None

        # Делаем запрос - получаем ответ
        _Search_soundtrack_Response_RequestGET = GET(url=url, params=params,headers=headers, cookies=cookies).Response()

        # Парсим в нужный вид
        from Adapter.Decode_Response import DecodeResponse

        response_dict = DecodeResponse(Response=_Search_soundtrack_Response_RequestGET).Result()

        # Теперь смотрим чо мы взяли
        if response_dict.get("code") == 200 :
            # Ищем ссылку на скачивание

            self.__Link_to_file =
