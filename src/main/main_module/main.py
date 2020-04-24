from src.main.model.genre_type import GenreType
from src.main.model.preparation_for_eit import PreparationForEIT
from src.main.model.calendar import Calendar
from src.main.model.goods_for_children import GoodsForChildren
from src.main.model.bookstore import Bookstore
from src.main.model.books_with_age_restrictions import BooksWithAgeRestrictions
from src.main.manager.bookstore_manager import BookstoreManager


def main():
    calendar = Calendar("Year", "UaCalendar", None, 125, "UA", True, False, 25.55, 2020, True)
    horror = BooksWithAgeRestrictions("It", "Hocking", GenreType.HORROR, 125, "UA", True, False, 25.55, 18, True)
    goods = [calendar, horror]

    # manager = BookstoreManager(calendar)
    [print(count_of_goods) for count_of_goods in goods]


if __name__ == '__main__':
    main()
