# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        if not Dashboard.objectName():
            Dashboard.setObjectName(u"Dashboard")
        Dashboard.resize(275, 433)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(2, 84, 100, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        Dashboard.setPalette(palette)
        self.centralwidget = QWidget(Dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.convoList = QListView(self.centralwidget)
        self.convoList.setObjectName(u"convoList")
        self.convoList.setMaximumSize(QSize(200, 16777215))
        palette1 = QPalette()
        brush3 = QBrush(QColor(229, 124, 35, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush3)
        brush4 = QBrush(QColor(232, 170, 66, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush4)
        self.convoList.setPalette(palette1)
        font = QFont()
        font.setPointSize(14)
        self.convoList.setFont(font)
        self.convoList.setSelectionMode(QAbstractItemView.SingleSelection)

        self.horizontalLayout_2.addWidget(self.convoList)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMinimumSize(QSize(0, 20))
        self.addButton.setMaximumSize(QSize(16777215, 15))
        self.addButton.setStyleSheet(u"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(4, 154, 180);")

        self.verticalLayout.addWidget(self.addButton)

        self.newConvoInput = QLineEdit(self.centralwidget)
        self.newConvoInput.setObjectName(u"newConvoInput")
        self.newConvoInput.setMinimumSize(QSize(0, 20))
        self.newConvoInput.setStyleSheet(u"background-color: rgb(232, 170, 66);\n"
"border: none;")

        self.verticalLayout.addWidget(self.newConvoInput)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setMinimumSize(QSize(30, 20))
        self.deleteButton.setMaximumSize(QSize(16777215, 15))
        self.deleteButton.setStyleSheet(u"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(4, 154, 180);")

        self.verticalLayout.addWidget(self.deleteButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        Dashboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dashboard)

        QMetaObject.connectSlotsByName(Dashboard)
    # setupUi

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"Todo", None))
        self.addButton.setText(QCoreApplication.translate("Dashboard", u"Add", None))
        self.deleteButton.setText(QCoreApplication.translate("Dashboard", u"Delete", None))
    # retranslateUi

