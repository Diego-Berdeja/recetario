from pathlib import Path
import pickle
########################################################################################################################





########################################################################################################################
class Ingredient:
    """Class for ingredients. Essentially a dictionary. Contains grams per unit, calories per unit,
    and a list of category keywords."""

    def __init__(self, name: str, pieces: int = 1, grams: float = 1, calories: float = 1, category: list = []):
        self.name = name
        self.pieces = pieces
        self.grams = grams
        self.calories = calories
        self.category = category
########################################################################################################################





########################################################################################################################
class Recipe:
    """Class for a recipe."""

    def __init__(self, name: str, serves: int = 1, ingredient_list: list = [], category: list = [], complexity: str = ''):
        self.name = name
        self.serves = serves
        self.ingredient_list = ingredient_list
        self.category = category
        self.complexity = complexity

    def list_ingredients(self):
        for item in self.ingredient_list:
            if item.pieces > 20:
                if int(item.grams) == 1:
                    print(f'{int(item.grams)} gram of {item.name.lower()}.')
                else:
                    print(f'{int(item.grams)} grams of {item.name.lower()}.')
            else:
                if round(item.pieces,1) == 1:
                    print(f'{round(item.pieces,1)} {item.name.lower()}.')
                else:
                    print(f'{round(item.pieces,1)} pieces of {item.name.lower()}.')

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
            new_item.pieces = (new_serves / self.serves) * item.pieces
            new_item.grams = (new_serves / self.serves) * item.grams
            new_item.calories = (new_serves / self.serves) * item.calories
            new_list.append(new_item)
        self.ingredient_list = new_list
########################################################################################################################





########################################################################################################################
class Recetario:
    """Class for recipe book."""
    def __init__(self, name: str, recipes: dict = {}, people: int = 1):
        self.name = name
        self.recipes = recipes
        self.people = people

    def list_recipes(self):
        for item in self.recipes:
            print(item)

    def add_recipe(self, entry: Recipe):
        self.recipes[entry.name] = entry
        print(f'\'{entry.name}\' added to \'{self.name}\'.')

    def remove_recipe(self, entry: Recipe):
        try:
            self.recipes.pop(entry.name.lower())
            print(f'\'{entry.name}\' removed from \'{self.name}\'.')
        except:
            print(f'No entries matching \'{entry.name}\' found in {self.name}\'.')

    def rescale_all_recipes(self, new_serves: int):
        new_list = {}
        for key, value in self.recipes.items():
            new_list[key] = value
            new_list[key].rescale_recipe(new_serves=new_serves)
        self.recipes = new_list
########################################################################################################################




########################################################################################################################
class Wizard(Recetario):
    """Recetario, recipe, and ingredient editor."""
    def __init__(self, master_recipes: Recetario):
        Recetario.__init__(self, name='master', recipes=master_recipes.recipes, people=1)
########################################################################################################################





########################################################################################################################
def populator():
    # We define a few basic Ingredient instances.
    apple = Ingredient(name='Apple', pieces=1, grams=150, calories=52, category=['fruit'])
    pear = Ingredient(name='Pear', pieces=1, grams=150, calories=100, category=['fruit'])
    # We define a few basic Recipe instances.
    caramelised_pears = Recipe(name='Caramelised Pears',
                               serves=2,
                               ingredient_list=[Ingredient(name='Pear', pieces=2, grams=300, calories=200,
                                                           category=['fruit'])], category=[], complexity='')
    caramelised_apples = Recipe(name='Caramelised Apples',
                                serves=2,
                                ingredient_list=[Ingredient(name='Apple', pieces=2, grams=300, calories=104,
                                                            category=['fruit'])], category=[], complexity='')

    # We create and populate a Recipe instance to use as a master collection of ingredients.
    ingredient_master = Recipe(name='master')
    ingredient_master.add_ingredient(apple)
    ingredient_master.add_ingredient(pear)
    # We create and populate a Recetario instance to use as a master collection of recipes. We add the master list of
    # ingredients.
    recipe_master = Recetario(name='master')
    recipe_master.add_recipe(ingredient_master)
    recipe_master.add_recipe(caramelised_pears)
    recipe_master.add_recipe(caramelised_apples)
    # We pickle the master Recetario into a master file.
    with open('master.pickle', 'wb') as file:
        # noinspection PyTypeChecker
        pickle.dump(recipe_master, file)
