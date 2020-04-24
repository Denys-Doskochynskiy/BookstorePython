from src.main.classes.bookstore import Bookstore


class BooksWithAgeRestrictions(Bookstore):
    def __init__(self, name, producer, genre_type, number_of_pages,
                 text_language, new_condition, hard_cover, price_in_uah, age_restrictions=None, foul_language=None):
        super().__init__(name, producer, genre_type, number_of_pages,
                         text_language, new_condition, hard_cover, price_in_uah)
        self.age_restrictions = age_restrictions
        self.foul_language = foul_language

    def __del__(self):
        print("Horror die")
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
        age_restrictions = "Age restrictions: {0}\n".format(self.age_restrictions)
        foul_language = "Foul language: {0}\n".format(self.foul_language)
        return name + producer + genre_type + number_of_pages + \
               text_language + new_condition + hard_cover + price_in_uah + age_restrictions + foul_language
