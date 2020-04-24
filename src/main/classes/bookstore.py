from src.main.classes.genre_type import GenreType


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
        print("bookstore die")
        return

    def __str__(self):
        name = "Name: {0}\n".format(self.name)
        producer = "Producer: {0}\n".format(self.producer)
        genre_type = "Genre type: {0}\n".format(self.genre_type)
        number_of_pages = "Number of pages: {0}\n".format(self.number_of_pages)
        text_language = "Text language: {0}\n".format(self.text_language)
        new_condition = "New condition: {0}\n".format(self.new_condition)
        hard_cover = "Hard cover: {0}\n".format(self.hard_cover)
        price_in_uah = "Price in UAH: {0}\n".format(self.price_in_uah)

        return name + producer + genre_type + number_of_pages + \
               text_language + new_condition + hard_cover + price_in_uah