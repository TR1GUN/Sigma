# Здесь опишем файл самого действия
import time

from Template.Template_BaseClass import IBaseClass


class Action(IBaseClass):
    _unique = True
    # Количество дней за которое собираем
    __Scheduler = 0
    # Количество секунд в сутках
    __Time_sleep = 86400

    __Tracks = {}

    def __init__(self, RadioStation_list: list, Scheduler: int, Params: dict = {"unique": True}):
        """
        Получаем ID радиостанции и работаем с их плейлистом
        :param RadioStation_list:
        """
        self._unique = Params.get("unique")
        self.__Scheduler = Scheduler
        self.__Tracks = {}
        RadioPlaylist = self._schedule(RadioStation_list=RadioStation_list)

        for name_soundtrack in RadioPlaylist:
            self.__Tracks[name_soundtrack] = self._download_soundtrack(name_soundtrack=name_soundtrack)

    # Читаем за все время треки в каждом радио
    def _schedule(self, RadioStation_list):
        """
        Сам механизм сбора плейлистов со всех заданных радио
        :param RadioStation_list:
        :return:
        """
        playlist_all = []
        for i in range(self.__Scheduler):
            playlist = self._formation_playlist(RadioStation_list=RadioStation_list)
            playlist_all = playlist_all + playlist
            time.sleep(self.__Time_sleep)

        # Делаем их уникальными
        if self._unique:
            return list(set(playlist_all))
        else:
            return playlist_all

    def _formation_playlist(self, RadioStation_list) -> list:
        """
        Злесл
        :param RadioStation_list:
        :return:
        """
        playlist_all = []
        # Получаем список треков за сутки для каждого радио
        playlist_to_day = [self._get_list_of_tracks_per_day(ID_radio=radio) for radio in RadioStation_list]

        for i in playlist_to_day:
            playlist_all = playlist_all + i

        return playlist_all

    def _get_list_of_tracks_per_day(self, ID_radio) -> list:
        """
        Здесь вычитываем что играло на радио за день
        Возвращаем только уникальные значения
        :param ID_radio:
        :return:
        """
        from WebSites.Radio import PlaylistSiteNameRadioPotok

        __Playlist, __code = PlaylistSiteNameRadioPotok(ID_radio=ID_radio)

        if __code == 6:
            # Возвращаем только уникальные значения за ДЕНЬ
            return list(set(__Playlist))
        else:
            return []

    # Пытаемся скачать все это
    def _download_soundtrack(self, name_soundtrack) -> [str, None]:
        """
        Скачиваем каждый трек
        :param name_soundtrack:
        :return:
        """
        from WebSites.Download import DownloadSiteNameMP3UKS

        __File, __code = DownloadSiteNameMP3UKS(name_soundtrack=name_soundtrack)

        if __code == 6:
            # Возвращаем только уникальные значения за ДЕНЬ
            return __File
        else:
            return None

    def get_tracks(self)->dict:
        """
        Возвращаем наши треки, что скачали
        :return:
        """
        return self.__Tracks
