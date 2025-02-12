########################################################################################################################
class Ingredient:
    """Class for ingredients. Essentially a dictionary. Contains grams per unit, calories per unit,
    and a list of category keywords."""

    def __init__(self, name: str, pieces: int, grams: float, calories: float, category: list):
        self.name = name
        self.pieces = pieces
        self.grams = grams
        self.calories = calories
        self.category = category





########################################################################################################################
class Recipe:
    """Class for a recipe."""

    def __init__(self, name: str, serves: int, ingredient_list: list, category: list, complexity: str):
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
class Recetario:
    """Class for recipe book."""

    def __init__(self, name: str, recipes: list, people: int):
        self.name = name
        self.recipes = recipes
        self.people = people

    def list_recipes(self):
        for item in self.recipes:
            print(f'{item.name}')

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

    def rescale_all_recipes(self, new_serves: int):
        new_list = []
        for item in self.recipes:
            new_recipe = item
            new_recipe.rescale_recipe(new_serves=new_serves)
            new_list.append(new_recipe)
        self.recipes = new_list



########################################################################################################################
class Wizard(Recipe, Recetario):
    """Recetario, recipe, and ingredient editor."""
    def __init__(self, master_ingredients: Recipe, master_recipes: Recetario):
        Recipe.__init__(self, name='master', serves=1, ingredient_list=master_ingredients.ingredient_list,
                        category=['master'],complexity='master')
        Recetario.__init__(self, name='master', recipes=master_recipes.recipes, people=1)