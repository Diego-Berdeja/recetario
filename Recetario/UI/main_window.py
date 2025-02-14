# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)
import icons_rc

class Ui_win_main(object):
    def setupUi(self, win_main):
        if not win_main.objectName():
            win_main.setObjectName(u"win_main")
        win_main.resize(702, 674)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(win_main.sizePolicy().hasHeightForWidth())
        win_main.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/Main/witch-hat.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        win_main.setWindowIcon(icon)
        self.centralwidget = QWidget(win_main)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Avenir"])
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        self.centralwidget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.box_output = QGroupBox(self.centralwidget)
        self.box_output.setObjectName(u"box_output")
        font1 = QFont()
        font1.setFamilies([u"Avenir"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.box_output.setFont(font1)
        self.gridLayout = QGridLayout(self.box_output)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_title = QLabel(self.box_output)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setFont(font)

        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 1)

        self.label_subtitle = QLabel(self.box_output)
        self.label_subtitle.setObjectName(u"label_subtitle")

        self.gridLayout.addWidget(self.label_subtitle, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.box_output)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout.addWidget(self.widget)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/Main/witch-hat.png"))

        self.verticalLayout.addWidget(self.label)

        self.tab_input = QTabWidget(self.centralwidget)
        self.tab_input.setObjectName(u"tab_input")
        self.tab_input.setFont(font1)
        self.tab_rec = QWidget()
        self.tab_rec.setObjectName(u"tab_rec")
        self.tab_input.addTab(self.tab_rec, "")
        self.tab_ing = QWidget()
        self.tab_ing.setObjectName(u"tab_ing")
        self.tab_input.addTab(self.tab_ing, "")

        self.verticalLayout.addWidget(self.tab_input)

        win_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(win_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 702, 36))
        win_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(win_main)
        self.statusbar.setObjectName(u"statusbar")
        win_main.setStatusBar(self.statusbar)

        self.retranslateUi(win_main)

        self.tab_input.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(win_main)
    # setupUi

    def retranslateUi(self, win_main):
        win_main.setWindowTitle(QCoreApplication.translate("win_main", u"Recetario", None))
        self.box_output.setTitle(QCoreApplication.translate("win_main", u"Recetario", None))
        self.label_title.setText(QCoreApplication.translate("win_main", u"Title", None))
        self.label_subtitle.setText(QCoreApplication.translate("win_main", u"Subtitle", None))
        self.label.setText("")
        self.tab_input.setTabText(self.tab_input.indexOf(self.tab_rec), QCoreApplication.translate("win_main", u"Recetario", None))
        self.tab_input.setTabText(self.tab_input.indexOf(self.tab_ing), QCoreApplication.translate("win_main", u"Ingredient database", None))
    # retranslateUi

