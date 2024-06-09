from fastapi import APIRouter, Request
#from pydantic import BaseModel

class GameApiRouting():
    """ Game Api Routing """

    router = APIRouter()
    def __init__(self):
        pass

    @router.get("/game/intro")
    async def game_welcome(request: Request):
        client_host = request.client.host
        return {"message": "Game Intro", "client_host": client_host}

    @router.get("/game/random")
    async def game_random(request: Request):
        client_host = request.client.host
        return {"message": "Hello Player, Random Game", "client_host": client_host}
    
    @router.get("/game/defined")
    async def game_defined(request: Request):
        client_host = request.client.host
        return {"message": "Hello Player, Defined Game", "client_host": client_host}
    
    @router.get("/game/rules")
    async def game_rules(request: Request):
        client_host = request.client.host
        return {"message": "Game Rules", "client_host": client_host}
    

