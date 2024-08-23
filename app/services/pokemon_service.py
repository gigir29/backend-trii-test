import requests

POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_data(
    type_filter: str = None, ability_filter: str = None, limit: int = 10
):
    response = requests.get(f"{POKEMON_API_URL}?limit={limit}")
    if response.status_code != 200:
        raise Exception("Error fetching data from Pokémon API")

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
