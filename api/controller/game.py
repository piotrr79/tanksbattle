import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from fastapi import Request
from armour_py.api.model.data_models import GameStatistics
from tanksbattle.battle import Battle
from .base_game import BaseGame
import utils.constant as const

class Game(BaseGame):

    def __init__(self):
        pass

    def play_demo_game(self) -> str:
        """ Demo random game  """
        return Battle.play_random(self)

    def play_random_game(self, request: Request) -> str:
        """ Random game  """
        user_name = BaseGame.get_current_user(self, request.headers['authorization'])
        result = Battle.play_random(self)
        response = Game.__stats_manipulation(self, user_name, request.client.host, result)       
        return response
    
    def play_defined_game(self) -> str:
        """ Defined game  """
        # ToDo - implement defined game
        return {"Hello Player, Defined Game will be available soon"}
    
    def play_game_welcome(self) -> str:
        """ Game welcome message """
        return {"Welcome in Tank game, play random battle with /game/random or define your own clash with /game/defined"}
    
    def play_game_rules(self) -> str:
        """ Game rules """
        response = "Game rules will be available soon"
        return  response
    
    def __stats_manipulation(self, username: str, ip: str, game_result: str) -> str:
        
        
        print(username)
        score = 0
        if game_result == const.TANK_IS_SAFE:
            score = 1
            response_string = const.YOU_WON
        elif game_result == const.NO_TANK_IS_SAFE:
            score = -1
            response_string = const.YOU_LOSE
        elif game_result == const.VULNERABLE_TO_SELF:
            score = 0
            response_string = const.YOU_DRAW_RUBBISH_TANK

        result = GameStatistics.save_result(self, username, ip, score)

        print(result)

        response = {
            'number of games played': result.number_of_games,
            'your total score': result.player_score,
            'your current result': response_string
        }

        return response
    
    
