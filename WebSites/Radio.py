# Здесь опишим клвасс с радио

# Нас интересует выкачка всех радио
#
# выкачка всех листов

# Здесь опишем класс, чтоб работать с получением
from Template.Template_BaseClass import IBaseClass


class PlaylistSiteNameRadioPotok(IBaseClass):
    """
    В Этом классе работаем с сайтом https://radiopotok.ru/

    Нам необходимо на этом сайте:
    - Скачать плейлист
    """
    # Само имя сайта с которого скачиваем
    WebSite_name = "https://radiopotok.ru/"
    # Плейлист
    __Playlist_list = []
    # Результат работы
    __result = ""
    # Код состояния
    __code = 6

    def __init__(self, ID_radio: str):
        """
        Что принимаем:
        :param Radio_ID: ID радио
        """

        # Пункт первый - Ищем нашу ссылку на файл для скачивания
        self.__Playlist_list = self._Search_Playlist(ID_radio=ID_radio)




    def _Search_Playlist(self, ID_radio):
        """
        В этом методе выполняем: Поиск нужного плейлиста
        :param name_soundtrack:
        :return:
        """
        from Service.Radio.Playlist_WebSite import WebsitePlaylistRadioPotok

        # Ищем ссылку
        Playlist_list, self.__code = WebsitePlaylistRadioPotok(ID_radio=ID_radio)

        return Playlist_list

    def __call__(self):

        return {"Playlist": self.__Playlist_list, "code": self.__code}

    # def Result(self):
    #     """
    #     Получаем результат деятельности
    #     :return:
    #     """
    #     return {"File": self.__Playlist_list, "code": self.__code}