# Pokémon API Filter and Download - Trii test👩🏼‍💻💚
Este proyecto es una aplicación web desarrollada con FastAPI que consume la API pública de Pokémon, aplica filtros y permite la descarga de los datos en formato comprimido (ZIP).
# Requisitos
Asegúrate de tener Python 3.8 o superior instalado. Puedes instalar las dependencias necesarias con:
```
pip install -r requirements.txt
```
# Endpoints
## 1. Obtener Pokémon con Filtros
**URL:** /pokemon/

**Método:** GET

**Parámetros de Consulta:**

- **type_filter (opcional):** Filtrar Pokémon por tipo (por ejemplo, grass).
- **ability_filter (opcional):** Filtrar Pokémon por habilidad (por ejemplo, overgrow).
- **limit (opcional):** Limitar el número de resultados (por defecto es 10).
  
### **Ejemplo de Solicitud:**
```
GET http://127.0.0.1:8000/pokemon/?type_filter=fire&limit=5

```
### **Respuesta:**
Devuelve una lista de Pokémon que cumplen con los filtros aplicados.
```
[
    {
        "name": "charizard",
        "url": "https://pokeapi.co/api/v2/pokemon/6/"
    },
    ...
]

```

## 2. Descargar Pokémon
**URL:** /download-pokemon/

**Método:** GET

**Parámetros de Consulta:**

- **type_filter (opcional):** Filtrar Pokémon por tipo (por ejemplo, grass).
- **ability_filter (opcional):** Filtrar Pokémon por habilidad (por ejemplo, overgrow).
- **limit (opcional):** Limitar el número de resultados (por defecto es 10).
  
### **Ejemplo de Solicitud:**

```
GET http://127.0.0.1:8000/download-pokemon/?type_filter=water&limit=5

```
### **Respuesta:**
Devuelve un archivo ZIP que contiene archivos JSON con la información de los Pokémon filtrados.


# **Configuración**
## **CORS**
La aplicación está configurada para permitir solicitudes desde los siguientes orígenes:

- http://localhost
- http://localhost:8000
- http://127.0.0.1:8000

# Instalación
1. Clona el repositorio

```
git clone https://github.com/gigir29/backend-trii-test.git
```
2. Navega al directorio del proyecto:
   
```
cd cd backend-trii-test
```

3. Crea y activa un entorno virtual

```
python -m venv venv
source venv/bin/activate  # En Windows usa venv\Scripts\activate
```
4. Instala las dependencias

```
pip install -r requirements.txt
```

## Uso

1. Inicia la aplicación FastAPI:

```
uvicorn app.main:app --reload
```
Esto iniciará el servidor de desarrollo de FastAPI en http://127.0.0.1:8000

2. Accede a la documentación interactiva de la API en tu navegador:

    [Documentación interactiva con Swagger](http://127.0.0.1:8000/docs#/)

3. Utiliza la API para aplicar filtros y descargar datos de Pokémon.

# Notas Importantes
## Descargar Pokémon Filtrados con el Endpoint /download-pokemon/
El endpoint /download-pokemon/ devuelve un archivo ZIP que contiene los datos de los Pokémon filtrados. Debido a la naturaleza de esta respuesta, es importante tener en cuenta lo siguiente:

- **Formato de Respuesta:** El endpoint devuelve un archivo ZIP. Por lo tanto, el Content-Type de la respuesta es application/zip.

## Uso de Postman:
Cuando uses Postman para probar este endpoint, asegúrate de no intentar interpretar la respuesta como JSON. Por defecto, Postman intenta mostrar la respuesta en formato JSON, lo que resultará en un error de interpretación (JSONError: Unexpected token 'P' at 1:1).

## Pasos para evitar el error en Postman:
Después de realizar la solicitud en Postman, selecciona la opción **"Save Response"** o elige **"Send and Download"**.
Guarda el archivo ZIP en tu sistema y ábrelo con un descompresor de archivos para revisar su contenido.
**Encabezados Importantes:**
**Content-Type:** application/zip
**Content-Disposition:** attachment; filename=pokemon_data.zip

## Ejemplo de Solicitud en Postman:
```
GET http://127.0.0.1:8000/download-pokemon/?type_filter=fire&limit=10
```
## Cómo Verificar el Archivo Descargado:
- Asegúrate de que Postman descargue el archivo ZIP en lugar de intentar interpretarlo como JSON.
- Utiliza un descompresor de archivos para abrir el archivo descargado.
Dentro del archivo ZIP, encontrarás archivos JSON correspondientes a cada Pokémon que cumplió con los filtros aplicados.

## Notas

- El servicio utiliza la API pública de Pokémon para obtener los datos.
- Asegúrate de que los filtros aplicados sean válidos según la API de Pokémon.
- En la documentación interactiva de Swagger al usar el endpoint de descargar pokemon se puede hacer clic en "Download file" para ver el archivo json.

Muchas gracias, cualquier comentario sera bienvenido a mi correo gabrielarincon229@gmail.com💚

