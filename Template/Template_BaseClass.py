# Здесь содержится базовый класс от которого все наследуются
from Constant import code


class IBaseClass:
    """
    Базовый класс от которого все наследуем
    Содержит в себе:
    -Логгер
    """

    _code = code

    def _LOG(self,Text:str ,Type_error:[int, str]):
        """
        Метод реализует Логгер.
        Сделаем через print, чтоб не заморачиваться
        :param Text: Текст который нужно передать в логгер
        :param Type_error: Тип логирования
        :return:
        """
        # Если передан код - получаем его интопретацию
        if type(Type_error) is int:
            status = self._code.get(Type_error)

            # Страхуемся
            if type(Type_error) is None:
                status = "Undefined"
            Type_error = status

        # Создаем переменную для логирования
        text_log = "[" + str(Type_error) + "] - " + str(Text)

        # Логируем
        print(text_log)
