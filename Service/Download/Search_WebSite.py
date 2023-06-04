
class WebsiteSearchMP3UKS(WebsiteSearch):
    """
    Класс для работы c поиском нужного трека на сайте https://mp3uks.ru/
    """

    # Код состояния
    _code = 6

    def __init__(self, name_soundtrack: str):
        """
        Что принимаем:

        :param name_soundtrack: Название саундтрека
        """

    def _search_soundtrack(self, name_soundtrack):
        """
        Ищем наш саундтрек пол названию
        :param name_soundtrack: - Название саундтрека
        :return:
        """
        # Формируем наш запрос -

