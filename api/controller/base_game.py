import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import requests
from utils.env import EnvReader

class BaseGame():

    def __init__(self):
        pass

    def get_current_user(self, token: str) -> str:
        try:
            payload = { 'Authorization' : token }
            server_response = requests.get(EnvReader.get_token_server_endpoint(self), headers=payload)
            user_id = str(server_response.json()['id'])
            user_name = str(server_response.json()['username'])
            return user_id + '/' + user_name
        except Exception as error:
            raise Exception('Cannot authorize user: ', error)