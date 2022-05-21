from typing import List
import pandas as pd
from Food import Food

RESTAURANT_FILE = 'food_list.xlsx'

class FoodList:
    # Constructor
    def __init__(self):
        self.source_file = RESTAURANT_FILE
        self.food_list = self.read_food_list()

    # Facilitates creation of food list from external input source
    def read_food_list(self) -> List[Food]:
        food_df = pd.read_excel(self.source_file)
        food_list = []
        for column, row in food_df.items():
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

    def populate_restaurant(self, restaurant: Food) -> None:
        print("populate_restaurant: FIXME")

