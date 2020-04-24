from src.main.classes.bookstore import Bookstore


class PreparationForEIT(Bookstore):
    def __init__(self, name, producer, genre_type, number_of_pages,
                 text_language, new_condition, hard_cover, price_in_uah, availability_of_solutions_task=None,
                 year_of_eit=None):
        super().__init__(name, producer, genre_type, number_of_pages,
                         text_language, new_condition, hard_cover, price_in_uah)
        self.year_of_eit = year_of_eit
        self.availability_of_solutions_task = availability_of_solutions_task

    def __del__(self):
        print("student die")
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
        availability_of_solutions_task = "Availability of solutions task: {0}\n".format(
            self.availability_of_solutions_task)
        year_of_eit = "Year of eit: {0}\n".format(self.year_of_eit)
        return name + producer + genre_type + number_of_pages + \
               text_language + new_condition + hard_cover + price_in_uah + availability_of_solutions_task + year_of_eit
