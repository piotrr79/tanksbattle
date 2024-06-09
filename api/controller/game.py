from fastapi import APIRouter, Request
from pydantic import BaseModel

class GameApiRouting():
    """ Game Api Routing """

    router = APIRouter()
    def __init__(self):
        pass

    @router.get("/welcome")
    async def root(request: Request):
        client_host = request.client.host
        return {"message": "Hello Player", "client_host": client_host}

    @router.get("/game/random")
    async def root(request: Request):
        client_host = request.client.host
        return {"message": "Hello Player, Random Game", "client_host": client_host}