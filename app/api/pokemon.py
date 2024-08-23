from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import StreamingResponse
from app.services.pokemon_service import get_pokemon_data
from app.utils.zip_utils import create_zip_file

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


@router.get("/download-pokemon/")
def download_pokemon(
    type_filter: str = Query(None, description="Filter by Pokémon type"),
    ability_filter: str = Query(None, description="Filter by Pokémon ability"),
    limit: int = Query(10, description="Limit the number of Pokémon returned"),
):
    try:
        pokemon_data = get_pokemon_data(type_filter, ability_filter, limit)
        zip_buffer = create_zip_file(pokemon_data)
        return StreamingResponse(
            zip_buffer,
            media_type="application/zip",
            headers={"Content-Disposition": "attachment; filename=pokemon_data.zip"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))