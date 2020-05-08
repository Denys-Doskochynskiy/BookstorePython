class Bookstore:
    def __init__(self, name=None, producer=None, number_of_pages=None,
                 text_language=None, new_condition=True, hard_cover=False, price_in_uah=None):
        self._name = name
        self._producer = producer

        self._number_of_pages = number_of_pages
        self._text_language = text_language
        self._new_condition = new_condition
        self._hard_cover = hard_cover
        self._price_in_uah = price_in_uah



    def __str__(self):
        name = "Name: {0}\n".format(self._name)
        producer = "Producer: {0}\n".format(self._producer)

        number_of_pages = "Number of pages: {0}\n".format(self._number_of_pages)
        text_language = "Text language: {0}\n".format(self._text_language)
        new_condition = "New condition: {0}\n".format(self._new_condition)
        hard_cover = "Hard cover: {0}\n".format(self._hard_cover)
        price_in_uah = "Price in UAH: {0}\n".format(self._price_in_uah)

        return name + producer + number_of_pages + \
               text_language + new_condition + hard_cover + price_in_uah

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def producer(self):
        return self._producer

    @producer.setter
    def producer(self, producer):
        self._producer = producer

    @property
    def number_of_pages(self):
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, number_of_pages):
        self._number_of_pages = number_of_pages

    @property
    def text_language(self):
        return self._text_language

    @text_language.setter
    def text_language(self, text_language):
        self._text_language = text_language

    @property
    def new_condition(self):
        return self._new_condition

    @new_condition.setter
    def new_condition(self, new_condition):
        self._new_condition = new_condition

    @property
    def hard_cover(self):
        return self._hard_cover

    @hard_cover.setter
    def hard_cover(self, hard_cover):
        self._hard_cover = hard_cover

    @property
    def price_in_uah(self):
        return self._price_in_uah

    @price_in_uah.setter
    def price_in_uah(self, price_in_uah):
        self._price_in_uah = price_in_uah