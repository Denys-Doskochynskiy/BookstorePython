from src.main.classes.bookstore import Bookstore


class Calendar(Bookstore):
    def __init__(self, name, producer, genre_type, number_of_pages,
                 text_language, new_condition, hard_cover, price_in_uah, year=None, leaky_calendar=None):
        super().__init__(name, producer, genre_type, number_of_pages,
                         text_language, new_condition, hard_cover, price_in_uah)
        self.year = year
        self.leaky_calendar = leaky_calendar

    def __del__(self):
        print("calendar die")
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
        year = "Year: {0}\n".format(self.year)
        leaky_calendar = "Leaky calendar: {0}\n".format(self.leaky_calendar)
        return name + producer + genre_type + number_of_pages + \
               text_language + new_condition + hard_cover + price_in_uah + year + leaky_calendar
