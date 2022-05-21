# --------------- Dependencies --------------- #
from random import choice
from typing import List
from Category import Category
from Food import Food
from FoodList import FoodList


# --------------- Classes --------------- #


# Class controls the selection of food and input / output of food list
class FoodController:

    # Constructor
    def __init__(self):
        self.food_list = FoodList()

    # Runs main menu and user menu selection.
    def food_picker_main(self) -> None:
        picking_food = True

        while picking_food:

            self.print_menu()
            user_input = input("\nPlease pick a menu option: ")

            if user_input == '1':
                self.pick_restaurant()
            elif user_input == '2':
                self.search_restaurant()
            elif user_input == '3':
                self.add_restaurant()
            elif user_input == '4':
                self.edit_restaurant()
            elif user_input == '5':
                picking_food = False
            else:
                print("Invalid input.")

    # Outputs main menu choices
    def print_menu(self) -> None:
        print("1. Pick Restaurant")
        print("2. Search Restaurant")
        print("3. Add Restaurant")
        print("4. Edit Restaurant")
        print("5. Exit")

    # MENU OPT 1 MAIN: Facilitates restaurant selection process.
    def pick_restaurant(self) -> None:
        categories = self.category_picker()
        food_sub_list = self.food_list.make_sub_list(categories)
        decision = choice(food_sub_list)
        print(f"Decided on restaurant... {decision.get_name()}\n")

    # MENU OPT 1 HELPER: Facilitates user category selection.
    def category_picker(self) -> List[str]:
        total_categories = [str(member.value) for name, member in Category.__members__.items()]
        user_categories = []
        user_inputting = True

        Category.print_categories()

        while user_inputting:
            input_value = input("Input the category numbers you want, press Q to exit: ")
            if input_value in total_categories:
                if input_value not in user_categories:
                    user_categories.append(input_value)
                else:
                    print("Selection already made:")
            elif input_value.upper() == 'Q':
                user_inputting = False
            else:
                print("Invalid selection")

        return self.category_int_mapper(user_categories)

    # MENU OPT 1 HELPER: Maps user input category strings to integers to category names.
    def category_int_mapper(self, str_categories: List[str]) -> List[str]:
        int_categories = [int(x) for x in str_categories]
        cat_obj_list = []

        for x in int_categories:
            for name, member in Category.__members__.items():
                if member.value == x:
                    cat_obj_list.append(name)

        return cat_obj_list

    # MENU OPT 2 MAIN:
    def search_restaurant(self) -> None:
        print("search_restaurant: FIXME")

    # MENU OPT 3 MAIN: Facilitates creating new food objects for external input source.
    def add_restaurant(self) -> None:
        name = input("Restaurant name: ")
        category = int(input("Restaurant category: "))
        new_food = Food(name, category)
        self.food_list.populate_restaurant(new_food)

    # MENU OPT 4 MAIN:
    def edit_restaurant(self) -> None:
        print("edit_restaurant: FIXME")


if __name__ == '__main__':
    restaurant_chooser = FoodController()
    restaurant_chooser.food_picker_main()
