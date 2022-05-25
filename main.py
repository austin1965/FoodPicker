# --------------- Dependencies --------------- #
from random import choice
from typing import List
from category import Category
from food import Food
from food_list import FoodList


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
                self.delete_restaurant()
            elif user_input == '6':
                picking_food = False
            else:
                print("Invalid input.")

    # Outputs main menu choices
    def print_menu(self) -> None:
        print()
        print("1. Pick Restaurant")
        print("2. Search Restaurant")
        print("3. Add Restaurant")
        print("4. Edit Restaurant")
        print("5. Delete Restaurant")
        print("6. Exit")

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

    # MENU OPT 2 MAIN: Facilitates lookup of specific restaurant names.
    def search_restaurant(self) -> None:
        lookup = input("Provide restaurant to lookup: ")
        result = self.food_list.find_restaurant(lookup)

        if result:
            print(f"{lookup} closest match is {result.get_name()} of category {result.get_category()}.")
        else:
            print(f"{lookup} is not in food list. {result} found.")

    # MENU OPT 3 MAIN: Facilitates creating new food objects for external input source.
    def add_restaurant(self) -> None:
        name = input("Restaurant name: ")
        category = int(input("Restaurant category: "))
        result = self.food_list.find_restaurant(name)
        confirmation = False

        if result is not None:
            print(f"Found existing restaurant {result.get_name()} of category {result.get_category()}.")
            inp = input("Are you sure you want to add this restaurant? (y/n)")
            if inp == 'y':
                print("Confirmation received.")
                confirmation = True
            else:
                print("Confirmation not received.")
        else:
            confirmation = True

        if confirmation:
            new_food = Food(name, category)
            self.food_list.populate_restaurant(new_food)

    # MENU OPT 4 MAIN: Facilitates editing restaurants with a specific name.
    def edit_restaurant(self) -> None:
        name = input("Provide name of restaurant you want to edit: ")
        result = self.food_list.find_restaurant(name)

        if result:
            print(f"Found restaurant - Name = {result.get_name()}; Category = {result.get_category()}")

            name_choice = input("Do you want a new name for this restaurant? (y/n)")
            if name_choice.lower() == "y":
                new_name = input("New restaurant name: ")

            category_choice = input("Do you want a new category for this restaurant? (y/n)")
            if category_choice.lower() == "y":
                new_category = int(input("New category type: "))

            new_food = Food()
            if name_choice.lower() == "y" or category_choice.lower() == "y":
                if name_choice.lower() == "y" and category_choice.lower() == "y":
                    new_food = Food(new_name, new_category)
                    self.food_list.populate_restaurant(new_food)
                elif name_choice.lower() == "y" and category_choice.lower() == "n":
                    new_food = Food(new_name, result.get_category_int())
                    self.food_list.populate_restaurant(new_food)
                elif name_choice.lower() == "n" and category_choice.lower() == "y":
                    new_food = Food(result.get_name(), new_category)
                    self.food_list.populate_restaurant(new_food)
                print(f"Previously: {result.get_name()}: {result.get_category()}")
                print(f"Edited to: {new_food.get_name()}: {new_food.get_category()}")
            else:
                print("Returning to menu\n")

        else:
            print("No restaurant with this name found.")

    # Facilitates deleting restaurants with a specific name.
    def delete_restaurant(self) -> None:
        name = input("Provide name of restaurant you want to delete: ")
        result = self.food_list.find_restaurant(name)

        if result:
            self.food_list.delete_restaurant(result)
        else:
            print(f"Cannot find restaurant with name {name}")


if __name__ == '__main__':
    restaurant_chooser = FoodController()
    restaurant_chooser.food_picker_main()
