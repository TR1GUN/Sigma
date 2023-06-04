from Template.Template_BaseClass import IBaseClass


class WebsiteDownloadMP3UKS(IBaseClass):
    """
    Класс работы со скачиванием
    """
    # Само имя сайта с которого скачиваем
    WebSite_name = "https://mp3uks.ru"
    # Параметр поиска
    _search_param = "index.php?do=search&subaction=search&story="

    # Файл, что скачали
    __File = b""
    # Код состояния
    __code = 6

    # Результат работы
    __result = {"Link_to_file": __File, "code": __code}

    def __init__(self, link_soundtrack: str):
        """
        Что принимаем:

        :param link_soundtrack: ссылка на скачивание
        """

        # Делаем запрос все дела
        response_dict = self._Download_mp3_file(link_soundtrack=link_soundtrack)
        # Теперь смотрим чо мы взяли

        print(response_dict)

        if response_dict.get("code") == 200:
            # Ищем ссылку на скачивание
            print(response_dict)

        # Иначе - логируем ошибку
        else:
            eror_log = "Ошибка запроса  - Информация о запросе: " + str(response_dict)
            # Ставим ее статус
            self.__code = 2
            self._LOG(Text=eror_log, Type_error=self.__code)
            self.__Link_to_file = None

    def _forming_correct_link_to_download_for_request(self, link: str) -> str:
        """
        Формируем правильное название ссылки для скачивания
        :param link: Само название, в форме которую может читать человек
        :return: название для параметра запроса
        """
        # Формируем наш параметр поиска
        link_to_download = self.WebSite_name + link
        return link_to_download

    def _Download_mp3_file(self, link_soundtrack: str) -> dict:
        """
        Скачиваем файл
        :return:
        """

        # Необходимые данные для этого:

        # Сайт и его URL
        url = self._forming_correct_link_to_download_for_request(link=link_soundtrack)
        # параметры запроса
        data = None
        # Хедер
        headers = None
        # Куки
        cookies = None

        # Формируем наш запрос -
        from Request.Request_POST import POST

        # Делаем запрос - получаем ответ
        _Download_soundtrack_Response_RequestPOST = POST(url=url, data=data, headers=headers,
                                                         cookies=cookies).Response()

        # Парсим в нужный вид
        from Adapter.Decode_Response import DecodeResponseFile

        response_dict = DecodeResponseFile(Response=_Download_soundtrack_Response_RequestPOST).Result()

        return response_dict

    def _Read_Binary_file(self, answer_to_site):
        """
        В этом методе
        :param answer_to_site:
        :return:
        """

    # def __call__(self):
    #
    #     # Лезем в рефлексию - не очень хорошо
    #     return {"File": self.__File, "code": self.__code}


link_soundtrack = "/dl.php?3uo-Wv6kd48ZhrGm98EPjcnJWUTM8LfpRvwMNvc9acYmmUv8E62dRQe-lXkwh7UbZ7IBHmTMeKYcPZ6Qm9SGvCzOdqnnL8U1PsrWcRCHjNLwaKMUa2nc82NXyEaVqj4bDmIikux9VBBz_bbYUYxLyH1VAl50i5dcCUL3F9sWIMhnY_erRQ8NZ_MOAZJvvyYcw5hIRSx45l0VW153ADF65GM7DnDdTmCuTogzp_67K2ww-DP-rjIs3oFA91ekgBiNi0pIPedF9WquKUnmV-r6pq-Ah58_r-7tBC0pCyRPJOOuNvh2Z2O_UwhhqCuZkCz-ug9VB-DXqkvNZQu0w9oBLg==.mp3"
WebsiteDownloadMP3UKS(link_soundtrack=link_soundtrack)
