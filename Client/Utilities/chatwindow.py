# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chatwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QWidget)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(410, 410)
        MainWindow.setMinimumSize(QSize(410, 410))
        MainWindow.setMaximumSize(QSize(410, 410))
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
        MainWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u":/icons/icons/chat.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.messageEdit = QPlainTextEdit(self.centralwidget)
        self.messageEdit.setObjectName(u"messageEdit")
        self.messageEdit.setGeometry(QRect(10, 320, 331, 61))
        self.messageEdit.setStyleSheet(u"QLineEdit {\n"
"border: 1px solid rgb(20,26,31);\n"
"border-radius: 40px;}")
        self.sendButton = QPushButton(self.centralwidget)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(350, 330, 41, 41))
        self.sendButton.setStyleSheet(u"QPushButton {background-color: rgb(4, 154, 180);font-size: 13px;border: none;border-radius: 19px;}QPushButton:hover {background-color: rgb(4, 191, 224);}")
        icon1 = QIcon()
        icon1.addFile(u"paper-airplane5825.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sendButton.setIcon(icon1)
        self.sendButton.setIconSize(QSize(48, 48))
        self.chat = QScrollArea(self.centralwidget)
        self.chat.setObjectName(u"chat")
        self.chat.setGeometry(QRect(9, 9, 391, 301))
        self.chat.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 389, 299))
        self.chat.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SadGram", None))
        self.messageEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your message", None))
        self.sendButton.setText("")
    # retranslateUi

