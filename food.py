# --------------- Dependencies --------------- #
from category import Category


# --------------- Classes --------------- #


class Food:
    """ Represents a restaurant. """

    def __init__(self, name: str = "", category: int = 0) -> None:
        """ Constructor. """

        self.__name = name
        self.__category = self.__populate_category(category)

    @staticmethod
    def __populate_category(category: int) -> Category:
        """ Populates food object category member based on input integer. """

        for _, member in Category.__members__.items():
            if member.value == category:
                return Category(member)

    def get_category(self) -> str:
        """ Retrieves category member string representation. """
        return self.__category.name

    def set_category(self, category: int) -> None:
        """ Sets value of object category. """
        self.__category = self.__populate_category(category)

    def get_category_int(self) -> int:
        """ Retrieves object's category integer representation. """
        return self.__category.value

    def get_name(self) -> str:
        """ Retrieves object's name string. """
        return self.__name

    def set_name(self, name: str) -> None:
        """ Changes object's name string. """
        self.__name = name

