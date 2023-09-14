from PySide6 import QtCore
from PySide6.QtCore import Qt


class ConversationModel(QtCore.QAbstractListModel):
    def __init__(self, *args, conversations=None, **kwargs):
        super(ConversationModel, self).__init__(*args, **kwargs)
        self.conversations = conversations or []

    def data(self, index, role):
        if role == Qt.DisplayRole:

            _, user = self.conversations[index.row()]

            return user

        elif role == Qt.EditRole:

            convo_id, _ = self.conversations[index.row()]

            return convo_id

    def rowCount(self, index):
        return len(self.conversations)
