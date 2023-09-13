import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QCloseEvent

from Utilities.login import Ui_Login
from Utilities.register import Ui_Register
from Utilities.message_handler import RequestHandler
from Utilities.puller import Puller


class Dashboard(QtWidgets.QMainWindow):
    EVENT = QtCore.Signal(list)
    ERROR = QtCore.Signal(str)

    def __init__(self):
        super(Dashboard, self).__init__()

        self.setWindowTitle("Dashboard")

        self.puller = Puller(requestHandler, self.puller_event_handler)
        self.puller.start_pulling()

        self.EVENT.connect(self.on_event)

    def puller_event_handler(self, data):
        if isinstance(data, list):
            self.EVENT.emit(data)

        elif isinstance(data, str):
            self.ERROR.emit("Error occured while pulling information")

    @QtCore.Slot(list)
    def on_event(self, data):

        for users in data[1]:
            self.handle_conversation(users)

    def handle_conversation(self, users):

        partner = requestHandler.get_partner_by_ids(users)

        #Add conversation to the list

    def closeEvent(self, event):
        self.puller.stop_pulling()
        event.accept()


class Register(QtWidgets.QMainWindow, Ui_Register):
    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("Register")

        self.submitButton.setStyleSheet("QPushButton {color: white}")
        self.loginButton.setStyleSheet("QPushButton {color: white}")

        self.loginButton.clicked.connect(self.login_button_pressed)

    def login_button_pressed(self):
        self.close()


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
        self.dashboard = None

        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setWindowTitle("Error")

    def register_button_pressed(self):

        self.registerWindow = Register()

        self.registerWindow.submitButton.clicked.connect(self.register_submit_button_pressed)

        self.registerWindow.show()

    def register_submit_button_pressed(self):

        if self.registerWindow.passwordLineEdit.text() == self.registerWindow.repasswordLineEdit.text():
            print("matching")
            requestHandler.username = self.registerWindow.usernameLineEdit.text()
            requestHandler.password = self.registerWindow.passwordLineEdit.text()
            return_code = requestHandler.register()

            if return_code == 12:
                self.msg.setText("Username already taken")
                self.msg.exec()

            elif return_code == 1:
                self.msg.setText("Couldn't reach server")
                self.msg.exec()

            elif return_code == 0:
                self.registerWindow.close()
                self.usernameLineEdit.setText(requestHandler.username)

        else:
            self.msg.setText("Passwords need to match")
            self.msg.exec()

    def submit_button_pressed(self):

        requestHandler.username = self.usernameLineEdit.text()
        requestHandler.password = self.passwordLineEdit.text()

        return_code = requestHandler.get_token()

        if return_code == 1:
            self.msg.setText("Couldn't reach server")
            self.msg.exec()

        elif return_code == 13:
            self.msg.setText("Bad credentials")
            self.msg.exec()

        elif return_code == 0:
            self.dashboard = Dashboard()
            self.hide()
            self.dashboard.show()

    def logout_button_pressed(self):
        self.dashboard.close()
        self.usernameLineEdit.setText(requestHandler.username)
        self.passwordLineEdit.clear()
        self.show()


app = QtWidgets.QApplication(sys.argv)

requestHandler = RequestHandler()

window = Login()
window.show()
app.exec()
