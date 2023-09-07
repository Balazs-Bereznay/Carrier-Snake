import requests

"""_summary_

    error codes:
        0: Task finished with no errors
        1: Couldn't reach api
        13: Invalid credentials
"""

class RequestHandler():
    valid = False
    token = None
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        
    def get_token(self):
        headers = {'username':self.username,
                   'password':self.password}
        
        try:
            response = requests.get('http://127.0.0.1:5000/login', headers=headers)
            self.token = response.json()['token']
            
        except requests.exceptions.RequestException:
            return 1
        
        except:
            return 13
        
        return 0
        
        
    def validate_token(self):
        if self.token == None:
            return_code = self.get_token()
                      
            if return_code != 0:
                return return_code
        
        headers = {'token':self.token}
            
        response = requests.get('http://127.0.0.1:5000/validate_token', headers=headers)
        
        if 'token' in response.headers:
            return 0
        
        else:
            return_code = self.get_token()
                      
            if return_code != 0:
                return return_code
        
        
if __name__ == '__main__':
    request_handler = RequestHandler('testuser1', 'testpassword1')
    print(request_handler.validate_token())
    print(request_handler.token)
        