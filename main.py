import sys, pickle
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from classes import Ingredient, Recipe, Recetario, MainWindow, populator

# We define a list of possible properties.
PROPERTIES = {
    'Calcium': True,
    'Calories': True,
    'Carbohydrates': True,
    'Cholesterol': True,
    'Fibre': True,
    'Iron': True,
    'Mono-saturated Fat': True,
    'Name': True,
    'Poly-saturated Fat': True,
    'Potassium': True,
    'Protein': True,
    'Saturated Fat': True,
    'Sodium': True,
    'Sugar': True,
    'Total Fat': True,
    'Vitamin A': True,
    'Vitamin B12': True,
    'Vitamin B6': True,
    'Vitamin C': True,
    'Vitamin E': True,
    'Vitamin K': True
}

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv) # In QT we must always have an app object. There can only be one. This launches the Python Launcher.
    window = MainWindow() # Note window is not a QT Window object, but rather our own inherited object.
    window.save_to_file(window.recipes, window.properties) # We save to file before quitting.
    sys.exit(app.exec()) # The .exec starts the app loop and waits until exit is called.

