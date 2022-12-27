from enum import Enum

class DishType(Enum):
    starter = 1
    dish = 2
    deseert = 3


class Dish:
    
    def __init__(self, name, preparation_time, dish_type: DishType):
        self.name = name
        self.preparation_time = preparation_time
        self.dish_type = dish_type    
    
    def __gt__(self, other):
        if self.preparation_time > other.preparation_time:
            return True
        else:
            return False
    
    def __lt__(self, other):
        if self.preparation_time < other.preparation_time:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.preparation_time == other.preparation_time:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.preparation_time >= other.preparation_time:
            return True
        else:
            return False

    def __le__(self, other):
        if self.preparation_time <= other.preparation_time:
            return True
        else:
            return False


class Menu:
    
    def __init__(self, name):
        self.name = name
        self.dishes = []
    
    def add_dish(self, dish: Dish):
        self.dishes.append(dish)
    
    def get_starters(self):
        return [dish for dish in self.dishes if dish.dish_type == "starter"]

    def get_dishes(self):
        return [dish for dish in self.dishes if dish.dish_type == "dish"]

    def get_desserts(self):
        return [dish for dish in self.dishes if dish.dish_type == "dessert"]
    
    def get_minimum_preparation_time(self):
        starter_time = min([dish.preparation_time for dish in self.get_starters()]) if len(self.get_starters()) > 0 else 0
        dish_time = min([dish.preparation_time for dish in self.get_dishes()]) if len(self.get_dishes()) > 0 else 0
        dessert_time = min([dish.preparation_time for dish in self.get_desserts()]) if len(self.get_desserts()) > 0 else 0

        return starter_time + dish_time + dessert_time

    def get_maximum_preparation_time(self):
        starter_time = max([dish.preparation_time for dish in self.get_starters()]) if len(self.get_starters()) > 0 else 0
        dish_time = max([dish.preparation_time for dish in self.get_dishes()]) if len(self.get_dishes()) > 0 else 0
        dessert_time = max([dish.preparation_time for dish in self.get_desserts()]) if len(self.get_desserts()) > 0 else 0

        return starter_time + dish_time + dessert_time
    
    def __add__(self, other):
        new_menu = Menu(self.name + ' & ' + other.name)
        for dish in self.dishes + other.dishes:
            new_menu.add_dish(dish)
        return new_menu
    
    def __str__(self):
        text = ""
        
        if len(self.get_starters()) > 0:
            text = text + "STARTER\n"
            for dish in sorted(self.get_starters(), key=lambda x: x.preparation_time):
                text = text + dish.name + '\n'
            text = text + "\n"

        if len(self.get_dishes()) > 0:
            text = text + "DISH\n"
            for dish in sorted(self.get_dishes(), key=lambda x: x.preparation_time):
                text = text + dish.name + '\n'
            text = text + "\n"
            
        if len(self.get_desserts()) > 0:
            text = text + "DESSERT\n"
            for dish in sorted(self.get_desserts(), key=lambda x: x.preparation_time):
                text = text + dish.name + '\n'
        
        return text

















