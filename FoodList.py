from typing import List
import re

import openpyxl
import pandas
import pandas as pd
from Food import Food

RESTAURANT_FILE = 'food_list.xlsx'

class FoodList:
    # Constructor
    def __init__(self):
        self.source_file = pd.read_excel(RESTAURANT_FILE)
        self.food_list = self.read_food_list()

    # Facilitates creation of food list from external input source
    def read_food_list(self) -> List[Food]:
        food_list = []

        for column, row in self.source_file.items():
            if column.lower() == "restaurant":
                for restaurant in list(row):
                    food_list.append(Food(restaurant))
            if column.lower() == "category":
                for i in range(len(food_list)):
                    food_list[i].set_category(row[i])

        return food_list

    def make_sub_list(self, category_list: List[str]) -> List[Food]:
        sub_list = []

        for food in self.food_list:
            for category in category_list:
                if food.get_category() == category:
                    sub_list.append(food)

        return sub_list

    def find_restaurant(self, lookup_restaurant: str) -> Food or None:
        name_for_compare = lookup_restaurant.lower()
        name_for_compare = re.sub('[^0-9a-zA-Z]+', '', name_for_compare)

        for restaurant in self.food_list:
            temp_name = restaurant.get_name().lower()
            temp_name = re.sub('[^0-9a-zA-Z]+', '', temp_name)

            if name_for_compare in temp_name:
                return restaurant

        return None

    def populate_restaurant(self, new_restaurant: Food) -> None:
        self.food_list.append(new_restaurant)

        temp_df = pd.DataFrame([[new_restaurant.get_name(), new_restaurant.get_category_int()]],
                               index=[len(self.source_file)],
                               columns=['Restaurant', 'Category'])

        self.source_file = pd.concat([self.source_file, temp_df])
        self.source_file.to_excel(RESTAURANT_FILE)

