# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(375, 384)
        Register.setMinimumSize(QSize(375, 384))
        Register.setMaximumSize(QSize(375, 384))
        Register.setStyleSheet(u"background-color: rgb(2, 84, 100);")
        self.centralwidget = QWidget(Register)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(375, 384))
        self.centralwidget.setMaximumSize(QSize(375, 384))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName(u"loginButton")

        self.gridLayout.addWidget(self.loginButton, 13, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_10, 4, 2, 1, 1)

        self.usernameLineEdit = QLineEdit(self.centralwidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setMinimumSize(QSize(221, 18))
        self.usernameLineEdit.setMaximumSize(QSize(2000, 30))
        font = QFont()
        font.setPointSize(12)
        self.usernameLineEdit.setFont(font)
        self.usernameLineEdit.setStyleSheet(u"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(3, 116, 136);")
        self.usernameLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.usernameLineEdit, 6, 1, 1, 3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 0, 4, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 2, 3)

        self.submitButton = QPushButton(self.centralwidget)
        self.submitButton.setObjectName(u"submitButton")

        self.gridLayout.addWidget(self.submitButton, 13, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 3)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 8, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.passwordLineEdit = QLineEdit(self.centralwidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setMaximumSize(QSize(16777215, 30))
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(3, 116, 136);")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.passwordLineEdit, 9, 1, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 14, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_11, 10, 2, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_12, 12, 2, 1, 1)

        self.repasswordLineEdit = QLineEdit(self.centralwidget)
        self.repasswordLineEdit.setObjectName(u"repasswordLineEdit")
        self.repasswordLineEdit.setFont(font)
        self.repasswordLineEdit.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(3, 116, 136);")
        self.repasswordLineEdit.setEchoMode(QLineEdit.Password)
        self.repasswordLineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.repasswordLineEdit, 11, 1, 1, 3)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        Register.setCentralWidget(self.centralwidget)

        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"MainWindow", None))
        self.loginButton.setText(QCoreApplication.translate("Register", u"Login", None))
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("Register", u"Username", None))
        self.label.setText(QCoreApplication.translate("Register", u"<html><head/><body><p align=\"center\"><img src=\"Utilities/account-25.png\"/></p></body></html>", None))
        self.submitButton.setText(QCoreApplication.translate("Register", u"Submit", None))
        self.label_2.setText(QCoreApplication.translate("Register", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Register</span></p></body></html>", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("Register", u"Password", None))
        self.repasswordLineEdit.setPlaceholderText(QCoreApplication.translate("Register", u"Re-Password", None))
    # retranslateUi

