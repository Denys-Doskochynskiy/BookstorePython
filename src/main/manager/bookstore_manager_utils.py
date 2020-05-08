from src.main.classes.books_with_age_restrictions import BooksWithAgeRestrictions
from src.main.classes.genre_type import GenreType
from src.main.classes.preparation_for_eit import PreparationForEIT
from src.main.classes.goods_for_children import GoodsForChildren
import doctest


class BookstoreManagerUtils:
    def __init__(self):
        pass

    @staticmethod
    def sort_by_price_descending(list_of_goods, reverse=True):
        """
        >>> child = GoodsForChildren("UaGame","Game",None,1,"Ua",True,None,1020,False,True)
        >>> horror = BooksWithAgeRestrictions("It", "Hocking", GenreType.HORROR, 125, "UA", True, False, 250, 18, True)
        >>> preparation = PreparationForEIT("100EIT", "UaTest", None, 200, "Ua", True, False, 350, True, 2019)
        >>> print(str(BookstoreManagerUtils.sort_by_price_descending(([child,horror, preparation])))) #doctest: +ELLIPSIS
        [GoodsForChildren(...price_in_uah=1020...), PreparationForEIT(...price_in_uah=350...), BooksWithAgeRestrictions(...price_in_uah=250...)]
        """
        return sorted(list_of_goods, key=lambda good: good.price_in_uah, reverse=reverse)

    @staticmethod
    def sort_by_price_ascending(list_of_goods, reverse=False):
        """
        >>> child = GoodsForChildren("UaGame","Game",None,1,"Ua",True,None,1020,False,True)
        >>> horror = BooksWithAgeRestrictions("It", "Hocking", GenreType.HORROR, 1250, "UA", True, False, 250, 18, True)
        >>> preparation = PreparationForEIT("100EIT", "UaTest", None, 200, "Ua", True, False, 350, True, 2019)
        >>> print(str(BookstoreManagerUtils.sort_by_price_ascending(([child,horror, preparation])))) #doctest: +ELLIPSIS
        [BooksWithAgeRestrictions(...price_in_uah=250...), PreparationForEIT(...price_in_uah=350...), GoodsForChildren(...price_in_uah=1020...)]
        """
        return sorted(list_of_goods, key=lambda good: good.price_in_uah, reverse=reverse)

    @staticmethod
    def sort_by_number_of_pages(list_of_goods, reverse=True):
        """
        >>> child = GoodsForChildren("UaGame","Game",None,1,"Ua",True,None,1020,False,True)
        >>> horror = BooksWithAgeRestrictions("It", "Hocking", GenreType.HORROR, 1250, "UA", True, False, 250, 18, True)
        >>> preparation = PreparationForEIT("100EIT", "UaTest", None, 200, "Ua", True, False, 350, True, 2019)
        >>> print(str(BookstoreManagerUtils.sort_by_number_of_pages(([child,horror, preparation])))) #doctest: +ELLIPSIS
        [GoodsForChildren(...number_of_pages=1...), PreparationForEIT(...number_of_pages=200...), BooksWithAgeRestrictions(...number_of_pages=1250...)]
        """
        return sorted(list_of_goods, key=lambda good: good.price_in_uah, reverse=reverse)


if __name__ == '__main__':
    doctest.testmod(verbose=True)
