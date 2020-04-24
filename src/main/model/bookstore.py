from src.main.model.genre_type import GenreType


class Bookstore:
    def __init__(self, name=None, producer=None, genre_type=GenreType.TALE, number_of_pages=None,
                 text_language=None, new_condition=True, hard_cover=False, price_in_uah=None):
        self.name = name
        self.producer = producer
        self.genre_type = genre_type
        self.number_of_pages = number_of_pages
        self.text_language = text_language
        self.new_condition = new_condition
        self.hard_cover = hard_cover
        self.price_in_uah = price_in_uah

    def __del__(self):
        return
