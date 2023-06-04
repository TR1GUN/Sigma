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
    # Код состояния
    __code = 6

    # Результат работы
    __result = {"Link_to_file": __Link_to_file, "code": __code}

    def __init__(self, name_soundtrack: str):
        """
        Что принимаем:

        :param name_soundtrack: Название саундтрека
        """

        # Делаем запрос все дела
        response_dict = self._search_soundtrack(name_soundtrack=name_soundtrack)

        # Теперь смотрим чо мы взяли
        if response_dict.get("code") == 200:
            # Ищем ссылку на скачивание
            self._parse_result(response_dict)

        # Иначе - логируем ошибку
        else:
            eror_log = "Ошибка запроса  - Информация о запросе: " + str(response_dict)
            # Ставим ее статус
            self.__code = 2
            self._LOG(Text=eror_log, Type_error=self.__code)
            self.__Link_to_file = None

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

    def _search_soundtrack(self, name_soundtrack: str) -> dict:
        """
        Ищем наш саундтрек пол названию.
        Делаем запрос, и разбираем его
        :param name_soundtrack:
        :return:
        """
        # Необходимые данные для этого:

        # Сайт и его URL
        url = self.WebSite_name
        # параметры запроса
        params = self._forming_correct_name_for_request(name_soundtrack)
        # Хедер
        headers = None
        # Куки
        cookies = None

        # Формируем наш запрос -
        from Request.Request_GET import GET

        # Делаем запрос - получаем ответ
        _Search_soundtrack_Response_RequestGET = GET(url=url, params=params, headers=headers,
                                                     cookies=cookies).Response()

        # Парсим в нужный вид
        from Adapter.Decode_Response import DecodeResponse

        response_dict = DecodeResponse(Response=_Search_soundtrack_Response_RequestGET).Result()

        return response_dict

    def _parse_result(self, response_dict):
        """
        Здесь парсим наш файл в поисках ссылки
        :param response_dict:
        :return:
        """
        from Adapter.Parser import Parser
        Text = Parser(text=response_dict["data"])

        # Определяем элементы
        element = "a"
        class_element = "track-dl"
        filed = "href"
        Link_to_file = Text.Find_element(element=element, class_element=class_element, filed=filed)
        # Если все спарсилось, то кайфуем

        if Link_to_file:
            self.__Link_to_file = Link_to_file
            self.__code = 6
            # Иначе - логируем
        else:
            eror_log = "Ошибка парсинга данных  - Информация о запросе: " + str(response_dict)
            # Ставим ее статус
            self.__code = 2
            self._LOG(Text=eror_log, Type_error=self.__code)
            self.__Link_to_file = None

    # # Попробуем рефлексию
    # def __call__(self):
    #     return [self.__code, self.__Link_to_file]
