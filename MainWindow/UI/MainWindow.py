# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_mw_main_window(object):
    def setupUi(self, mw_main_window):
        if not mw_main_window.objectName():
            mw_main_window.setObjectName(u"mw_main_window")
        mw_main_window.resize(720, 526)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mw_main_window.sizePolicy().hasHeightForWidth())
        mw_main_window.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/Main/witch-hat.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        mw_main_window.setWindowIcon(icon)
        self.centralwidget = QWidget(mw_main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Avenir"])
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        self.centralwidget.setFont(font)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.w_output = QWidget(self.centralwidget)
        self.w_output.setObjectName(u"w_output")
        font1 = QFont()
        font1.setFamilies([u"Avenir"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.w_output.setFont(font1)
        self.gridLayout = QGridLayout(self.w_output)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.label_title = QLabel(self.w_output)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setFont(font)

        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 1)

        self.label_pic = QLabel(self.w_output)
        self.label_pic.setObjectName(u"label_pic")
        self.label_pic.setPixmap(QPixmap(u":/Main/witch-hat_small.png"))

        self.gridLayout.addWidget(self.label_pic, 0, 2, 1, 1)

        self.label_subtitle = QLabel(self.w_output)
        self.label_subtitle.setObjectName(u"label_subtitle")

        self.gridLayout.addWidget(self.label_subtitle, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.w_output, 0, 0, 1, 1)

        self.tab_input = QTabWidget(self.centralwidget)
        self.tab_input.setObjectName(u"tab_input")
        self.tab_input.setFont(font1)
        self.tab_ingredients = QWidget()
        self.tab_ingredients.setObjectName(u"tab_ingredients")
        self.verticalLayout = QVBoxLayout(self.tab_ingredients)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table_ingredients = QTableWidget(self.tab_ingredients)
        if (self.table_ingredients.columnCount() < 4):
            self.table_ingredients.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_ingredients.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_ingredients.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_ingredients.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_ingredients.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_ingredients.setObjectName(u"table_ingredients")
        self.table_ingredients.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout.addWidget(self.table_ingredients)

        self.tab_input.addTab(self.tab_ingredients, "")
        self.tab_recipes = QWidget()
        self.tab_recipes.setObjectName(u"tab_recipes")
        self.tab_input.addTab(self.tab_recipes, "")

        self.gridLayout_2.addWidget(self.tab_input, 1, 0, 1, 1)

        mw_main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mw_main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 720, 36))
        mw_main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mw_main_window)
        self.statusbar.setObjectName(u"statusbar")
        mw_main_window.setStatusBar(self.statusbar)

        self.retranslateUi(mw_main_window)

        self.tab_input.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mw_main_window)
    # setupUi

    def retranslateUi(self, mw_main_window):
        mw_main_window.setWindowTitle(QCoreApplication.translate("mw_main_window", u"Recetario", None))
        self.label_title.setText(QCoreApplication.translate("mw_main_window", u"Welcome!", None))
        self.label_pic.setText("")
        self.label_subtitle.setText("")
        ___qtablewidgetitem = self.table_ingredients.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mw_main_window", u"Name", None));
        ___qtablewidgetitem1 = self.table_ingredients.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mw_main_window", u"Grams Per Unit", None));
        ___qtablewidgetitem2 = self.table_ingredients.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mw_main_window", u"Calories Per Unit", None));
        ___qtablewidgetitem3 = self.table_ingredients.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("mw_main_window", u"Category", None));
        self.tab_input.setTabText(self.tab_input.indexOf(self.tab_ingredients), QCoreApplication.translate("mw_main_window", u"Ingredients", None))
        self.tab_input.setTabText(self.tab_input.indexOf(self.tab_recipes), QCoreApplication.translate("mw_main_window", u"Recipes", None))
    # retranslateUi

