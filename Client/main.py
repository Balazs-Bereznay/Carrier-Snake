import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QAbstractItemView

from Utilities.login import Ui_Login
from Utilities.register import Ui_Register
from Utilities.dashboard import Ui_Dashboard
from Utilities.models import ConversationModel
from Utilities.message_handler import RequestHandler
from Utilities.puller import Puller


class Dashboard(QtWidgets.QMainWindow, Ui_Dashboard):
    EVENT = QtCore.Signal(list)
    ERROR = QtCore.Signal(str)

    def __init__(self):
        super(Dashboard, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("Dashboard")

        self.model = ConversationModel()
        self.convoList.setModel(self.model)
        self.convoList.setModelColumn(0)
        self.convoList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.convoList.doubleClicked.connect(self.convo_clicked)

        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setWindowTitle("Error")

        self.addButton.clicked.connect(self.add_button_clicked)
        self.deleteButton.clicked.connect(self.delete_button_clicked)

        self.puller = Puller(requestHandler, self.puller_event_handler, target='conversation')
        self.puller.start_pulling()
        self.conversations = []

        self.EVENT.connect(self.on_event)

    def puller_event_handler(self, data):
        if isinstance(data, list):
            self.EVENT.emit(data)

        elif isinstance(data, str):
            print("Error occured while pulling information")

    @QtCore.Slot(list)
    def on_event(self, data):

        for conversation in data:
            if conversation not in self.conversations:

                self.handle_conversation(conversation[1], conversation[0])
                self.conversations.append(conversation)

    def handle_conversation(self, users, convo_id):

        partner = requestHandler.get_partner_by_ids(users)

        self.model.conversations.append((convo_id, partner))
        self.model.layoutChanged.emit()

    def convo_clicked(self, index):
        print(self.model.itemData(index))

    def add_button_clicked(self):
        return_code = requestHandler.new_conversation(self.newConvoInput.text())

        print(return_code)

        #TODO: open the chat window with the new convo

    def delete_button_clicked(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Are you sure you want to delete the conversation?")
        msgBox.setWindowTitle("Delete")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        button_clicked = msgBox.exec()

        if button_clicked == QtWidgets.QMessageBox.Ok:
            indexes = self.convoList.selectedIndexes()
            if indexes:
                index = indexes[0]

                return_code = requestHandler.delete_conversation(self.model.itemData(index)[2])

                if return_code == 0:
                    for conversation in self.conversations:
                        if self.model.itemData(index)[2] == conversation[0]:

                            self.puller.conversations.remove(conversation)
                            self.conversations.remove(conversation)

                    print(self.conversations)
                    print(self.puller.conversations)

                    del self.model.conversations[index.row()]
                    self.model.layoutChanged.emit()

                    self.convoList.clearSelection()

                else:
                    self.msg.setText(f"Error occurred: {return_code}")
                    self.msg.exec()

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
