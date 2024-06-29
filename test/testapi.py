import sys
import os
import pytest
import json
from fastapi.testclient import TestClient
from starlette.exceptions import HTTPException
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from api.controller.game_routing import GameApiRouting

client = TestClient(GameApiRouting.router)

class TestApi:

    def test_game_intro(self):
        """ Test api game intro """
        response = client.get("/game/intro")
        assert response.status_code == 200
        assert response.json() == {'message': ['Welcome in Tank game, play random battle with /game/random or define your own clash with /game/defined']}

    def test_game_rules(self):
        """ Test api game rules """
        response = client.get("/game/rules")
        assert response.status_code == 200
        assert response.json() == {'message': 'Game rules will be available soon'}

    def test_game_defined(self):
        """ Test api game defined """
        response = client.get("/game/defined")
        assert response.status_code == 200
        assert response.json() == { 'client_host': 'testclient', 'message': ['Hello Player, Defined Game will be available soon']}

    def test_game_demo(self):
        """ Test api game demo """
        username = {"username": "pytest_username"}
        response = client.post("/game/demo", json=username)
        assert response.status_code == 200
        response_string = json.dumps(response.json())
        assetrtion_to_test = 'Hello pytest_username' in response_string
        assert assetrtion_to_test is True

    def test_game_random_missing_token(self):
        """ Test api wrong token """
        req_headers = {"X-Token": "hailhydra"}
        with pytest.raises(HTTPException):
            client.post("/game/random", headers=req_headers)

    def test_game_random_invalid_token(self):
        """ Test api invalid token """
        req_headers = {"Authorization": "hailhydra"}
        with pytest.raises(Exception) as ex_msg:
            client.post("/game/random", headers=req_headers)

if __name__ == '__main__':
    pytest.main()