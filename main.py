from classes import Ingredient, Recipe, Recetario
from PyQt6 import QtWidgets

import random, pickle, populator

# Load ingredients, recipes, and recetarios from database files.
with open('ingredients.pickle','rb') as file:
    ingredients = pickle.load(file)
with open('recipes.pickle','rb') as file:
    recipes = pickle.load(file)

print(recipes)
recipes[1].list_ingredients()