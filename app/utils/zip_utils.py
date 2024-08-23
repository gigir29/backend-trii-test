import zipfile
import io
import json


def create_zip_file(pokemon_data):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for i, pokemon in enumerate(pokemon_data):
            filename = f"pokemon_{i + 1}.json"
            zip_file.writestr(filename, json.dumps(pokemon))
    zip_buffer.seek(0)
    return zip_buffer
