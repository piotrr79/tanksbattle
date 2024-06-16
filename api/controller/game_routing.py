from fastapi import APIRouter, Request
#from pydantic import BaseModel
from .game import Game

class GameApiRouting(Request):
    """ Game Api Routing """

    router = APIRouter()
    def __init__(self):
        pass

    def __pass_self(self):
        return self

    @classmethod
    @router.get("/game/intro")
    async def game_welcome(request: Request):
        respone = Game.play_game_welcome(GameApiRouting.__pass_self)
        return {"message": respone}

    @classmethod
    @router.get("/game/random")
    async def game_random(request: Request):
        client_host = request.client.host
        respone = Game.play_random_game(GameApiRouting.__pass_self)
        return {"message": respone, "client_host": client_host}
    
    @classmethod
    @router.get("/game/defined")
    async def game_defined(request: Request):
        client_host = request.client.host
        respone = Game.play_defined_game(GameApiRouting.__pass_self)
        return {"message": respone, "client_host": client_host}
    
    @classmethod
    @router.get("/game/rules")
    async def game_rules(request: Request):
        respone = Game.play_game_rules(GameApiRouting.__pass_self)
        return {"message": respone}
    

