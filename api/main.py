from fastapi import FastAPI
from .controller.game_routing import GameApiRouting

app = FastAPI()


app.include_router(GameApiRouting.router)


@app.get("/")
async def root():
    return {"message": "Welcome in Tank Game Application!"}