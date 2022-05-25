# --------------- Dependencies --------------- #
from category import Category


# --------------- Classes --------------- #


""" Represents a restaurant. """
class Food:
    """ Constructor. """
    def __init__(self, name: str = "", category: int = 0) -> None:
        self.__name = name
        self.__category = self.__populate_category(category)

    """ Populates food object category member based on input integer. """
    def __populate_category(self, category: int) -> Category:
        for name, member in Category.__members__.items():
            if member.value == category:
                return Category(member)

    """ Retrieves category member string representation. """
    def get_category(self) -> str:
        return self.__category.name

    """ Sets value of object category. """
    def set_category(self, category: int) -> None:
        self.__category = self.__populate_category(category)

    """ Retrieves object's category integer representation. """
    def get_category_int(self) -> int:
        return self.__category.value

    """ Retrieves object's name string. """
    def get_name(self) -> str:
        return self.__name

    """ Changes object's name string. """
    def set_name(self, name: str) -> None:
        self.__name = name

