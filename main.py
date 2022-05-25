# --------------- Dependencies --------------- #
from random import choice
import sys
from typing import List
from category import Category
from food import Food
from food_list import FoodList
from rich.console import Console
from os import system
from time import sleep

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
                    break
                case _:
                    console.print("[bold red]Invalid Input\n")
            console.input("\n[green]press [green]enter[/green] to continue.....")
        system("clear")
        console.print(
            """\n\n\n.▀█▀.█▄█.█▀█.█▄.█.█▄▀　█▄█.█▀█.█─█
─.█.─█▀█.█▀█.█.▀█.█▀▄　─█.─█▄█.█▄█\n\tusing our app"""
        )
        sleep(1.5)
        system("clear")

    def print_menu(self) -> None:
        """Outputs main menu choices."""
        system("clear")
        console.print(
            """\n\n\n[bold green]                                                                                         
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
    [purple]4.[/purple] [blue]Edit Restaurant [/blue]
    [purple]5.[/purple] [blue]Delete Restaurant [/blue]
    [purple]6.[/purple] [blue]Exit [/blue]
"""
        )

    def pick_restaurant(self) -> None:
        """MENU OPT 1 MAIN: Facilitates restaurant selection process."""

        categories = self.category_picker()
        if categories:
            food_sub_list = self.food_list.make_sub_list(categories)
            decision = choice(food_sub_list)
            console.print(
                f"\n[green]Decided on restaurant... [purple]{decision.get_name()}[/purple]\n"
            )

    def category_picker(self) -> List[str] | None:
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
                    console.print("[blue]already selected")
            elif input_value.upper() == "Q":
                user_inputting = False
            else:
                print("Invalid selection")
        if user_categories:
            return self.category_int_mapper(user_categories)
        else:
            self.print_menu()

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

        lookup = console.input(
            "[green]Provide restaurant to lookup, press [red]Q[/red] to exit: "
        ).strip()
        if lookup.upper() == "Q":
            self.print_menu()
        else:
            result = self.food_list.find_restaurant(lookup)

            if result:
                console.print(
                    f"\n[green]{lookup} closest match is [purple]{result.get_name()}[/purple] of category [purple]{result.get_category()}[/purple].\n"
                )
            else:
                console.print(f"\n[red]{lookup} is not in food list. {result} found.\n")

    def add_restaurant(self) -> None:
        """MENU OPT 3 MAIN: Facilitates creating new food objects for external input source."""

        name = console.input(
            "[bold green]Restaurant name, press [red]Q[/red] to exit: "
        ).strip()
        if name.upper() == "Q":
            self.print_menu()
        else:
            category = int(input("Restaurant category: "))
            result = self.food_list.find_restaurant(name)
            confirmation = False

            if result is not None:
                console.print(
                    f"Found existing restaurant {result.get_name()} of category {result.get_category()}."
                )
                inp = input("Are you sure you want to add this restaurant? (y/n)")
                if inp == "y":
                    console.print("[light green]Confirmation received.")
                    confirmation = True
                else:
                    console.print("[red]Confirmation not received.")
            else:
                confirmation = True

            if confirmation:
                new_food = Food(name, category)
                self.food_list.populate_restaurant(new_food)
                console.print(f"[purple]successfully added {name} in restaurants")

    def edit_restaurant(self) -> None:
        """MENU OPT 4 MAIN: Facilitates editing restaurants with a specific name."""

        name = console.input(
            "[bold green]Provide name of restaurant you want to edit, press [red]Q[/red] to quit: "
        ).strip()
        if name.upper() == "Q":
            self.print_menu()
        else:
            result = self.food_list.find_restaurant(name)

            if result:
                console.print(
                    f"[light green]Found restaurant - Name = [purple]{result.get_name()}[/purple]; Category = [purple]{result.get_category()}[/purple]\n"
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
                    print(
                        f"Edited to: {new_food.get_name()}: {new_food.get_category()}"
                    )
                else:
                    print("Returning to menu\n")

            else:
                console.print("[red]No restaurant with this name found.")

    def delete_restaurant(self) -> None:
        """MENU OPT 5 MAIN: Facilitates deleting restaurants with a specific name."""

        name = console.input(
            "[bold green]Provide name of restaurant you want to delete, press [red]Q[/red] to quit: "
        ).strip()
        if name.upper() == "Q":
            self.print_menu()
        result = self.food_list.find_restaurant(name)

        if result:
            self.food_list.delete_restaurant(result)
        else:
            console.print(f"[red]Cannot find restaurant with name {name}\n")


def main():
    restaurant_chooser = FoodController()
    restaurant_chooser.food_picker_main()


if __name__ == "__main__":
    main()
