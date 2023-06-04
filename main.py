# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                               Мастер класс  от которого наследуемся
#                            Здесь будут задействованы основные запросы
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------


#
# class TemplateRequest:
#     """
#     Мастер класс от которого наследуемся
#     Здесь будут задействованы основные запросы
#
#     """
#
#     # куки
#     _cookies = None
#
#     # Сам айпишник железки
#     _ip_address = '192.168.0.1'
#
#     # Путь url
#     _path_url = ''
#
#     # Клиент - Нужен для Хедерса
#     _user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
#     # Страница с которой зашли - иногда нужно
#     _Referer = 'http://192.168.0.1/login'
#
#     # хедерс - Иногда нужен
#     _headers = {
#         'User-Agent': _user_agent,
#         'Referer': 'http://192.168.0.1/login',
#         'Host': '192.168.0.1',
#         # 'Connection': keep-alive
#         'Accept': '*/*',
#         'Content-type': 'application/json',
#         'Origin': 'http://192.168.0.1',
#         # 'Cookie': 'sessionid=16349148992619061200'
#     }
#
#     # КОД Операции
#     _result_code = None
#     _data = None
#
#     def _parser_request(self, response):
#         """
#         Считываем нужные данные
#         :param response:
#         :return: Возвращаем response_dict
#         """
#         # Код операции
#         self._result_code = response.GET_result_code()
#         # Текстовые данные, если есть
#         self._data = response.GET_data()
#         # куки
#         cookies = response.get_cookies()
#         # headers
#         headers = response.get_headers()
#         # Общий словарь данных
#         response_dict = response.Result()
#
#         return response_dict
#
#     def _request_POST(self, JSON: str):
#         """
#         Использование Метода POST
#
#         :param JSON:
#         :return:
#         """
#         from JSON_Backend_framework.Service.Request_POST import POST
#
#         # Первое - удаляем все пробелы из строки JSON
#         JSON = JSON.replace(" ", '')
#         # Делаем запрос - получаем ответ - возвращаем
#         response = POST(url=self._path_url,
#                         data=JSON,
#                         cookies=self._cookies,
#                         headers=self._headers,
#                         ip_device=self._ip_address)
#         # Получаем :
#         # --->
#         response_dict = self._parser_request(response=response)
#         # --->
#         return response_dict
#
#     def _request_GET(self):
#         """
#         Использование Метода GET
#
#         :return:
#         """
#         from JSON_Backend_framework.Service.Request_GET import GET
#
#         # Первое - удаляем все пробелы из строки JSON
#         # JSON = JSON.replace(" ", '')
#         # Делаем запрос - получаем ответ - возвращаем
#
#         response = GET(url=self._path_url,
#                        cookies=self._cookies,
#                        headers=self._headers,
#                        ip_device=self._ip_address)
#         # Получаем :
#         # --->
#         response_dict = self._parser_request(response=response)
#         # --->
#         return response_dict
#
#     def _request_PUT(self, JSON: str):
#         """
#         Использование Метода PUT
#
#         :param JSON:
#         :return:
#         """
#         from JSON_Backend_framework.Service.Request_PUT import PUT
#
#         # Первое - удаляем все пробелы из строки JSON
#         JSON = JSON.replace(" ", '')
#         # Делаем запрос - получаем ответ - возвращаем
#
#         response = PUT(url=self._path_url, data=JSON, cookies=self._cookies, headers=self._headers,
#                        ip_device=self._ip_address)
#         # Получаем :
#         # --->
#         response_dict = self._parser_request(response=response)
#         # --->
#         return response_dict
#
#     def _request_DELETE(self, JSON: str = ''):
#         """
#         Использование Метода DELETE
#
#         :param JSON:
#         :return:
#         """
#         from JSON_Backend_framework.Service.Request_DELETE import DELETE
#
#         # Первое - удаляем все пробелы из строки JSON
#         JSON = JSON.replace(" ", '')
#         # Делаем запрос - получаем ответ - возвращаем
#         response = DELETE(url=self._path_url, data=JSON, cookies=self._cookies, headers=self._headers,
#                           ip_device=self._ip_address)
#         # Получаем :
#         # --->
#         response_dict = self._parser_request(response=response)
#         # --->
#         return response_dict


from  requests import request, get, post, put, delete


url1 = "https://radiopotok.ru/"


# Идентификатор группы

# <script>
#         STATIONS[1543]
# Весь плейлист
url =  "https://radiopotok.ru/api/radio/tracks?id=1543"
lol = get(url=url1)

print(lol)
# url_Download = "https://mp3uks.ru"
#
# url = "https://mp3uks.ru/index.php?do=search&subaction=search&story=madchild-+lawn+mower+man"
# data = "do=search&subaction=search&story=madchild-+lawn+mower+man"
#
# # В ответе -  track-dl - ссыка на скачивание файла
# # <div class="track-time">02:36</div>
# # 	<a class="track-dl" href="/dl.php?3uo-Wv6kd48ZhrGm98EPjcnJWUTM8LfpRvwMNvc9acYmmUv8E62dRQe-k0sKk4QICIY2IGTTe-4XQ7KptZaavTjPRoXJLNo1CLrQFDaJiuzwRLsESXbSqQ4VzyHqkTkNW3khzs5DUhJnrbTITqpKvxowOUx0z7w4dnL2B994JspJScbwUiIVEM1wBM9joCJ6rLRkRjxq_Qd6T2xlAFtJ9Rg7B1rODU-xc5wqpNu7Lgozxh2KlHw1h7tE_yXf-SuZuV5XPoxPwA6pKX-eCKLsio20nOkBr-7tBC0pCyRPJOOuNvh2Z2O_UwhhqCuZkCz-ug9VB-DXqkvNZQu0w9oBLg==.mp3" title="Скачать трек" download><span class="fas fa-arrow-alt-to-bottom"></span></a>
# # 	<a class="__adv_purchase" href="#"><span class="__adv_list_track-icon"></span></a>
# # 	<div class="mgf"></div>
#
# url_ = url_Download + "/dl.php?3uo-Wv6kd48ZhrGm98EPjcnJWUTM8LfpRvwMNvc9acYmmUv8E62dRQe-k0sKk4QICIY2IGTTe-4XQ7KptZaavTjPRoXJLNo1CLrQFDaJiuzwRLsESXbSqQ4VzyHqkTkNW3khzs5DUhJnrbTITqpKvxowOUx0z7w4dnL2B994JspJScbwUiIVEM1wBM9joCJ6rLRkRjxq_Qd6T2xlAFtJ9Rg7B1rODU-xc5wqpNu7Lgozxh2KlHw1h7tE_yXf-SuZuV5XPoxPwA6pKX-eCKLsio20nOkBr-7tBC0pCyRPJOOuNvh2Z2O_UwhhqCuZkCz-ug9VB-DXqkvNZQu0w9oBLg==.mp3"
# lol = get(url=url_)
# print(lol.text)
#
# class Action():
#     """
#     Главный класс действий
#
#     """

# {радиостанции:[], ЗА сколько суток собирать: количество ,  только уникальные : True}

# Читаем все радиостанции
#
# Получаем ID нужных радиостанций
#
# Получае список треков по времени
#
# Компануем это все в плейлист
#
# Пытаемся скачать все это
#
# Выдаем скаченную подборку



#
# url_Download = "https://mp3uks.ru"
#
# url = "https://mp3uks.ru/index.php?do=search&subaction=search&story=madchild-+lawn+mower+man"
# data = "do=search&subaction=search&story=madchild-+lawn+mower+man"
#
# lol = GET(url=url_Download, params=data)
