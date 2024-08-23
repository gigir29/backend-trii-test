from fastapi import APIRouter, Query, HTTPException
from app.services.pokemon_service import get_pokemon_data

router = APIRouter()


@router.get("/pokemon/")
def get_pokemon(
    type_filter: str = Query(None, description="Filter by Pokémon type"),
    ability_filter: str = Query(None, description="Filter by Pokémon ability"),
    limit: int = Query(10, description="Limit the number of Pokémon returned"),
):
    try:
        return get_pokemon_data(type_filter, ability_filter, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
