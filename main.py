from classes import Ingredient, Recipe, Recetario, Wizard, populator
from pathlib import Path
from PySide6 import QtWidgets

import pickle

def main():
    populator()
    with open('master.pickle','rb') as file:
        # noinspection PyTypeChecker
        master_recipes = pickle.load(file)
    wizard = Wizard(master_recipes=master_recipes)
    print(Wizard)

if __name__ == '__main__':
    main()