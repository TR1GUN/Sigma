# //////////////////////////////////////////////////////////////////////////////////////////
#                         Класс работы с методом GET
# //////////////////////////////////////////////////////////////////////////////////////////
from Template.Template_Request import ITemplateRequest


class GET(ITemplateRequest):
    """
    Класс для работы с методом - GET

    """
    # Переменная результата
    _result = {}

    # Тип запроса, который выполняем
    _Request_method_type = "GET"

    def __init__(self,
                 address_site: str,
                 url_routers: str = "",
                 data: str = "",
                 headers: dict = None,
                 cookies: dict = None):
        """
        Выполнение Метода GET

        :param address_site: адрес веб сайта
        :param url_routers: url роутера веб сайта
        :param data: данные для уточнения запроса
        :param headers: Хэдерс - ОБЬЕКТ ХЭДЕРСА
        :param cookies: Куки
        """
        # обнуляем результат
        self._result = {}

        # Запускаем наш класс запроса
        response = self._Setup(url=url)

        print("ОТВЕТ :",  response)
        # # Переносим ответ в отдельное поле
        # self._response = response
        #
        # # Теперь разбираем ответ
        # self._Parse_result_code(response=response)
        # self._Parse_JSON(response=response)
        #
        # if self._debug:
        #     print(self._result)

    # Основной метод
    def _Setup(self, url, cookies=None, headers=None):
        """
        :param url: Url запроса
        :return: Возвращает результат запроса
        """
        # Получаем функцию, что отвечает за метод
        _Request = self._define_method_to_request()



        # print(self._Request())
        # # Получаем наш адрес запроса
        # url = self._url_collector(url=url)
        # import requests

        # Запускаем
        # Если нет ни кук ни хедлесов
        if (cookies is None) and (headers is None):
            response = _Request(url = url)
        # Если есть куки
        elif (cookies is not None) and (headers is None):
            response = _Request(url, cookies=cookies)
        # Если есть хедлерс
        elif (headers is not None) and (cookies is None):
            response = _Request(url, headers=headers)
        # Если есть и то и то
        elif (cookies is not None) and (headers is not None):
            response = _Request(url, headers=headers, cookies=cookies)
        # Иначе - отправляет просто
        else:
            response = _Request(url)
        # --->

        # print(response)
        # Возвращаем данные
        return response

    def _Parse_result_code(self, response):
        """
        Парсим Результат запроса

        :param response: Результат опроса - тип данных - HTTPResponse
        :return:
        """

        self._result["code"] = response.status_code

    def _Parse_JSON(self, response):
        """
        Здесь Вытаскиваем JSON
        :param response: Результат опроса - тип данных - HTTPResponse
        :return:
        """

        try:
            self._result["data"] = response.json()

        # ЕСЛИ у нас ошибка - пытаемся вытащить текстовый файл
        except Exception as e:
            self._result["info"] = e
            self._Parse_text(response)

    def _Parse_text(self, response):
        """
        Здесь пытаемся вытащить текст
        :param response: Результат опроса - тип данных - HTTPResponse
        :return:
        """

        try:
            self._result["data"] = response.text
        except Exception as e:
            self._result["info"] = str(e) + "\n Текстовых данных нет"
            self._Parse_bytte_array(response)

    def _Parse_bytte_array(self, response):
        """
        Здесь смотрим что что то у нас есть хоть что-то  в байтах
        :param response: Результат опроса - тип данных - HTTPResponse
        :return:
        """
        try:
            self._result["data"] = response.raw
        except Exception as e:
            self._result["info"] = str(e) + "\n Байтовых данных нет>"
            self._result["data"] = False


url_Download = "https://mp3uks.ru"

url = "https://mp3uks.ru/index.php?do=search&subaction=search&story=madchild-+lawn+mower+man"
data = "do=search&subaction=search&story=madchild-+lawn+mower+man"

lol = GET(address_site=url_Download, data=data)
