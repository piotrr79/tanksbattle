import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from armour_py.api.model.data_models import GameStatistics
from tanksbattle.battle import Battle
from .base_game import BaseGame
import utils.constant as const

class Game(BaseGame):

    def __init__(self):
        pass

    def play_random_game(self, username: str, ip: str) -> str:

        result = Battle.play_random(self)
        response = Game.__stats_manipulation(self, username, ip, result)       
        return response
    
    def play_defined_game(self) -> str:
        # ToDo - implement defined game
        return {"Hello Player, Defined Game will be available soon"}
    
    def play_game_welcome(self) -> str:
        return {"Welcome in Tank game, play random battle with /game/random or define your own clash with /game/defined"}
    
    def play_game_rules(self) -> str:
        response = "Game rules will be available soon"
        return  response
    
    def __stats_manipulation(self, username: str, ip: str, result: str) -> str:

        score = 0
        if result == const.TANK_IS_SAFE:
            score = 1
        elif result == const.NO_TANK_IS_SAFE:
            score = -1
        elif result == const.VULNERABLE_TO_SELF:
            score = 0

        response = GameStatistics.save_result(self, username, ip, score)
        return response
