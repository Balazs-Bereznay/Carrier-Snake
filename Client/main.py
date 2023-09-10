import sys
from PySide6 import QtWidgets
from PySide6.QtGui import QImage, QPixmap, Qt

from Utilities.login import Ui_Login
from Utilities.register import Ui_Register


class Register(QtWidgets.QMainWindow, Ui_Register):
    def __init__(self, parent=None):
        super(Register, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Register")

        self.submitButton.setStyleSheet("QPushButton {color: white}")
        self.loginButton.setStyleSheet("QPushButton {color: white}")

        self.loginButton.clicked.connect(self.login_button_pressed)
        self.submitButton.clicked.connect(self.submit_button_pressed)

    def login_button_pressed(self):
        self.close()

    def submit_button_pressed(self):
        print(self.usernameLineEdit.text(), self.passwordLineEdit.text(), self.repasswordLineEdit.text())


class Login(QtWidgets.QMainWindow, Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("Login")

        self.submitButton.setStyleSheet("QPushButton {color: white}")
        self.registerButton.setStyleSheet("QPushButton {color: white}")

        self.registerButton.clicked.connect(self.register_button_pressed)
        self.submitButton.clicked.connect(self.submit_button_pressed)

        self.registerWindow = None

    def register_button_pressed(self):

        self.registerWindow = Register(self)
        self.registerWindow.show()

    def submit_button_pressed(self):
        print(self.usernameLineEdit.text(), self.passwordLineEdit.text())


app = QtWidgets.QApplication(sys.argv)

window = Login()
window.show()
app.exec()