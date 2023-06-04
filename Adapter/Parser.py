# Здесь разместим наши парсеры
from bs4 import BeautifulSoup


class Parser:
    """
    Класс парсера

    сделал на основе BeautifulSoup

    Имеет функционал:

    - Поиск Первого элемента
    - Поиск всех элементов
    """
    _file_to_parse = None

    def __init__(self, text):
        self._Load_file_to_parse(text=text)

    def _Load_file_to_parse(self, text: str):
        """
        Здесь мы загружаем наши данные для парсинга
        :param text:
        :return:
        """
        self._file_to_parse = BeautifulSoup(text, 'html.parser')

    def Find_element(self, element: str, class_element: str) -> str:
        """
        Здесь происходит поиск ОДНОГО элемента
        :param element:
        :param class_element:
        :return:
        """

        parse_string = self._file_to_parse.find(element, class_=class_element).text

        return parse_string

    def Find_all_elements(self, element: str, class_element: str) -> list:
        """
        Здесь происходит поиск всех Элементов
        :param element:
        :param class_element:
        :return:
        """

        parse_list = self._file_to_parse.find_all(element, class_=class_element)

        parse_string_list = [parse.text for parse in parse_list]

        return parse_string_list
