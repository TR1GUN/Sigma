from Template.Template_BaseClass import IBaseClass


class WebsiteDownload(IBaseClass):
    """
    Класс работы со скачиванием
    """
    #
    # Файл, что скачали
    __File = b""
    # Код состояния
    __code = 6

    def __init__(self, link_soundtrack: str):
        """
        Что принимаем:

        :param Sound_list: Список из названий. песен
        """

    def _Download_mp3_file(self):

        #
        data = ""
        #

        # Провеляем что что то  получили
        if data:

            # формируем файл
            mp3_File = b""

            return mp3_File

        else:
            # Логируем, что не скачали
            error = "Не удалось скачать файл - "
            self._LOG(Text=error, Type_error=2)

            return None

    def _Read_Binary_file(self, answer_to_site):
        """
        В этом методе
        :param answer_to_site:
        :return:
        """

    def __call__(self):

        # Лезем в рефлексию - не очень хорошо
        return {"File": self.__File, "code": self.__code}
