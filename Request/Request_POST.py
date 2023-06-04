# //////////////////////////////////////////////////////////////////////////////////////////
#                         Класс работы с методом POST
# //////////////////////////////////////////////////////////////////////////////////////////
from Template.Template_Request import ITemplateRequest
import requests


class POST(ITemplateRequest):
    """
    Класс для работы с методом - POST
    """
    # Переменная результата
    _result = {}

    # Тип запроса, который выполняем
    _Request_method_type = "POST"

    # Куки запроса
    _cookies_dict = None
    # Хэдерс запроса
    _headers_dict = None

    def __init__(self,
                 url: str,
                 data: dict = None,
                 headers: dict = None,
                 cookies: dict = None):
        """
        Выполнение Метода POST

        :param url: адрес веб сайта
        :param data: данные для уточнения запроса
        :param headers: Хэдерс - ОБЬЕКТ ХЭДЕРСА
        :param cookies: Куки
        """
        # обнуляем результат
        self._response = None

        # Оформляем хэдерсы
        self._formation_of_the_added_headers(headers=headers)
        # Оформляем куки
        self._formation_of_the_added_cookies(cookies=cookies)

        # Запускаем наш класс запроса
        self._response = self._Setup(url=url, data=data)

    def _Setup(self, url, data) -> requests.models.Response:
        """
        Делаем сам запрос

        :param url: Url запроса
        :param data: JSON - формат строка
        :return:  результат запроса
        """
        # # Получаем функцию, что отвечает за метод
        # _Request = self._define_method_to_request()

        # ЕСли нет ни кук ни хедлесов
        if (self._cookies_dict is None) and (self._headers_dict is None):

            response = requests.post(url, data=data)
        # Если есть куки но нет хэдерса
        elif (self._cookies_dict is not None) and (self._headers_dict is None):

            response = requests.post(url, data=data, cookies=self._cookies_dict)
        # Если есть хедлерс
        elif (self._headers_dict is not None) and (self._cookies_dict is None):

            response = requests.post(url, data=data, headers=self._headers_dict)
        # Если есть и то и то

        elif (self._cookies_dict is not None) and (self._headers_dict is not None):

            response = requests.post(url, data=data, headers=self._headers_dict, cookies=self._cookies_dict)
        # Иначе - отправляет просто
        else:
            response = requests.post(url, data=data)

        # Возвращаем данные
        return response
