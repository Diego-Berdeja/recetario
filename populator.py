from classes import Ingredient, Recipe, Recetario
import random, pickle

def main():
    # We create a list of ingredients and pickle it into a file.
    ingredient_list = [
    Ingredient('Apple', 150, 52, ['fruit']),
    Ingredient('Pear', 150, 100, ['fruit'])]

    with open('ingredients.pickle', 'wb') as file:
        pickle.dump(ingredient_list, file)

    # We create a list of recipes and pickle it into a file.
    recipe_list = [
        Recipe('Caramelised Pears', 2, [[2, 'p', 'Pear']], 'dessert', 'easy'),
        Recipe('Caramelised Apples', 3, [[4, 'p', 'Apple']], 'dessert', 'easy')]

    with open('recipes.pickle', 'wb') as file:
        pickle.dump(recipe_list, file)

if __name__ == '__main__':
    main()