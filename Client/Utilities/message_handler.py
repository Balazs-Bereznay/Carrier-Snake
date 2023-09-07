import requests

"""_summary_

    error codes:
        0: Task finished with no errors
        1: Couldn't reach api
        12: Database integrity error, probably username already in use
        13: Invalid credentials
"""

class RequestHandler():
    token = None
     
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    
    def register(self):
        headers = {'username':self.username,
                   'password':self.password}
        
        try:
            response = requests.get('http://127.0.0.1:5000/register', headers=headers)
            
        except requests.exceptions.Timeout:
            return 1
        
        if response.status_code == 409:
            return 12
        
        return_code = self.get_token()
        
        return return_code
        
    def get_token(self):
        headers = {'username':self.username,
                   'password':self.password}
        
        try:
            response = requests.get('http://127.0.0.1:5000/login', headers=headers)
            self.token = response.json()['token']
            
        except requests.exceptions.Timeout:
            return 1
        
        except:
            return 13
        
        return 0
        
        
    def validate_token(self):
        if self.token == None:
            return_code = self.get_token()
                      
            return return_code
        
        headers = {'token':self.token}
        
        try:
            response = requests.get('http://127.0.0.1:5000/validate_token', headers=headers)
            
        except requests.exceptions.Timeout:
            return 1    
        
        if 'token' in response.headers:
            return 0
        
        else:
            return_code = self.get_token()
                      
            return return_code
        
        
if __name__ == '__main__':
    request_handler = RequestHandler('testuser6', 'testpassword6')
    
    print(request_handler.register())
    print(request_handler.validate_token())
    print(request_handler.token)
        