from src.main.classes.genre_type import GenreType
from src.main.classes.preparation_for_eit import PreparationForEIT
from src.main.classes.calendar import Calendar
from src.main.classes.goods_for_children import GoodsForChildren
from src.main.classes.bookstore import Bookstore
from src.main.classes.books_with_age_restrictions import BooksWithAgeRestrictions
from src.main.manager.bookstore_manager import BookstoreManager


def main():
    child = GoodsForChildren("YStoryTale", "UaTale", GenreType.TALE, 125, "UA", True, True, 450.76, False, False)
    horror = BooksWithAgeRestrictions("It", "Hocking", GenreType.HORROR, 125, "UA", True, False, 25.55, 18, True)
    preparation = PreparationForEIT("100EIT", "UaTest", None, 200, "Ua", True, False, 150.50, True, 2019)
    goods = [child, horror, preparation]

    # manager = BookstoreManager(calendar)
    [print(count_of_goods) for count_of_goods in goods]


if __name__ == '__main__':
    main()
