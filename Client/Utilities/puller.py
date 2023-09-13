from threading import Thread
from Utilities.message_handler import RequestHandler
import time
import datetime
import requests


class Puller:
    thread : Thread
    pull = False
    last_datetime = datetime.datetime(1995, 10, 12)

    def __init__(self, requestHandler, event_listener):
        self.requestHandler = requestHandler
        self.event_listener = event_listener

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
        try:
            response = self.requestHandler.get_conversations()

        except Exception as e:
            self.event_listener(e)
            return

        conversations = response.json()['data']

        new_messages = [[],[]]

        latest = self.last_datetime

        for conversation in conversations:
            messages = sorted(conversation['messages'], key=lambda x: x['sent_date'])

            if len(messages) and datetime.datetime.strptime(messages[-1]['sent_date'], '%Y.%m.%d:%H.%M.%S') > self.last_datetime:
                new_messages[0].append(conversation['id'])
                new_messages[1].append(conversation['users'])
                new_messages.append(list(filter(lambda x: datetime.datetime.strptime(x["sent_date"], '%Y.%m.%d:%H.%M.%S') > self.last_datetime, messages)))

                if datetime.datetime.strptime(messages[-1]['sent_date'], '%Y.%m.%d:%H.%M.%S') > latest:
                    latest = datetime.datetime.strptime(messages[-1]['sent_date'], '%Y.%m.%d:%H.%M.%S')

        self.event_listener(new_messages)
        self.last_datetime = latest


if __name__ == "__main__":
    puller = Puller(RequestHandler(username="testuser2", password="testpassword2"), None)

    puller.pull_data()