# --------------- Dependencies --------------- #
from random import choice
from typing import List
from category import Category
from food import Food
from food_list import FoodList
from rich.console import Console

# --------------- Classes --------------- #

console = Console()


class FoodController:
    """Class controls the selection of food and input / output of food list."""

    def __init__(self):
        """Constructor."""
        self.food_list = FoodList()

    def food_picker_main(self) -> None:
        """Runs main menu and user menu selection."""

        picking_food = True

        while picking_food:

            self.print_menu()
            # console.print("[green]\nPlease pick a menu option:", end="")
            # console.print("|", end="")
            user_input = console.input(
                "[green]\nPlease pick a menu option: [blink]"
            ).strip()
            match user_input:
                case "1":
                    self.pick_restaurant()
                case "2":
                    self.search_restaurant()
                case "3":
                    self.add_restaurant()
                case "4":
                    self.edit_restaurant()
                case "5":
                    self.delete_restaurant()
                case "6":
                    picking_food = False
                case _:
                    console.print("[bold red]Invalid Input")

    def print_menu(self) -> None:
        """Outputs main menu choices."""
        console.print(
            """[bold green]                                                                                         
                                          ████████                                      
      ░░              ██████  ██████▒▒████░░      ██████████                            
                    ██      ██                              ██                          
                  ██                                          ██                        
                  ██                                    ██  ██                          
                    ████████    ██████      ████        ████                            
                    ████    ██████    ██████    ████████████                            
                      ██      ██        ██        ██      ██                            
                      ██      ██        ██        ██      ██                            
                      ██      ██                  ██      ██                            
                      ██      ██                  ██      ██                            
                      ████▓▓▓▓▓▓▓▓██████████████▓▓▓▓▓▓██████                  ░░        
    ░░                  ████▓▓▓▓██▓▓▓▓██████▓▓▓▓██▓▓████████        ░░        ░░        
                        ░░██████▓▓▓▓██████▓▓████████            ░░                  
                          ██████▓▓▓▓▓▓██████▓▓▓▓▓▓██████                                
                         █▓▓▓▓▓▓▓▓██████████████▓▓▓▓▓▓████                  ░░        
                       ███▓▓▓▓▓▓▓▓██████████████▓▓▓▓▓▓█████                  ░░        


"""
        )
        console.print(
            """    [purple]1.[/purple] [blue]Pick Restaurant [/blue]
    [purple]2.[/purple] [blue]Search Restaurant [/blue]
    [purple]3.[/purple] [blue]Add Restaurant [/blue]
    [purple]4.[/purple] [blue]Search Restaurant [/blue]
    [purple]5.[/purple] [blue]Edit Restaurant [/blue]
    [purple]6.[/purple] [blue]Exit [/blue]"""
        )

    def pick_restaurant(self) -> None:
        """MENU OPT 1 MAIN: Facilitates restaurant selection process."""

        categories = self.category_picker()
        food_sub_list = self.food_list.make_sub_list(categories)
        decision = choice(food_sub_list)
        print(f"Decided on restaurant... {decision.get_name()}\n")

    def category_picker(self) -> List[str]:
        """MENU OPT 1 HELPER: Facilitates user category selection."""

        total_categories = [
            str(member.value) for name, member in Category.__members__.items()
        ]
        user_categories = []
        user_inputting = True

        Category.print_categories()

        while user_inputting:
            input_value = console.input(
                "[green]Input the category numbers you want, press [red]Q[/red] to exit: "
            )

            if input_value in total_categories:
                if input_value not in user_categories:
                    user_categories.append(input_value)
                else:
                    print("Selection already made:")
            elif input_value.upper() == "Q":
                user_inputting = False
            else:
                print("Invalid selection")

        return self.category_int_mapper(user_categories)

    def category_int_mapper(self, str_categories: List[str]) -> List[str]:
        """MENU OPT 1 HELPER: Maps user input category strings to integers to category names."""

        int_categories = [int(x) for x in str_categories]
        cat_obj_list = []

        for x in int_categories:
            for name, member in Category.__members__.items():
                if member.value == x:
                    cat_obj_list.append(name)

        return cat_obj_list

    def search_restaurant(self) -> None:
        """MENU OPT 2 MAIN: Facilitates lookup of specific restaurant names."""

        lookup = input("Provide restaurant to lookup: ")
        result = self.food_list.find_restaurant(lookup)

        if result:
            print(
                f"{lookup} closest match is {result.get_name()} of category {result.get_category()}."
            )
        else:
            print(f"{lookup} is not in food list. {result} found.")

    def add_restaurant(self) -> None:
        """MENU OPT 3 MAIN: Facilitates creating new food objects for external input source."""

        name = input("Restaurant name: ")
        category = int(input("Restaurant category: "))
        result = self.food_list.find_restaurant(name)
        confirmation = False

        if result is not None:
            print(
                f"Found existing restaurant {result.get_name()} of category {result.get_category()}."
            )
            inp = input("Are you sure you want to add this restaurant? (y/n)")
            if inp == "y":
                print("Confirmation received.")
                confirmation = True
            else:
                print("Confirmation not received.")
        else:
            confirmation = True

        if confirmation:
            new_food = Food(name, category)
            self.food_list.populate_restaurant(new_food)

    def edit_restaurant(self) -> None:
        """MENU OPT 4 MAIN: Facilitates editing restaurants with a specific name."""

        name = input("Provide name of restaurant you want to edit: ")
        result = self.food_list.find_restaurant(name)

        if result:
            print(
                f"Found restaurant - Name = {result.get_name()}; Category = {result.get_category()}"
            )

            name_choice = input("Do you want a new name for this restaurant? (y/n)")
            if name_choice.lower() == "y":
                new_name = input("New restaurant name: ")

            category_choice = input(
                "Do you want a new category for this restaurant? (y/n)"
            )
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

    def delete_restaurant(self) -> None:
        """MENU OPT 5 MAIN: Facilitates deleting restaurants with a specific name."""

        name = input("Provide name of restaurant you want to delete: ")
        result = self.food_list.find_restaurant(name)

        if result:
            self.food_list.delete_restaurant(result)
        else:
            print(f"Cannot find restaurant with name {name}")


def main():
    restaurant_chooser = FoodController()
    restaurant_chooser.food_picker_main()


if __name__ == "__main__":
    main()
