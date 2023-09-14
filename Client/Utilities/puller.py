from threading import Thread
from Utilities.message_handler import RequestHandler
import time
import datetime
import requests


class Puller:
    thread : Thread
    pull = False
    last_datetime = datetime.datetime(1995, 10, 12)

    def __init__(self, requesthandler, event_listener, target, conversation_id=None):
        self.requestHandler = requesthandler
        self.event_listener = event_listener

        self.conversations = []

        self.target = target
        self.conversation_id = conversation_id

    def start_pulling(self):
        self.pull = True
        self.thread = Thread(target=self.infinite_pull)
        self.thread.start()

    def stop_pulling(self):
        self.pull = False
        self.last_datetime = 0

    def infinite_pull(self):
        while self.pull:
            self.pull_data()
            time.sleep(1)

    def pull_data(self):
        if self.target == "message":

            try:
                response = self.requestHandler.get_messages_conversation(self.conversation_id)

            except Exception as e:
                self.event_listener(e)
                return

            messages = response.json()['messages']

            messages = sorted(messages, key=lambda x: x['sent_date'])

            if len(messages) and datetime.datetime.strptime(messages[-1]['sent_date'], '%Y.%m.%d:%H.%M.%S') > self.last_datetime:
                self.event_listener(list(filter(lambda x: datetime.datetime.strptime(x['sent_date'], '%Y.%m.%d:%H.%M.%S') > self.last_datetime, messages)))

                self.last_datetime = datetime.datetime.strptime(messages[-1]['sent_date'], '%Y.%m.%d:%H.%M.%S')

        elif self.target == "conversation":

            try:
                response = self.requestHandler.get_conversations()

            except Exception as e:
                self.event_listener(e)
                return

            conversations = response.json()['data']

            for conversation in conversations:
                if conversation['id'] not in [x[0] for x in self.conversations]:
                    self.conversations.append([conversation['id'], conversation['users']])

            self.event_listener(self.conversations)


if __name__ == "__main__":
    puller = Puller(RequestHandler(username="testuser2", password="testpassword2"), None)

    puller.pull_data()