class Ingredient:
    """Class for ingredients. Essentially a dictionary. Contains grams per unit, calories per unit,
    and a list of category keywords."""

    def __init__(self, name: str, grams: float, calories: float, category: list):
        self.name = name
        self.grams = grams
        self.calories = calories
        self.category = category

class Recipe:
    """Class for a recipe."""

    def __init__(self, name: str, serves: int, ingredient_list: list, category: str, complexity: str):
        self.name = name
        self.serves = serves
        self.ingredient_list = ingredient_list
        self.category = category
        self.complexity = complexity

    def add_ingredient(self, ingredient):
        self.ingredient_list.append(ingredient)
        print(f'\'{ingredient.name}\' added to \'{self.name}\'.')

class Recetario:
    """Class for recipe book."""

    def __init__(self, name: str, recepies: list, people: int):
        self.name = name
        self.recepies = recepies
        self.people = people

    def add_recipe(self, entry):
        self.recepies.append(entry)
        print(f'\'{entry.name}\' added to \'{self.name}\'.')

    def remove_recipe(self, entry):
        for item in self.recepies:
            if entry.name == item.name:
                self.recepies.remove(entry)
                print(f'\'{item.name}\' removed from \'{self.name}\'.')
                return 0
        print(f'No entries matching \'{entry.name}\' found in {self.name}\'.')