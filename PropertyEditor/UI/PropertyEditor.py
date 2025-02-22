# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PropertyEditor.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QLabel, QRadioButton,
    QSizePolicy, QWidget)

class Ui_dialog_property_editor(object):
    def setupUi(self, dialog_property_editor):
        if not dialog_property_editor.objectName():
            dialog_property_editor.setObjectName(u"dialog_property_editor")
        dialog_property_editor.resize(283, 582)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog_property_editor.sizePolicy().hasHeightForWidth())
        dialog_property_editor.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(dialog_property_editor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_buttons = QWidget(dialog_property_editor)
        self.widget_buttons.setObjectName(u"widget_buttons")
        self.formLayout = QFormLayout(self.widget_buttons)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.name = QRadioButton(self.widget_buttons)
        self.name.setObjectName(u"name")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.name)

        self.calories = QRadioButton(self.widget_buttons)
        self.calories.setObjectName(u"calories")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.calories)

        self.carbohydrates = QRadioButton(self.widget_buttons)
        self.carbohydrates.setObjectName(u"carbohydrates")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.carbohydrates)

        self.cholesterol = QRadioButton(self.widget_buttons)
        self.cholesterol.setObjectName(u"cholesterol")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.cholesterol)

        self.fibre = QRadioButton(self.widget_buttons)
        self.fibre.setObjectName(u"fibre")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.fibre)

        self.protein = QRadioButton(self.widget_buttons)
        self.protein.setObjectName(u"protein")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.protein)

        self.sugar = QRadioButton(self.widget_buttons)
        self.sugar.setObjectName(u"sugar")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.sugar)

        self.total_fat = QRadioButton(self.widget_buttons)
        self.total_fat.setObjectName(u"total_fat")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.total_fat)

        self.monosaturated_fat = QRadioButton(self.widget_buttons)
        self.monosaturated_fat.setObjectName(u"monosaturated_fat")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.monosaturated_fat)

        self.polysaturated_fat = QRadioButton(self.widget_buttons)
        self.polysaturated_fat.setObjectName(u"polysaturated_fat")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.polysaturated_fat)

        self.saturated_fat = QRadioButton(self.widget_buttons)
        self.saturated_fat.setObjectName(u"saturated_fat")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.saturated_fat)

        self.calcium = QRadioButton(self.widget_buttons)
        self.calcium.setObjectName(u"calcium")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.calcium)

        self.iron = QRadioButton(self.widget_buttons)
        self.iron.setObjectName(u"iron")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.iron)

        self.potassium = QRadioButton(self.widget_buttons)
        self.potassium.setObjectName(u"potassium")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.potassium)

        self.sodium = QRadioButton(self.widget_buttons)
        self.sodium.setObjectName(u"sodium")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.sodium)

        self.vitamin_a = QRadioButton(self.widget_buttons)
        self.vitamin_a.setObjectName(u"vitamin_a")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.vitamin_a)

        self.vitamin_b12 = QRadioButton(self.widget_buttons)
        self.vitamin_b12.setObjectName(u"vitamin_b12")

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.vitamin_b12)

        self.vitamin_b6 = QRadioButton(self.widget_buttons)
        self.vitamin_b6.setObjectName(u"vitamin_b6")

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.vitamin_b6)

        self.vitamin_c = QRadioButton(self.widget_buttons)
        self.vitamin_c.setObjectName(u"vitamin_c")

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.vitamin_c)

        self.vitamin_e = QRadioButton(self.widget_buttons)
        self.vitamin_e.setObjectName(u"vitamin_e")

        self.formLayout.setWidget(20, QFormLayout.LabelRole, self.vitamin_e)

        self.vitamin_k = QRadioButton(self.widget_buttons)
        self.vitamin_k.setObjectName(u"vitamin_k")

        self.formLayout.setWidget(21, QFormLayout.LabelRole, self.vitamin_k)

        self.label = QLabel(self.widget_buttons)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)


        self.gridLayout.addWidget(self.widget_buttons, 0, 0, 2, 1)

        self.buttonBox = QDialogButtonBox(dialog_property_editor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 0, 1, 1, 1)


        self.retranslateUi(dialog_property_editor)
        self.buttonBox.accepted.connect(dialog_property_editor.accept)
        self.buttonBox.rejected.connect(dialog_property_editor.reject)

        QMetaObject.connectSlotsByName(dialog_property_editor)
    # setupUi

    def retranslateUi(self, dialog_property_editor):
        dialog_property_editor.setWindowTitle(QCoreApplication.translate("dialog_property_editor", u"Property Editor", None))
        self.name.setText(QCoreApplication.translate("dialog_property_editor", u" Name", None))
        self.calories.setText(QCoreApplication.translate("dialog_property_editor", u"Calories", None))
        self.carbohydrates.setText(QCoreApplication.translate("dialog_property_editor", u"Carbohydrates", None))
        self.cholesterol.setText(QCoreApplication.translate("dialog_property_editor", u"Cholesterol", None))
        self.fibre.setText(QCoreApplication.translate("dialog_property_editor", u"Fibre", None))
        self.protein.setText(QCoreApplication.translate("dialog_property_editor", u"Protein", None))
        self.sugar.setText(QCoreApplication.translate("dialog_property_editor", u"Sugar", None))
        self.total_fat.setText(QCoreApplication.translate("dialog_property_editor", u"Total Fat", None))
        self.monosaturated_fat.setText(QCoreApplication.translate("dialog_property_editor", u"Mono-saturated Fat", None))
        self.polysaturated_fat.setText(QCoreApplication.translate("dialog_property_editor", u"Poly-saturated Fat", None))
        self.saturated_fat.setText(QCoreApplication.translate("dialog_property_editor", u"Saturated Fat", None))
        self.calcium.setText(QCoreApplication.translate("dialog_property_editor", u"Calcium", None))
        self.iron.setText(QCoreApplication.translate("dialog_property_editor", u"Iron", None))
        self.potassium.setText(QCoreApplication.translate("dialog_property_editor", u"Potassium", None))
        self.sodium.setText(QCoreApplication.translate("dialog_property_editor", u"Sodium", None))
        self.vitamin_a.setText(QCoreApplication.translate("dialog_property_editor", u"Vitamin A", None))
        self.vitamin_b12.setText(QCoreApplication.translate("dialog_property_editor", u"Vitamin B12", None))
        self.vitamin_b6.setText(QCoreApplication.translate("dialog_property_editor", u"Vitamin B6", None))
        self.vitamin_c.setText(QCoreApplication.translate("dialog_property_editor", u"Vitamin C", None))
        self.vitamin_e.setText(QCoreApplication.translate("dialog_property_editor", u"Vitamin E", None))
        self.vitamin_k.setText(QCoreApplication.translate("dialog_property_editor", u"Vitamin K", None))
        self.label.setText(QCoreApplication.translate("dialog_property_editor", u"Properties:", None))
    # retranslateUi

