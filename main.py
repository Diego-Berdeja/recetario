import sys, pickle
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtWidgets import QMainWindow
from classes import Ingredient, Recipe, Recetario, Wizard, populator

from MainWindow.UI.MainWindow import Ui_mw_main_window

class MainWindow(qtw.QMainWindow, Ui_mw_main_window): # Defines a new class based on the class created by QT Designer.
    def __init__(self):
        super().__init__() # Note Ui_win_main has no initializer: only two functions.
        self.setupUi(self) # setupUI() is one of them: it takes in a widget and turns it into a window with your design.
def main() -> Wizard :
    populator()
    with open('master.pickle','rb') as file:
        # noinspection PyTypeChecker
        master_recipes = pickle.load(file)
    wizard = Wizard(master_recipes=master_recipes)
    return wizard

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv) # In QT we must always have an app object. There can only be one.
    window = MainWindow() # Note window is not a QT Window object, but rather our own inherited object.
    window.show()
    wizard = main()
    window.tab_ing. wizard.recipes['master'].list_ingredients()

    sys.exit(app.exec()) # The .exec starts the app loop and waits until exit is called.