from src.main.model.bookstore import Bookstore


class PreparationForEIT(Bookstore):
    def __init__(self, name, producer, genre_type, number_of_pages,
                 text_language, new_condition, hard_cover, price_in_uah, availability_of_solutions_task=None,
                 year_of_eit=None):
        super().__init__(name, producer, genre_type, number_of_pages,
                         text_language, new_condition, hard_cover, price_in_uah)
        self.year_of_eit = year_of_eit
        self.availability_of_solutions_task = availability_of_solutions_task

    def __del__(self):
        return
