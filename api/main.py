from fastapi import FastAPI
from controller.game import GameApiRouting

app = FastAPI()


app.include_router(GameApiRouting.router)


@app.get("/")
async def root():
    return {"message": "Hello Game Applications!"}