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


# url = "https://radiopotok.ru/api/radio/tracks?id=1543"
# # data = "tracks?id=1543"
#
# # хедерс
#
#
#
# headers = {
# "Accept" :"text/plain, */*; q=0.01",
# "Accept-Encoding": "gzip, deflate, br",
# "Accept-Language": "ru,ru-RU;",
# "Cookie": "cf_clearance=hRtkJYOor2kdmH.9oGLljP5vHS4LCuYFMcd0BykCx_w-1685906163-0-160; _ym_uid=1685906166287565822; _ym_d=1685906166; _ym_isad=2; tmr_lvid=56fcab46a65c9d11a3e06b1ecbd86b31; tmr_lvidTS=1685906165960; __cf_bm=B39T7S4f29TGvllrlEPcqFTfuNOKTu0PcmHl415T3A4-1685906434-0-AYANbIZeXrHuxnMr3GZE5JPqzOlRBBoP3fWYFxAv5iwkcVOOMNS+PlANC8/jDOAm3vmwYWnkkX303z5XJvzH1i5pccT86k1lUKqVV5Rgwf7X; tmr_detect=0%7C1685906435490",
# "Referer": "https://radiopotok.ru/radio/1543",
# "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
# "Sec-Ch-Ua-Mobile": "?0",
# "Sec-Ch-Ua-Platform": "Windows",
# "Sec-Fetch-Dest": "empty",
# "Sec-Fetch-Mode": "cors",
# "Sec-Fetch-Site":"same-origin",
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
# "X-Requested-With": "XMLHttpRequest"
# }
#
#
# lol = GET(url=url, headers=headers).Result()
#
# print(lol["data"])

# ПОИСК всего плейлиста
plalist = """<tr>
    <td>00:17</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Артур Руденко и Виктория Алешко - Виктория-вестница</td>
</tr><tr>
    <td>00:12</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Евгений Кемеровский - Нас разделяет материк</td>
</tr><tr>
    <td>00:08</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Сергей Наговицын - Зима на Черноморском</td>
</tr><tr>
    <td>23:55</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Виктор Третьяков - Первоклассница</td>
</tr><tr>
    <td>23:51</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Владислав Медяник - Бродяга</td>
</tr><tr>
    <td>23:45</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Стас Михайлов - Приказ</td>
</tr><tr>
    <td>23:42</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Афина - Дикое танго</td>
</tr><tr>
    <td>23:21</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Ля-Минор - Мадера</td>
</tr><tr>
    <td>23:13</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Игорь Аравский - Пластинка юности моей</td>
</tr><tr>
    <td>23:00</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Сергей Любавин - Счастье в долгу у несчастья</td>
</tr><tr>
    <td>22:51</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Джанго - Босая осень</td>
</tr><tr>
    <td>22:34</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Елена Ваенга - Письмо</td>
</tr><tr>
    <td>22:30</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Александр Новиков - Чертовка</td>
</tr><tr>
    <td>22:27</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Андрей Косинский - Корюшка</td>
</tr><tr>
    <td>22:08</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Шуфутинский - Ты от меня далеко (2017)</td>
</tr><tr>
    <td>22:01</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Круг - Это было вчера</td>
</tr><tr>
    <td>22:00</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Брендон Стоун - Правда без лица</td>
</tr><tr>
    <td>21:54</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Март Бабаян - Женщина в белом</td>
</tr><tr>
    <td>21:29</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Стас Михайлов - Я буду очень тебя беречь</td>
</tr><tr>
    <td>21:05</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Анатолий Полотно и Федя Карманов - Славные денёчки</td>
</tr><tr>
    <td>21:02</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Владимир Высоцкий - Лирическая</td>
</tr><tr>
    <td>21:00</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Алена Ланская - Наше счастье одно на двоих</td>
</tr><tr>
    <td>20:54</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Дюмин Александр - Зараза, брось</td>
</tr><tr>
    <td>20:41</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Артем Дёмин - Зажигай</td>
</tr><tr>
    <td>20:35</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Шуфутинский - Гитарушка</td>
</tr><tr>
    <td>20:31</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Задорин - Это не любовь</td>
</tr><tr>
    <td>20:27</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Бумер - Озоновый слой</td>
</tr><tr>
    <td>20:23</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Артур Руденко и Виктория Алешко - Виктория-вестница</td>
</tr><tr>
    <td>20:16</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Бурляш - Гетера</td>
</tr><tr>
    <td>20:11</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Сергей Трофимов - Ностальгия</td>
</tr><tr>
    <td>20:07</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Настасья Самбурская - Саша</td>
</tr><tr>
    <td>20:03</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Лесоповал - Седьмая струна</td>
</tr><tr>
    <td>19:40</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Виталий Аксёнов - Ждёт она меня</td>
</tr><tr>
    <td>19:27</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Анатолий Полотно и Федя Карманов - Цветная Азия</td>
</tr><tr>
    <td>19:21</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Андрей Бандера - Голуби</td>
</tr><tr>
    <td>19:15</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Александр Маршал - Мы вернёмся домой</td>
</tr><tr>
    <td>19:07</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Катерина Голицына - Прости</td>
</tr><tr>
    <td>19:03</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Иван Кучин - Багульник</td>
</tr><tr>
    <td>18:51</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Граф Гагарин - 3 режима</td>
</tr><tr>
    <td>18:41</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Брендон Стоун - Папа</td>
</tr><tr>
    <td>18:38</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Круг - Браво</td>
</tr><tr>
    <td>18:34</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Екатерина Семёнова - Школьница</td>
</tr><tr>
    <td>18:31</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Владимир Ждамиров и Сергей Завьялов - Ой денёк</td>
</tr><tr>
    <td>18:24</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Шуфутинский - Love story</td>
</tr><tr>
    <td>18:21</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Юта - Любимый мой</td>
</tr><tr>
    <td>18:16</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Чиж & Co - Вот пуля просвистела</td>
</tr><tr>
    <td>18:12</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Любовь Успенская - Горький вкус бузины</td>
</tr><tr>
    <td>18:07</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Дмитрий Волгин и группа Хорошая Песня - Ночка</td>
</tr><tr>
    <td>18:00</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Руслан Алехно - Виноват, прости</td>
</tr><tr>
    <td>17:55</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Валерий Курас - Самолётик</td>
</tr><tr>
    <td>17:47</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Афина - Душа кричит</td>
</tr><tr>
    <td>17:43</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Сергей Любавин и Настя Николь - Любовь устало по секрету</td>
</tr><tr>
    <td>17:34</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Владимир и Воровайки - Тополя-предатели</td>
</tr><tr>
    <td>17:31</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Сентябрь - Волшебный рай</td>
</tr><tr>
    <td>17:27</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Татьяна Буланова - Играю в прятки на судьбу</td>
</tr><tr>
    <td>17:20</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Елена Ваенга - Больно</td>
</tr><tr>
    <td>17:11</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Владислав Медяник - Тяжело седому пацану</td>
</tr><tr>
    <td>17:03</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Лесоповал - От всей души (Держитесь на поверхности, ребята)</td>
</tr><tr>
    <td>17:00</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Александр Иванов - Забытая</td>
</tr><tr>
    <td>16:54</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Владимир Высоцкий - Песня о друге</td>
</tr><tr>
    <td>16:52</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Александр Абдулов и Семён Фарада - Уно моменто</td>
</tr><tr>
    <td>16:45</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Зара - У любви свои законы</td>
</tr><tr>
    <td>16:41</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Сергей Трофимов - ЧБ</td>
</tr><tr>
    <td>16:37</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Григорий Лепс - Натали</td>
</tr><tr>
    <td>16:27</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Александр Новиков - Ананасы в шампанском</td>
</tr><tr>
    <td>16:23</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Николай Расторгуев - Возвращение</td>
</tr><tr>
    <td>16:12</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Виктор Королев - На белой карете</td>
</tr><tr>
    <td>16:03</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Анатолий Полотно и Федя Карманов - Рыбацкие байки</td>
</tr><tr>
    <td>16:00</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">ВИА Волга-Волга - Поручни любви</td>
</tr><tr>
    <td>15:54</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Виталий Аксенов - Сочи</td>
</tr><tr>
    <td>15:50</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Евгений Кемеровский - Вот и здравствуй</td>
</tr><tr>
    <td>15:42</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Стас Ярушин - Я не могу тебя ждать</td>
</tr><tr>
    <td>15:34</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Афина - День рождения</td>
</tr><tr>
    <td>15:22</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Рада Рай - Радуюсь</td>
</tr><tr>
    <td>15:14</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Сергей Куренков - Лучик</td>
</tr><tr>
    <td>15:05</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Ирина Аллегрова - С днем рождения</td>
</tr><tr>
    <td>14:55</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Елена Ваенга - Ягода</td>
</tr><tr>
    <td>14:47</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Любовь Успенская - Дорогами</td>
</tr><tr>
    <td>14:43</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Алёна Петровская и Евгений Росс - Донская бравада</td>
</tr><tr>
    <td>14:35</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Катя Огонек - До свидания (Уезжаю)</td>
</tr><tr>
    <td>14:21</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Владислав Медяник - Звездочка</td>
</tr><tr>
    <td>14:15</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Григорий Лепс - Не троньте душу грязными руками</td>
</tr><tr>
    <td>14:03</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Александр Розенбаум - Лето в садоводстве</td>
</tr><tr>
    <td>14:00</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Артур Руденко и Виктория Алешко - Виктория-вестница</td>
</tr><tr>
    <td>13:46</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Антиреспект - Разбитый телефон</td>
</tr><tr>
    <td>13:42</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Ирина Круг - Ты моя вселенная</td>
</tr><tr>
    <td>13:27</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Афина - Дикое танго</td>
</tr><tr>
    <td>13:23</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Стас Михайлов - Детство</td>
</tr><tr>
    <td>13:22</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Вилли Токарев - Небоскребы</td>
</tr><tr>
    <td>13:16</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Владимир Ждамиров - А я несу тебе цветы</td>
</tr><tr>
    <td>13:07</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Олег Газманов и Александр Маршал - Мама - Родина</td>
</tr><tr>
    <td>12:44</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Дмитрий Хмелёв - Капитан</td>
</tr><tr>
    <td>12:41</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Евгений Григорьев - Венеция</td>
</tr><tr>
    <td>12:35</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Сергей Трофимов - Город в пробках</td>
</tr><tr>
    <td>12:30</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Александр Барыкин - Прощай, любимый город (Вечер на рейде)</td>
</tr><tr>
    <td>12:27</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Анатолий Полотно и Федя Карманов - Цветная Азия</td>
</tr><tr>
    <td>12:16</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Слава - Спелый мой</td>
</tr><tr>
    <td>12:12</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Шуфутинский - Глаза в глаза</td>
</tr><tr>
    <td>12:03</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Иван Кучин - Фотокарточка</td>
</tr><tr>
    <td>12:00</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Максим Олейников - Нас толкает за рамки любовь</td>
</tr><tr>
    <td>11:55</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Игорь Слуцкий - Не догонит беда</td>
</tr><tr>
    <td>11:37</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Alex Pilips feat. Братья Карамазова - Хемингуэй</td>
</tr><tr>
    <td>11:34</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Лесоповал - Суп-тоска</td>
</tr><tr>
    <td>11:31</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Сергей Куренков - Я хочу побыть с тобой</td>
</tr><tr>
    <td>11:28</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Надежда Мельянцева - Сашка</td>
</tr><tr>
    <td>11:21</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Евгений Кемеровский - Я к тебе не вернусь</td>
</tr><tr>
    <td>11:16</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Александр Буйнов - Руки теплые на бархате цветном</td>
</tr><tr>
    <td>11:07</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Виталий Аксёнов - Поезд</td>
</tr><tr>
    <td>11:03</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Елена Ваенга - Аэропорт</td>
</tr><tr>
    <td>10:55</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Катерина Голицына - Как ты там</td>
</tr><tr>
    <td>10:52</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Артур Руденко - Мне тебя не хватает очень</td>
</tr><tr>
    <td>10:37</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Александр Розенбаум - Необычно, незнакомо</td>
</tr><tr>
    <td>10:33</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Анимация - Осторожно - Россия</td>
</tr><tr>
    <td>10:30</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Алексей Брянцев - Любовь уходит тихо</td>
</tr><tr>
    <td>10:27</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Гоша Грачевский - Тунеядец</td>
</tr><tr>
    <td>10:24</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Шуфутинский - Love story</td>
</tr><tr>
    <td>10:22</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Ринат Сафин - Месяц</td>
</tr><tr>
    <td>10:16</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Юрий Антонов - На улице Каштановой</td>
</tr><tr>
    <td>10:13</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Любовь Успенская - Горький вкус бузины</td>
</tr><tr>
    <td>09:45</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Бурляш - Гетера</td>
</tr><tr>
    <td>09:41</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Настасья Самбурская - Саша</td>
</tr><tr>
    <td>09:27</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Артем Дёмин - Зажигай</td>
</tr><tr>
    <td>09:24</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Стас Михайлов - Этот долгий день</td>
</tr><tr>
    <td>09:21</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Баян Микс - Не гони коней</td>
</tr><tr>
    <td>09:08</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Ля-Минор - У черного моря</td>
</tr><tr>
    <td>09:03</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Сергей Трофимов - Горько</td>
</tr><tr>
    <td>09:00</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Таисия Повалий - Чай с молоком</td>
</tr><tr>
    <td>08:55</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Виктор Третьяков - Карамелька</td>
</tr><tr>
    <td>08:51</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Март Бабаян - Самая красивая женщина</td>
</tr><tr>
    <td>08:43</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Воровайки - Московские улочки</td>
</tr><tr>
    <td>08:40</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Валерий Сюткин - Король "Оранжевое лето"</td>
</tr><tr>
    <td>08:31</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Григорий Лепс - Водопадом</td>
</tr><tr>
    <td>08:27</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Татьяна Буланова - Играю в прятки на судьбу</td>
</tr><tr>
    <td>08:11</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Шуфутинский - Ты-моя жизнь</td>
</tr><tr>
    <td>07:54</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Андрей Бандера - Сыпь, тальянка</td>
</tr><tr>
    <td>07:50</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михайлов , Стас - Кто, если не ты</td>
</tr><tr>
    <td>07:46</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Николай Расторгуев - Есть только миг</td>
</tr><tr>
    <td>07:42</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Виктор Королев - На белой карете</td>
</tr><tr>
    <td>07:38</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Гарик Сукачев - Тот, который не стрелял</td>
</tr><tr>
    <td>07:34</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Сосо Павлиашвили и Арсен Шахунц - Загуляли пацаны</td>
</tr><tr>
    <td>07:30</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Любовь Успенская - Кабриолет</td>
</tr><tr>
    <td>07:27</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Сентябрь - Моя стюардесса</td>
</tr><tr>
    <td>07:23</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Сергей Любавин - Счастье в долгу у несчастья</td>
</tr><tr>
    <td>07:13</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Олег Газманов - Единственная</td>
</tr><tr>
    <td>07:05</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Елена Ваенга - Клавиши</td>
</tr><tr>
    <td>07:00</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Вахтанг - Обнадёжь надеждой, нирвана</td>
</tr><tr>
    <td>06:37</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Круг - Электричка</td>
</tr><tr>
    <td>06:34</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Владимир Захаров - Костры</td>
</tr><tr>
    <td>06:30</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Бублик - Сыграем</td>
</tr><tr>
    <td>06:23</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Владимир Высоцкий - Диалог у телевизора</td>
</tr><tr>
    <td>06:21</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Домогаров Александр - Дорогая</td>
</tr><tr>
    <td>06:17</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Гоша Грачевский - Карта не прет</td>
</tr><tr>
    <td>06:13</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Брендон Стоун - Папа</td>
</tr><tr>
    <td>06:04</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Катерина Голицына - Любовь не бывает</td>
</tr><tr>
    <td>06:00</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Артур Руденко и Виктория Алешко - Виктория-вестница</td>
</tr><tr>
    <td>05:54</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Белый орел - Я один и ты одна</td>
</tr><tr>
    <td>05:50</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Иван Кучин - Друг</td>
</tr><tr>
    <td>05:37</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Денис Майданов - Будем жить, старина!</td>
</tr><tr>
    <td>05:34</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Александр Розенбаум - На улице Марата</td>
</tr><tr>
    <td>05:27</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Анатолий Полотно и Федя Карманов - Цветная Азия</td>
</tr><tr>
    <td>05:23</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Дорин Виктор - Самое красивое имя</td>
</tr><tr>
    <td>05:20</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Ля-Минор - Алёшка жарил на баяне*</td>
</tr><tr>
    <td>05:12</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Григорий Лепс - Не троньте душу грязными руками</td>
</tr><tr>
    <td>05:08</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Ислам Итляшев - Хищница</td>
</tr><tr>
    <td>05:01</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Стас Михайлов - Половинка</td>
</tr><tr>
    <td>04:54</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Андрей Никольский - Марусенька</td>
</tr><tr>
    <td>04:50</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Евгений Григорьев - Таксист</td>
</tr><tr>
    <td>04:44</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Максим Олейников - Нас толкает за рамки любовь</td>
</tr><tr>
    <td>04:40</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Катя Огонек - Подруженька</td>
</tr><tr>
    <td>04:31</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Аркадий Северный - Корчма</td>
</tr><tr>
    <td>04:27</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Алёна Петровская и Евгений Росс - Донская бравада</td>
</tr><tr>
    <td>04:23</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Задорин - Это не любовь</td>
</tr><tr>
    <td>04:21</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Александр Дюмин - Кареглазая</td>
</tr><tr>
    <td>04:06</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Афина - Дикое танго</td>
</tr><tr>
    <td>03:55</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Андрей Бандера - Ивушки</td>
</tr><tr>
    <td>03:44</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Хор Турецкого - Ленинградский горьковатый хлеб</td>
</tr><tr>
    <td>03:37</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Любовь Успенская - Дорогами</td>
</tr><tr>
    <td>03:30</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">ВИА Волга-Волга - Поручни любви</td>
</tr><tr>
    <td>03:26</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Герман Грач - Дон</td>
</tr><tr>
    <td>03:23</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Граф Гагарин - 3 режима</td>
</tr><tr>
    <td>03:12</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Игорь Слуцкий - Прости и прощай</td>
</tr><tr>
    <td>03:06</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Андрей Васильев - Колесики</td>
</tr><tr>
    <td>03:01</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Евгений Кемеровский - Милая</td>
</tr><tr>
    <td>03:00</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Лолита - Судьба (DJ Antonio remix)</td>
</tr><tr>
    <td>02:54</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Анатолий Полотно - Живите-здравствуйте!</td>
</tr><tr>
    <td>02:41</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Геннадий Жаров - Крапива</td>
</tr><tr>
    <td>02:39</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Братья Мищуки - Дорога, разлука</td>
</tr><tr>
    <td>02:28</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Брендон Стоун - Правда без лица</td>
</tr><tr>
    <td>02:21</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Владимир Асмолов - Ты мой сон</td>
</tr><tr>
    <td>02:12</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Сергей Наговицын - Глашка</td>
</tr><tr>
    <td>02:05</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Шуфутинский - Love story</td>
</tr><tr>
    <td>02:00</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Владислав Медяник - Тяжело седому пацану</td>
</tr><tr>
    <td>01:55</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Балаган Лимитед - Чё те надо</td>
</tr><tr>
    <td>01:50</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Анатолий Днепров - Красивая</td>
</tr><tr>
    <td>01:48</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Юрий Барабаш - Не хотел умирать</td>
</tr><tr>
    <td>01:38</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Надежда Мельянцева - Сашка</td>
</tr><tr>
    <td>01:31</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Алена Ланская - Наше счастье одно на двоих</td>
</tr><tr>
    <td>01:12</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Валерий Залкин - Одинокая ветка сирени</td>
</tr><tr>
    <td>01:05</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Игорь Росписной - Благослови</td>
</tr><tr>
    <td>01:00</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Ясения - Я знаю, мама</td>
</tr><tr>
    <td>00:54</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Михаил Бублик - За серебряными снегами</td>
</tr><tr>
    <td>00:49</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Евгений Росс и Федор Добронравов - У переправы</td>
</tr><tr>
    <td>00:42</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Гоша Грачевский - Ресторан</td>
</tr><tr>
    <td>00:32</td>
    <td class="font-medium w-full leading-tight js--radio-playlist-track">Александр Буйнов - Руки теплые на бархате цветном</td>
</tr>"""

soup = BeautifulSoup(plalist,'html.parser')

song_title_list = soup.find_all('td',class_='font-medium w-full leading-tight js--radio-playlist-track')

song_title_list = [song_title.text for song_title in song_title_list]

# for song_title in song_title_list :
#     print(song_title.text)

print(song_title_list)

# ПОИСК ВСЕХ РАДИОСТАНЦИЙ
# RadioStation =