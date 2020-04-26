import doctest

from src.main.classes.books_with_age_restrictions import BooksWithAgeRestrictions
from src.main.classes.genre_type import GenreType
from src.main.classes.goods_for_children import GoodsForChildren
from src.main.classes.preparation_for_eit import PreparationForEIT


class BookstoreManager:
    def __init__(self, list_of_goods=[]):
        self.list_of_goods = list_of_goods

    def find_goods_by_genre(self, genre_type: GenreType):
        """
        >>> child = GoodsForChildren("UaGame","Game",None,1,"Ua",True,None,1020,False,True)
        >>> horror = BooksWithAgeRestrictions("It", "Hocking", GenreType.HORROR, 125, "UA", True, False, 250, 18, True)
        >>> preparation = PreparationForEIT("100EIT", "UaTest", None, 200, "Ua", True, False, 350, True, 2019)
        >>> print(str(BookstoreManager([child, horror, preparation]).find_goods_by_genre(GenreType.HORROR))) #doctest: +ELLIPSIS
        [BooksWithAgeRestrictions(...genre_type=GenreType.HORROR...)]


        """
        return list(filter(lambda good: good.genre_type == genre_type, self.list_of_goods))


if __name__ == '__main__':
    doctest.testmod(verbose=True)
