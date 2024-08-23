from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/"


@app.get("/pokemon/")
def get_pokemon(
    type_filter: str = Query(None, description="Filter by Pokémon type"),
    ability_filter: str = Query(None, description="Filter by Pokémon ability"),
    limit: int = Query(10, description="Limit the number of Pokémon returned"),
):
    response = requests.get(f"{POKEMON_API_URL}?limit={limit}")
    if response.status_code != 200:
        raise HTTPException(
            status_code=500, detail="Error fetching data from Pokémon API"
        )

    pokemon_data = response.json().get("results", [])
    filtered_data = []

    for pokemon in pokemon_data:
        pokemon_details = requests.get(pokemon["url"]).json()
        if type_filter and type_filter not in [
            t["type"]["name"] for t in pokemon_details["types"]
        ]:
            continue
        if ability_filter and ability_filter not in [
            a["ability"]["name"] for a in pokemon_details["abilities"]
        ]:
            continue
        filtered_data.append(pokemon_details)

    return filtered_data
