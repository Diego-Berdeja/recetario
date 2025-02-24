import sys, pickle
from icecream import ic
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
# We import the widget classes generated by QT Designer, so we can inherit them and modify them below.
from MainWindow.UI.MainWindow import Ui_mw_main_window
from PropertyEditor.UI.PropertyEditor import Ui_dialog_property_editor
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

    def __init__(self, name: str, serves: int = 1, ingredient_list: list = [], category: list = [],
                 complexity: str = ''):
        self.name = name
        self.serves = serves
        self.ingredient_list = ingredient_list
        self.category = category
        self.complexity = complexity

        self.output_signal=qtc.Signal()

    def list_ingredients(self):
        output = []
        for item in self.ingredient_list:
            if item.pieces > 20:
                if int(item.grams) == 1:
                    output.append(f'{int(item.grams)} gram of {item.name.lower()}.')
                else:
                    output.append(f'{int(item.grams)} grams of {item.name.lower()}.')
            else:
                if round(item.pieces,1) == 1:
                    output.append(f'{round(item.pieces,1)} {item.name.lower()}.')
                else:
                    output.append(f'{round(item.pieces,1)} pieces of {item.name.lower()}.')
        self.output_signal.emit(output)

    def add_ingredient(self, ingredient: Ingredient):
        output = []
        if ingredient not in self.ingredient_list:
            self.ingredient_list.append(ingredient)
            output.append(f'\'{ingredient.name}\' added to \'{self.name}\'.')
        else:
            output.append(f'\'{ingredient.name}\' already listed in \'{self.name}\'.')
        self.output_signal.emit(output)

    def remove_ingredient(self, ingredient: Ingredient):
        output = []
        if ingredient in self.ingredient_list:
            self.ingredient_list.remove(ingredient)
            output.append(f'\'{ingredient.name}\' removed from \'{self.name}\'.')
        else:
            output.append(f'\'{ingredient.name}\' not listed in \'{self.name}\'.')
        self.output_signal.emit(output)

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
        except FileNotFoundError:
            print(f'No entries matching \'{entry.name}\' found in {self.name}\'.')

    def rescale_all_recipes(self, new_serves: int):
        new_list = {}
        for key, value in self.recipes.items():
            new_list[key] = value
            new_list[key].rescale_recipe(new_serves=new_serves)
        self.recipes = new_list
########################################################################################################################




########################################################################################################################
class MainWindow(qtw.QMainWindow, Ui_mw_main_window, Ui_dialog_property_editor):
    # Defines a new class based on the class created by QT Designer.
    """Recetario, recipe, and ingredient editor."""
    def __init__(self):
        # Note Ui_win_main has no initializer: only two functions.
        super().__init__()
        self.setupUi(self)
        # setupUI() is one of them: it sets up the MainWindow UI, which inherits from the QMainWindow class.
        (self.recipes, self.properties) = self.load_from_file()
        # We unpickle database into Recetario object.
        self.display_ingredient_list(self.recipes.recipes['master'].ingredient_list)
        # We display the master ingredient list in the corresponding tab.
        self.show() # We show our main window.
        # We connect signals to slots.
        self.pb_edit.pressed.connect(self.property_editor)

    @qtc.Slot()
    def save_to_file(self, recipes: Recetario, properties: dict, name='master.pickle'):
        with open(name, 'wb') as file:
            # noinspection PyTypeChecker
            pickle.dump((recipes, properties), file)
            print(f'Saved data to \'{name}\'.')

    @qtc.Slot()
    def load_from_file(self, name='master.pickle') -> (Recetario, dict):
        try:
            with open(name, 'rb') as file:
                # noinspection PyTypeChecker
                 return pickle.load(file)
        except FileNotFoundError:
            print(f'File \'{name}\' not found.')
            return Recetario('master')

    # This slot populates the Ingredients tab with whatever list of Ingredients it is given.
    @qtc.Slot()
    def display_ingredient_list(self, ingredient_list: list):
        row = 0
        self.table_ingredients.setRowCount(len(ingredient_list))
        for ingredient in ingredient_list:
            self.table_ingredients.setItem(row, 0, qtw.QTableWidgetItem(str(ingredient.name)))
            self.table_ingredients.setItem(row, 1, qtw.QTableWidgetItem(str(ingredient.grams) + 'g'))
            self.table_ingredients.setItem(row, 2, qtw.QTableWidgetItem(str(ingredient.calories) + ' calories'))
            category = ''
            for item in ingredient.category:
                category = category + item + ', '
            category = list(category)
            category.pop()
            category.pop()
            category = ''.join(category)
            self.table_ingredients.setItem(row, 3, qtw.QTableWidgetItem(category))
            row += 1

    @qtc.Slot()
    def property_editor(self):
        editor_window = PropertyEditor()
        for item in self.properties:
            ic(item)
            if item[1]:
                ic(eval('editor_window.' + item[0].lower() + '.setCheckState(2)'))
            else:
                eval('editor_window.' + item[0].lower() + '.setCheckState(0)')
        editor_window.exec()
########################################################################################################################

########################################################################################################################
class PropertyEditor(qtw.QDialog, Ui_dialog_property_editor):
    """Property editor that allows the user to select what properties of a given ingredient list to choose."""
    def __init__(self):
        super().__init__()
        self.setupUi(self)



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
