import requests
from Template.Template_Decode_Response import IDecodeResponse


class DecodeResponse(IDecodeResponse):
    """
    Базовый класс для преобразования из формата requests в формат dict
    """
    _result = {}

    def __init__(self, Response: requests.models.Response):
        self._result = {}
        # Теперь расшифровываем что получили
        self._parse_answer(Response)


class DecodeResponseFile(IDecodeResponse):
    """
    Скачиваем файл
    """
    _result = {}

    def __init__(self, Response: requests.models.Response):
        self._result = {}
        # Теперь расшифровываем что получили
        self._parse_answer(Response)

    def _parse_answer(self, answer_request: requests.models.Response) -> dict:
        """
        Здесь разбираем наш ответ в формат dict из формата requests.models.Response
        :param answer_request:
        :return: dict ответа
        """
        # Код ошибки
        self._Parse_result_code(answer_request)
        # Читаем ответ, что нам приходит
        self._Parse_bytte_array(answer_request)

    def _Parse_bytte_array(self, response: requests.models.Response):
        """
        Здесь смотрим что, то у нас есть хоть что-то в байтах
        :param response: Результат опроса - тип данных - HTTPResponse
        :return:
        """
        try:
            self._result["data"] = response.content
        except Exception as e:
            self._result["info"] = str(e) + "\n Байтовых данных нет>"
            self._result["data"] = None