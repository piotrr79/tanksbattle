from fastapi import APIRouter, Request, Depends
from fastapi.security import APIKeyHeader
from typing_extensions import Annotated
from .game import Game
from .request_validation import RandomGame

class GameApiRouting(Request):
    """ Game Api Routing """

    router = APIRouter()
    header_token = APIKeyHeader(name='Authorization')
    TokenCheck = Annotated[str, Depends(header_token)]

    def __init__(self):
        pass

    def __pass_self(self):
        return self

    @classmethod
    @router.get("/game/intro")
    async def game_welcome(request: Request):
        response = Game.play_game_welcome(GameApiRouting.__pass_self)
        return {"message": response}

    @classmethod
    @router.post("/game/demo")
    async def play_demo_game(request: Request, user: RandomGame):
        response = Game.play_demo_game(GameApiRouting.__pass_self)
        return {"message": "Hello" + user, "result": response, "client_host": request.client.host}

    @classmethod
    @router.post("/game/random")
    async def game_random(request: Request, token: TokenCheck):
        response = Game.play_random_game(GameApiRouting.__pass_self, request)
        return {"message": response, "client_host": request.client.host}
    
    @classmethod
    @router.get("/game/defined")
    async def game_defined(request: Request):
        client_host = request.client.host
        response = Game.play_defined_game(GameApiRouting.__pass_self)
        return {"message": response, "client_host": client_host}
    
    @classmethod
    @router.get("/game/rules")
    async def game_rules(request: Request):
        response = Game.play_game_rules(GameApiRouting.__pass_self)
        return {"message": response}
    

