import requests
from Template.Template_Decode_Response import IDecodeResponse


class DecodeResponse(IDecodeResponse):
    """
    Базовый класс для преобразования из формата requests в формат dict
    """
    _result = None

    def __init__(self , Response: requests.models.Response):
        # Теперь расшифровываем что получили
        self._result = self._parse_answer(Response)
