
from JSON_Backend_framework.Service.TemplateRequest import TemplateRequest


# //////////////////////////////////////////////////////////////////////////////////////////
#                 Шаблон работы с методом POST
# //////////////////////////////////////////////////////////////////////////////////////////


class POST(TemplateRequest):
    """
    Класс Метода POST

    """
    # Переменная результата
    _result = {}

    def __init__(self, url: str, data: str, cookies=None, headers=None, ip_device=None):

        # обнуляем результат
        self._result = {}
        # Если изменен айпишник - то задаем его тоже
        if ip_device is not None:
            self.ip_port = str(ip_device)

        # Вытаскиваем Хэдерс
        if headers:
            try:
                _headers_dict = headers.Get_headers()
            except Exception as e :
                print("Exception :", e)
                _headers_dict = None
        else:
            _headers_dict = None

        # Вытаскиваем Куки
        if cookies:

            try:
                _cookie = cookies.Get_cookie()
            except Exception as e:
                print("Exception :", e)
                _cookie = None
        else:
            _cookie = None

        # Запускаем наш класс запроса
        response = self._Setup(url=url, data=data, cookies=_cookie, headers=_headers_dict)

        # Переносим ответ в отдельное поле
        self._response = response
        # Теперь разбираем ответ
        self._Parse_result_code(response=response)
        self._Parse_JSON(response=response)

        if self._debug:
            print(self._result)

    def _Setup(self, url, data, cookies=None, headers=None):
        """
        Делаем сам запрос

        :param url: Url запроса
        :param data: JSON - формат строка
        :param cookies: Куки - если есть
        :param headers:  Хеадресс - если есть
        :return: Возвращает результат запроса
        """

        import requests
        # print(url)

        # Получаем наш адрес запроса
        url = self._url_collector(url=url)

        # Запускаем

        # ЕСли нет ни кук ни хедлесов
        if (cookies is None) and (headers is None):

            response = requests.post(url, data=data)
        # Если есть куки но нет хэдерса
        elif (cookies is not None) and (headers is None) :

            response = requests.post(url, data=data, cookies=cookies)
        # Если есть хедлерс
        elif (headers is not None) and (cookies is None) :

            response = requests.post(url, data=data, headers=headers)
        # Если есть и то и то

        elif (cookies is not None) and (headers is not None):

            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        # Иначе - отправляет просто
        else:
            response = requests.post(url, data=data)
        # --->
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
        import json
        try:
            self._result["data"] = response.json()

        # ЕСЛИ у нас ошибка - пытаемся вытащить текстовый файл
        except json.JSONDecodeError:
            self._Parse_text(response)
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



