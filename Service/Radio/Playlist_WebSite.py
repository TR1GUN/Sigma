from Template.Template_BaseClass import IBaseClass


# Хорошо бы создать класс шаблон - WebsiteSearch
class WebsitePlaylistRadioPotok(IBaseClass):
    """
    Класс для работы c поиском нужного плейлиста на сайте https://radiopotok.ru/
    """

    # Само имя сайта с которого скачиваем
    WebSite_name = "https://radiopotok.ru/api/radio/"
    # Параметр поиска
    _search_param = "tracks?id="

    # Плейлист
    __Playlist = []
    # Код состояния
    __code = 6

    # Результат работы
    __result = {"Playlist": __Playlist, "code": __code}

    def __init__(self, ID_radio: str):
        """
        Что принимаем:

        :param ID_radio: Название радиостанции
        """

        # Делаем запрос все дела
        response_dict = self._search_playlist(ID_radio=ID_radio)

        # Теперь смотрим чо мы взяли
        if response_dict.get("code") == 200:
            # Ищем ссылку на скачивание
            self._parse_result(response_dict)
            self.__code = 6

        # Иначе - логируем ошибку
        else:
            eror_log = "Ошибка запроса  - Информация о запросе: " + str(response_dict)
            # Ставим ее статус
            self.__code = 2
            self._LOG(Text=eror_log, Type_error=self.__code)
            self.__Link_to_file = None

    # Формируем правильное название
    def _forming_correct_name_for_request(self, ID_radio: str) -> str:
        """
        Формируем правильное название в форме, которая кушает запрос.
        :param ID_radio: ID радио
        :return: название для параметра запроса
        """
        # Формируем наш параметр поиска
        search_param = self._search_param + str(ID_radio)
        return search_param

    def _search_playlist(self, ID_radio: str) -> dict:
        """
        Ищем наш плейлист по радио.
        Делаем запрос, и разбираем его
        :param ID_radio:
        :return:
        """
        # Необходимые данные для этого:

        # Сайт и его URL
        url = self.WebSite_name
        # параметры запроса
        params = self._forming_correct_name_for_request(ID_radio)
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
        Здесь парсим наш файл в поисках всего плейлиста
        :param response_dict:
        :return:
        """
        from Adapter.Parser import Parser
        Text = Parser(text=response_dict["data"])

        # Определяем элементы
        element = "td"
        class_element = "font-medium w-full leading-tight js--radio-playlist-track"
        # filed = "href"
        Playlist_list = Text.Find_all_elements(element=element, class_element=class_element)
        # Если все спарсилось, то кайфуем

        if Playlist_list:
            self.__Playlist = Playlist_list
            self.__code = 6
            # Иначе - логируем
        else:
            eror_log = "Ошибка парсинга данных  - Информация о запросе: " + str(response_dict)
            # Ставим ее статус
            self.__code = 2
            self._LOG(Text=eror_log, Type_error=self.__code)
            self.__Playlist = []

    # Попробуем рефлексию
    def __call__(self):
        return self.__Playlist, self.__code

    # def Result(self):
    #     return self.__Playlist, self.__code