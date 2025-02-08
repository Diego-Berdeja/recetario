from classes import Ingredient, Recipe, Recetario
import random, pickle

# Here we create a Recipe object whose ingredient list contains our starting list of ingredients. We then pickle it.

ingredient_list = Recipe('', 0, [], '','')

ingredient_list.add_ingredient(Ingredient('Apple', 150, 52, 'fruit'))
ingredient_list.add_ingredient(Ingredient('Pear', 150, 100, 'fruit'))

with open('ingredients.pickle', 'wb') as file:
    pickle.dump(ingredient_list, file)


# Here we create a Recetario object whose recipe list contains our starting list of recipes.

recipe_list = Recetario('', [], 0)

recipe_list.add_recipe(Recipe('Caramelised Pears', 2, [
    [2, 'p', 'Pear']
], 'dessert', 'easy'))
recipe_list.add_recipe(Recipe('Caramelised Apples', 3, [
    [4, 'p', 'Apple']
], 'dessert', 'easy'))

with open('recipes.pickle', 'wb') as file:
    pickle.dump(recipe_list, file)