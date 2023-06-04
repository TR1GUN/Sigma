# //////////////////////////////////////////////////////////////////////////////////////////
#                 Главный класс запроса от которого будем наследоваться
# //////////////////////////////////////////////////////////////////////////////////////////

from Template.Template_BaseClass import IBaseClass
import requests


class ITemplateRequest(IBaseClass):
    """
    Базовый класс который работает с запросами через REQUESTS
    Наследник от Базового класса

    Содержит в себе:


    """
    # Наш ответ
    _response = None

    # Куки запроса
    _cookies_dict = None
    # Хэдерс запроса
    _headers_dict = None
    # Тип метода запроса
    _Request_method_type = ""

    # Подключаем библиотеку для работы с запросами
    __Request_methods_dict = {
        "GET": requests.get,
        "POST": requests.post,
        "PUT": requests.put,
        "DELETE": requests.delete,
    }

    def _define_method_to_request(self) -> object:
        """
        Получение метода запроса
        :return:
        """
        return self.__Request_methods_dict.get(self._Request_method_type)

    # Формируем хэдерс
    def _formation_of_the_added_headers(self, headers):
        """
        В этом методе обрабатываем формирование headers к нашему запросу
        :param headers:
        :return:
        """
        # Вытаскиваем Хэдерс
        if type(headers) is dict:
            self._headers_dict = headers
        else:
            self._headers_dict = None

    # Формируем cookies
    def _formation_of_the_added_cookies(self, cookies):
        """
        В этом методе обрабатываем формирование cookies к нашему запросу
        :param cookies:
        :return:
        """
        # Вытаскиваем Куки
        if type(cookies) is dict:
            self._cookies_dict = cookies
        else:
            self._cookies_dict = None

    def Response(self) -> requests.models.Response:
        """
        Возвращаем результат операции
        :return:
        """
        return self._response

