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

class SearchAdapter():
    """
    Главный клас который отвечает за
    """

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


from bs4 import BeautifulSoup

# # Скачивание
# url_Download = "https://mp3uks.ru"
#
# url = "https://mp3uks.ru/index.php?do=search&subaction=search&story=madchild-+lawn+mower+man"
# data = "do=search&subaction=search&story=madchild-+lawn+mower+man"
#
# lol = GET(url=url_Download, params=data).Result()
#
# print(lol["data"])
#
#
#
#
# soup = BeautifulSoup(lol["data"],'html.parser')
#
# # song_title = soup.find('h1',class_='track-dl').text
#
#
# # < a class ="track-dl" href="/dl.php?3uo-Wv6kd48ZhrGm98EPjcnJWUTM8LfpRvwMNvc9acYmmUv8E62dRQe-lXkwh7UbZ7IBHmTMeKYcPZ6Qm9SGvCzOdqnnL8U1PsrWcRCHjNLwaKMUa2nc82NXyEaVqj4bDmIikux9VBBz_bbYUYxLyH1VAl50i5dcCUL3F9sWIMhnY_erRQ8NZ_MOAZJvvyYcw5hIRSx45l0VW153ADF65GM7DnDdTmCuTogzp_67K2ww-DP-rjIs3oFA91ekgBiNi0pIPedF9WquKUnmV-r6pq-Ah58_r-7tBC0pCyRPJOOuNvh2Z2O_UwhhqCuZkCz-ug9VB-DXqkvNZQu0w9oBLg==.mp3" title="Скачать трек" download > < span class ="fas fa-arrow-alt-to-bottom" > < / span > < / a >
#
# string = soup.find(name="a", attrs = {"class":"track-dl"})
# print(string)
#
# print(string.get("href"), type(string.get("href")))
#
#
# # Скачивать - ПОСТ
# # page-ref: https://mp3uks.ru/index.php?do=search


# # Получение всех всех радио
#
#
# url = "https://radiopotok.ru"
# # data = "do=search&subaction=search&story=madchild-+lawn+mower+man"
#
# # хедерс
#
# headers = {}
# lol = GET(url=url).Result()
#
# print(lol["data"])



# Получение трек листа радио


url = "https://radiopotok.ru/api/radio/tracks?id=1543"
# data = "tracks?id=1543"

# хедерс



headers = {
"Accept" :"text/plain, */*; q=0.01",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "ru,ru-RU;",
"Cookie": "cf_clearance=hRtkJYOor2kdmH.9oGLljP5vHS4LCuYFMcd0BykCx_w-1685906163-0-160; _ym_uid=1685906166287565822; _ym_d=1685906166; _ym_isad=2; tmr_lvid=56fcab46a65c9d11a3e06b1ecbd86b31; tmr_lvidTS=1685906165960; __cf_bm=B39T7S4f29TGvllrlEPcqFTfuNOKTu0PcmHl415T3A4-1685906434-0-AYANbIZeXrHuxnMr3GZE5JPqzOlRBBoP3fWYFxAv5iwkcVOOMNS+PlANC8/jDOAm3vmwYWnkkX303z5XJvzH1i5pccT86k1lUKqVV5Rgwf7X; tmr_detect=0%7C1685906435490",
"Referer": "https://radiopotok.ru/radio/1543",
"Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
"Sec-Ch-Ua-Mobile": "?0",
"Sec-Ch-Ua-Platform": "Windows",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site":"same-origin",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
"X-Requested-With": "XMLHttpRequest"
}


lol = GET(url=url, headers=headers).Result()

print(lol["data"])