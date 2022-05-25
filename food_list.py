# --------------- Dependencies --------------- #
from typing import List
import re
import pandas as pd
from food import Food

# --------------- Constants --------------- #
RESTAURANT_FILE = 'food_list.xlsx'


# --------------- Classes --------------- #


class FoodList:
    """ Provides abstraction layer for interfacing with external data source and list of food objects. """

    def __init__(self):
        """ Constructor. """

        self.source_file = pd.read_excel(RESTAURANT_FILE)
        self.food_list = self.read_food_list()

    def read_food_list(self) -> List[Food]:
        """ Facilitates creation of food list from external input source. """

        food_list = []

        for column, row in self.source_file.items():
            if column.lower() == "restaurant":
                for restaurant in list(row):
                    food_list.append(Food(restaurant))
            if column.lower() == "category":
                for i, _ in enumerate(food_list):
                    food_list[i].set_category(row[i])

        return food_list

    def make_sub_list(self, category_list: List[str]) -> List[Food]:
        """ Generates a sublist of the larger food list member filtered down by categories provided. """

        sub_list = []

        for food in self.food_list:
            for category in category_list:
                if food.get_category() == category:
                    sub_list.append(food)

        return sub_list

    def find_restaurant(self, lookup_restaurant: str) -> Food | None:
        """ Performs lookup by of a particular restaurant. """

        name_for_compare = lookup_restaurant.lower()
        name_for_compare = re.sub('[^0-9a-zA-Z]+', '', name_for_compare)

        for restaurant in self.food_list:
            temp_name = restaurant.get_name().lower()
            temp_name = re.sub('[^0-9a-zA-Z]+', '', temp_name)

            if name_for_compare in temp_name:
                return restaurant

        return None

    def populate_restaurant(self, new_restaurant: Food) -> None:
        """ Adds new restaurant to external data source and ephemeral food list. """

        self.food_list.append(new_restaurant)
        temp_df = pd.DataFrame([[new_restaurant.get_name(), new_restaurant.get_category_int()]],
                               columns=['Restaurant', 'Category'])

        self.source_file = pd.concat([self.source_file, temp_df], ignore_index=True)
        self.source_file.to_excel(RESTAURANT_FILE)

    def delete_restaurant(self, rest_to_del: Food) -> None:
        """ Removes a restaurant from external data source and ephemeral food list. """

        self.food_list.remove(rest_to_del)
        i = self.source_file[self.source_file["Restaurant"] == rest_to_del.get_name()].index.values
        self.source_file = self.source_file.drop(self.source_file.index[i])
        self.source_file.to_excel(RESTAURANT_FILE)

