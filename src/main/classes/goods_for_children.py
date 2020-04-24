from src.main.classes.bookstore import Bookstore


class GoodsForChildren(Bookstore):
    def __init__(self, name, producer, genre_type, number_of_pages,
                 text_language, new_condition, hard_cover, price_in_uah, availability_of_coloring_books=None,
                 education_toys=None):
        super().__init__(name, producer, genre_type, number_of_pages,
                         text_language, new_condition, hard_cover, price_in_uah)
        self.education_toys = education_toys
        self.availability_of_coloring_books = availability_of_coloring_books

    def __del__(self):
        print("children die")
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
        availability_of_coloring_books = "Availability of coloring books: {0}\n".format(
            self.availability_of_coloring_books)
        education_toys = "Education toys: {0}\n".format(self.education_toys)
        return name + producer + genre_type + number_of_pages + \
               text_language + new_condition + hard_cover + price_in_uah + \
               availability_of_coloring_books + education_toys
