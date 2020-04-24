from src.main.model.bookstore import Bookstore


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

