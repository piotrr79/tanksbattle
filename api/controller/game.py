import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from armour_py.api.model.data_models import GameStatistics
from tanksbattle.battle import Battle

class Game():

    def __init__(self):
        pass

    def play_random_game(self) -> str:
        response = Battle.play_random(self)
        # ToDo - put DB logic bnindings here
        return response
    
    def play_defined_game(self) -> str:
        # ToDo - compelete random game
        return {"Hello Player, Defined Game will be available soon"}
    
    def play_game_welcome(self) -> str:
        # ToDo - compelete random game
        return {"Welcome in Tank game, play random battle with /game/random or define your own clash with /game/defined"}
    
    def play_game_rules(self) -> str:
        response = "Game rules will be available soon"
        return  response