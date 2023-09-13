import requests

"""_summary_

    error codes:
        0: Task finished with no errors
        1: Couldn't reach api
        12: Database integrity error, probably username already in use
        13: Invalid credentials
"""


class RequestHandler:
    token = None
     
    def __init__(self, username=None, password=None, url='http://127.0.0.1:5000/'):
        self.username = username
        self.password = password
        self.url = url
    
    def register(self):
        headers = {'username': self.username,
                   'password': self.password}
        
        try:
            response = requests.get(self.url + 'register', headers=headers)
            
        except requests.exceptions.RequestException:
            return 1
        
        if response.status_code == 409:
            return 12
        
        return_code = self.get_token()
        
        return return_code
        
    def get_token(self):
        headers = {'username': self.username,
                   'password': self.password}
        
        try:
            response = requests.get(self.url + 'login', headers=headers)
            self.token = response.headers['token']
            
        except requests.exceptions.RequestException:
            return 1
        
        except:
            return 13
        
        return 0

    def validate_token(self):
        if self.token is None:
            return_code = self.get_token()
                      
            return return_code
        
        headers = {'token': self.token}
        
        try:
            response = requests.get(self.url + 'validate_token', headers=headers)
            
        except requests.exceptions.RequestException:
            return 1    
        
        if 'token' in response.headers:
            return 0
        
        else:
            return_code = self.get_token()
                      
            return return_code

    def get_conversations(self):
        return_code = self.validate_token()

        if return_code == 0:

            headers = {'token': self.token}

            conversations = requests.get(self.url + 'get_conversations', headers=headers)

            return conversations

        else:

            return return_code

    def get_partner_by_ids(self, users):
        return_code = self.validate_token()

        if return_code == 0:

            headers = {'token': self.token}

            data = {

                'id1': users[0],
                'id2': users[1]

            }

            partner = requests.get(self.url + 'user_by_id', headers=headers, json=data)

            partner = partner.json()['partner']

            return partner

        else:

            return return_code

        
if __name__ == '__main__':
    request_handler = RequestHandler('testuser2', 'testpassword2')
    
    print(request_handler.get_conversations())
        