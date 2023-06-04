# Здесь опишем главный класс запроса от которого будем наследоваться

# //////////////////////////////////////////////////////////////////////////////////////////
#                 Шаблон основных данных по которым отправляется запрос
# //////////////////////////////////////////////////////////////////////////////////////////

from Template.Template_BaseClass import IBaseClass
import requests


class ITemplateRequest(IBaseClass):
    """
    Базовый класс который работает с запросами через REQUESTS
    Наследник от Базового класса

    Содержит в себе:
    - Работу с URL

    """
    # Наш заголовок
    _http = 'https://'
    _result = {}
    _response = None

    _debug = False

    # Куки запроса
    _cookies_dict = None
    # Хэдерс запроса
    _headers_dict = None
    # Тип метода запроса
    _Request_method_type = ""

    # # Подключаем библиотеку для работы с запросами
    # __Request_methods_dict = {
    #     "GET": requests.get,
    #     "POST": requests.post,
    #     "PUT": requests.put,
    #     "DELETE": requests.delete,
    #                         }

    # def _method(self, method="") -> object:
    #     # self._Request = self._Request_methods_dict.get(method)
    #     # print(method)
    #     return self.__Request_methods_dict.get(method)

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

    def Result(self):
        """
        Возвращаем общий словарь результатов
        :return:
        """
        return self._result

    def GET_data(self):
        """
        Возвращаем поле дата
        :return:
        """
        return self._result.get("data")

    def GET_result_code(self):
        """
        Возвращаем результат работы
        :return:
        """
        return self._result.get("code")

    # def _url_collector(self, url):
    #     """
    #     В этом методе собираем наш URL
    #
    #     НУжен дял сборки валидного УРЛ , чтоб не выстреливать себе в ногу из-за слэшей и прочего
    #     :param url: сюда пихаем наш путь url
    #     :return: Возвращаем корректно собранный URL
    #     """
    #
    #     # Первое что делаем - определяемся из каких частей состоит наш урл
    #
    #     # UPD :
    #     # если у нас путь ровняется пустоте - выбрасываем на глагне
    #     if url is None:
    #         url = '/login'
    #
    #     # Закрытое поле - не нужно выставлять
    #     http = self._http
    #
    #     # Айпишник
    #     ip_port = self.ip_port
    #
    #     # А тут погналась свистопляска :
    #     # МЫ спустили url без начинающего первого слэша
    #     if url[0] != '/':
    #         # Собирать ничего не надо
    #         if 'http://' in url:
    #             url = url
    #         else:
    #             # Проверяем - есть ли у нас айпишник уже в записи
    #             if url[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
    #                 # Добавляем http заголовок и все
    #                 url = http + url
    #             # иначе - думаем что ссылка прсото без слэша и проверяем уже правильно ли задан айпишник
    #             else:
    #                 # Вариант 1 - задан с http заголовком
    #                 if 'http://' in ip_port:
    #                     # Вариант 1.1 - со слэшем в конце
    #                     if ip_port[-1] == '/':
    #                         url = ip_port + url
    #
    #                     # Вариант 1.2 - без слэша в конце
    #                     else:
    #                         url = ip_port + '/' + url
    #                 # Вариант 2 - задан без http заголовка
    #                 else:
    #                     # Вариант 2.1 - со слэшем в конце
    #                     if ip_port[-1] == '/':
    #                         url = http + ip_port + url
    #
    #                     # Вариант 2.2 - без слэша в конце
    #                     else:
    #                         url = http + ip_port + '/' + url
    #
    #     # Если вставили URL без слэша - Проверяем что есть в этом url
    #     else:
    #         # Проверяем - есть ли у нас айпишник уже в записи
    #         if url[1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
    #             url = http[:-1] + url
    #
    #         # Иначе считаем что с url все хорошо
    #         else:
    #             # Теперь проверяем айпишник
    #
    #             # Вариант 1 - задан с http заголовком
    #             if 'http://' in ip_port:
    #                 # Вариант 1.1 - со слэшем в конце
    #                 if ip_port[-1] == '/':
    #                     url = ip_port[:-1] + url
    #
    #                 # Вариант 1.2 - без слэша в конце
    #                 else:
    #                     url = ip_port + url
    #
    #             # Вариант 2 - задан без http заголовка
    #             else:
    #                 # Вариант 2.1 - со слэшем в конце
    #                 if ip_port[-1] == '/':
    #                     url = http + ip_port[:-1] + url
    #
    #                 # Вариант 2.2 - без слэша в конце
    #                 else:
    #                     url = http + ip_port + url
    #
    #     return url
    #
    # def get_cookies(self):
    #     """
    #     Возвращаем куки операции
    #
    #     :return:
    #     """
    #     if self._response is not None:
    #         cookies = self._response.cookies
    #     else:
    #         cookies = None
    #     return cookies
    #
    # def get_headers(self):
    #     """
    #     Возвращаем headers операции
    #
    #     :return:
    #     """
    #     if self._response is not None:
    #         headers = self._response.headers
    #     else:
    #         headers = None
    #     return headers

    def get_response(self):
        """
        Возвращаем класс ответа - необходимо может быть для отдали
        :return:
        """

        return self._response

    # _Request =_Request_methods_dict.get(method)
