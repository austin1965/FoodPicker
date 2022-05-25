# --------------- Dependencies --------------- #
from enum import Enum, unique


# --------------- Classes --------------- #


""" Represents potential categories food can take on. """
@unique
class Category(Enum):
    # Values
    FAST_FOOD = 1
    DINE_IN = 2
    DESSERT = 3
    COFFEE = 4
    ALCOHOL = 5
    BREAKFAST = 6

    """ Outputs potential categories. """
    @classmethod
    def print_categories(cls) -> None:
        print("Categories: ")
        for name, member in Category.__members__.items():
            print(f"{member.value}. {name}")
        print()

