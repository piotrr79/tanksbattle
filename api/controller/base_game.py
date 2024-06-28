import sys, os, json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import requests
from utils.env import EnvReader
import utils.constant as const

class BaseGame():

    def __init__(self):
        pass

    def get_current_user(self, token: str) -> str:
        try:
            if EnvReader.get_environment(self) == const.DEV:
                header_payload = { 'Authorization' : token }
                server_response = requests.get(EnvReader.get_token_server_endpoint(self), headers=header_payload)
                user_id = str(server_response.json()['id'])
                user_name = str(server_response.json()['username'])
            elif EnvReader.get_environment(self) == const.STAGING:
                header_payload = { 'Authorization' : token,
                            'Accept': 'application/json', 
                            'Content-Type': 'application/x-www-form-urlencoded' }
                body_payload = {'token': token.replace('Bearer ', '') }
                server_response = requests.post(EnvReader.get_token_server_endpoint(self), headers=header_payload, data=body_payload)
                user_id = str(server_response.json()['client_id'])
                user_name = str(server_response.json()['username'])
            return user_id + '/' + user_name
        except Exception as error:
            raise Exception('Cannot authorize user: ', error)
        