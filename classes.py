########################################################################################################################
class Ingredient:
    """Class for ingredients. Essentially a dictionary. Contains grams per unit, calories per unit,
    and a list of category keywords."""

    def __init__(self, name: str, grams: float, calories: float, category: list):
        self.name = name
        self.grams = grams
        self.calories = calories
        self.category = category





########################################################################################################################
class Recipe:
    """Class for a recipe."""

    def __init__(self, name: str, serves: int, ingredient_list: list, category: str, complexity: str):
        self.name = name
        self.serves = serves
        self.ingredient_list = ingredient_list
        self.category = category
        self.complexity = complexity

    def list_ingredients(self):
        for item in self.ingredient_list:
            if item[1] == 'p':
                print(f'{item[0]} pieces of {item[2].lower()}.')
            else:
                print(f'{item[0]} grams of {item[2].lower()}')

    def add_ingredient(self, ingredient: Ingredient):
        if ingredient not in self.ingredient_list:
            self.ingredient_list.append(ingredient)
            print(f'\'{ingredient.name}\' added to \'{self.name}\'.')
        else:
            print(f'\'{ingredient.name}\' already listed in \'{self.name}\'.')

    def remove_ingredient(self, ingredient: Ingredient):
        if ingredient in self.ingredient_list:
            self.ingredient_list.remove(ingredient)
            print(f'\'{ingredient.name}\' removed from \'{self.name}\'.')
        else:
            print(f'\'{ingredient.name}\' not listed in \'{self.name}\'.')

    def rescale_recipe(self, new_serves: int):
        new_list = []
        for item in self.ingredient_list:
            new_item = item
            new_item[0] = (new_serves / self.serves) * item[0]
        self.ingredient_list = new_list






########################################################################################################################
class Recetario:
    """Class for recipe book."""

    def __init__(self, name: str, recipes: list, people: int):
        self.name = name
        self.recipes = recipes
        self.people = people

    def add_recipe(self, entry):
        self.recipes.append(entry)
        print(f'\'{entry.name}\' added to \'{self.name}\'.')

    def remove_recipe(self, entry):
        for item in self.recipes:
            if entry.name == item.name:
                self.recipes.remove(entry)
                print(f'\'{item.name}\' removed from \'{self.name}\'.')
                return 0
            print(f'No entries matching \'{entry.name}\' found in {self.name}\'.')





########################################################################################################################
class Wizard(Recipe, Recetario):
    """Recetario, recipe, and ingredient editor."""
    def __init__(self, master_ingredients: list, master_recipes: list):
        Recipe.__init__(self, name='master', serves=1, ingredient_list=master_ingredients, category='master',
                        complexity='master')
        Recetario.__init__(self, name='master', recipes=master_recipes, people=1)