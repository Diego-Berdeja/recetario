from classes import Ingredient, Recipe, Recetario, Wizard
from PyQt6 import QtWidgets

import random, pickle

def populator():
    # We define a few basic Ingredient instances.
    apple = Ingredient(name='Apple', pieces=1, grams=150, calories=52, category=['fruit'])
    pear = Ingredient(name='Pear', pieces=1, grams=150, calories=100, category=['fruit'])

    # We create, populate, and pickle a Recipe instance to use as a master collection of ingredients.
    ingredient_list = Recipe(name='', serves=1, ingredient_list=[], category=[], complexity='')
    ingredient_list.add_ingredient(apple)
    ingredient_list.add_ingredient(pear)
    with open('ingredients.pickle', 'wb') as file:
        pickle.dump(ingredient_list, file)

    # We define a few basic Recipe instances.
    caramelised_pears = Recipe(name='Caramelised Pears',
                               serves=2,
                               ingredient_list=[Ingredient(name='Pear',pieces=2, grams=300,calories=200,
                                                                    category=['fruit'])],category=[],complexity='')
    caramelised_apples = Recipe(name='Caramelised Apples',
                               serves=2,
                               ingredient_list=[Ingredient(name='Apple',pieces=2, grams=300,calories=104,
                                                                    category=['fruit'])],category=[],complexity='')

    # We create, populate, and pickle a Recetario instance to use as a master collection of recipes.
    recipe_list = Recetario(name='', recipes=[], people=1)
    recipe_list.add_recipe(caramelised_pears)
    recipe_list.add_recipe(caramelised_apples)
    with open('recipes.pickle', 'wb') as file:
        pickle.dump(recipe_list, file)

    return(ingredient_list,recipe_list)

master=populator()

master[0].list_ingredients()