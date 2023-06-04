import requests
from Template.Template_BaseClass import IBaseClass


class IDecodeResponse(IBaseClass):
    """
    Базовый класс для преобразования из формата requests в формат dict
    """
    _result = {}

    # def __init__(self , Response: requests.models.Response):
    #     # Теперь расшифровываем что получили
    #     self._result = self._parse_answer(Response)

    def _parse_answer(self, answer_request: requests.models.Response) -> dict:
        """
        Здесь разбираем наш ответ в формат dict из формата requests.models.Response
        :param answer_request:
        :return: dict ответа
        """
        # Код ошибки
        self._Parse_result_code(answer_request)
        # Читаем ответ, что нам приходит
        self._Parse_text(answer_request)

        return self._result

    def _Parse_result_code(self, response: requests.models.Response):
        """
        Парсим Результат запроса

        :param response: Результат опроса - тип данных - HTTPResponse
        :return:
        """

        self._result["code"] = response.status_code

    def _Parse_JSON(self, response: requests.models.Response):
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

    def _Parse_text(self, response: requests.models.Response):
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

    def _Parse_bytte_array(self, response: requests.models.Response):
        """
        Здесь смотрим что что то у нас есть хоть что-то  в байтах
        :param response: Результат опроса - тип данных - HTTPResponse
        :return:
        """
        try:
            self._result["data"] = response.raw
        except Exception as e:
            self._result["info"] = str(e) + "\n Байтовых данных нет>"
            self._result["data"] = None

    def Result(self) -> dict:
        """
        Возвращаем результат операции
        :return:
        """
        return self._result
