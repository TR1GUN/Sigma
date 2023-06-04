# Здесь опишем файл самого действия
from Template.Template_BaseClass import IBaseClass
class Action(IBaseClass):



    def __init__(self, RadioStation_list:list , Params:dict = {"unique":True} ):
        """
        Получаем ID радиостанции и работаем с их плейлистом
        :param Radiostation_list:
        """

    # Получаем список треков за сутки
    def _get_list_of_tracks_per_day(self):

        pass

    # Компануем это все в плейлист
    def _formation_playlist(self):

        pass

    # Пытаемся скачать все это
    def _download_soundtrack(self):

        pass