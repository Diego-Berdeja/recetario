import sys, pickle
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from classes import Ingredient, Recipe, Recetario, MainWindow, populator



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv) # In QT we must always have an app object. There can only be one. This launches the Python Launcher.

    window = MainWindow() # Note window is not a QT Window object, but rather our own inherited object.
    window.show()
    window.recipes.list_recipes()

    window.save_to_file(window.recipes) # We save to file before quitting.
    sys.exit(app.exec()) # The .exec starts the app loop and waits until exit is called.