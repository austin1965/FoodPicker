from Category import Category


class Food:
    def __init__(self, name: str = "", category: int = 0) -> None:
        self.__name = name
        self.__category = self.__populate_category(category)

    def __populate_category(self, category: int) -> Category:

        for name, member in Category.__members__.items():
            if member.value == category:
                return Category(member)

    def get_category(self) -> str:
        return self.__category.name

    def set_category(self, category: int) -> None:
        self.__category = self.__populate_category(category)

    def get_category_int(self) -> int:
        return self.__category.value

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

