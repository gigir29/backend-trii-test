from fastapi import FastAPI
from .api import pokemon

app = FastAPI()

app.include_router(pokemon.router)
