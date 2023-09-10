import sys
from PySide6 import QtWidgets

from Utilities.login import Ui_Login
from Utilities.register import Ui_Register
from Utilities.message_handler import RequestHandler


class Register(QtWidgets.QMainWindow, Ui_Register):
    def __init__(self, parent=None):
        super(Register, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Register")

        self.submitButton.setStyleSheet("QPushButton {color: white}")
        self.loginButton.setStyleSheet("QPushButton {color: white}")

        self.loginButton.clicked.connect(self.login_button_pressed)

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

        self.registerWindow.submitButton.clicked.connect(self.register_submit_button_pressed)

        self.registerWindow.show()

    def register_submit_button_pressed(self):

        if self.registerWindow.passwordLineEdit.text() == self.registerWindow.repasswordLineEdit.text():
            print("matching")
            requestHandler.username = self.registerWindow.usernameLineEdit.text()
            requestHandler.password = self.registerWindow.passwordLineEdit.text()
            return_code = requestHandler.register()

            if return_code != 0:
                print("Registration unsuccessful!")
                """TODO: open dialog saying username already taken"""

            else:
                self.registerWindow.close()
                self.usernameLineEdit.setText(requestHandler.username)

        else:
            pass
            """TODO: open dialog saying passwords need to match"""

    def submit_button_pressed(self):
        print(self.usernameLineEdit.text(), self.passwordLineEdit.text())

        requestHandler.username = self.usernameLineEdit.text()
        requestHandler.password = self.passwordLineEdit.text()

        return_code = requestHandler.get_token()

        if return_code != 0:
            print("Login failed")

        else:
            """TODO: open dashboard, close login window"""
            print(f"Logged in!\ntoken: {requestHandler.token}")


app = QtWidgets.QApplication(sys.argv)

requestHandler = RequestHandler()

window = Login()
window.show()
app.exec()