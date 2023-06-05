# //////////////////////////////////////////////////////////////////////////////////////////
#                         Класс работы с методом GET
# //////////////////////////////////////////////////////////////////////////////////////////
from Template.Template_Request import ITemplateRequest
import requests


class GET(ITemplateRequest):
    """
    Класс для работы с методом - GET
    """
    # Переменная результата
    _response = {}

    # Тип запроса, который выполняем
    _Request_method_type = "GET"

    # Куки запроса
    _cookies_dict = None
    # Хэдерс запроса
    _headers_dict = None

    def __init__(self,
                 url : str,
                 params: str = "",
                 headers: dict = None,
                 cookies: dict = None):
        """
        Выполнение Метода GET

        :param url: адрес веб сайта
        :param params: данные для уточнения запроса
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
        self._response = self._Setup(url=url, params=params)

    # Основной метод
    def _Setup(self, url, params) -> requests.models.Response:
        """
        Функция для отправления GET запроса
        :param url:
        :param params:
        :return:
        """
        # # Получаем функцию, что отвечает за метод
        # _Request = self._define_method_to_request()

        # Если нет ни кук ни хедлесов
        if (self._cookies_dict is None) and (self._headers_dict is None):
            response = requests.get(url=url, params=params)
        # Если есть куки
        elif (self._cookies_dict is not None) and (self._headers_dict is None):
            response = requests.get(url, params=params, cookies=self._cookies_dict)
        # Если есть хедлерс
        elif (self._headers_dict is not None) and (self._cookies_dict is None):
            response = requests.get(url, params=params, headers=self._headers_dict)
        # Если есть и то и то
        elif (self._cookies_dict is not None) and (self._headers_dict is not None):
            response = requests.get(url, params=params, headers=self._headers_dict, cookies=self._cookies_dict)
        # Иначе - отправляет просто
        else:
            response = requests.get(url, params=params)
        # --->

        # Возвращаем данные
        return response
