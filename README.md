# Pokémon API Filter and Download - Trii backend test👩🏼‍💻💚
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
GET /pokemon/?type_filter=grass&ability_filter=overgrow&limit=5
```
### **Respuesta:**
Devuelve una lista de Pokémon que cumplen con los filtros aplicados.

## 2. Descargar Pokémon Filtrados
**URL:** /download-pokemon/

**Método:** GET

**Parámetros de Consulta:**

- **type_filter (opcional):** Filtrar Pokémon por tipo (por ejemplo, grass).
- **ability_filter (opcional):** Filtrar Pokémon por habilidad (por ejemplo, overgrow).
- **limit (opcional):** Limitar el número de resultados (por defecto es 10).
  
### **Ejemplo de Solicitud:**

```
GET /download-pokemon/?type_filter=grass&ability_filter=overgrow&limit=5

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
git clone <URL del repositorio>
```
2. Navega al directorio del proyecto:
   
```
cd <directorio del proyecto>
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
Donde main es el nombre del archivo que contiene la instancia de FastAPI (app).

2. Accede a la documentación interactiva de la API en tu navegador:

    [Documentación interactiva con Swagger](http://127.0.0.1:8000/docs#/)

3. Utiliza la API para aplicar filtros y descargar datos de Pokémon.

## Notas

- El servicio utiliza la API pública de Pokémon para obtener los datos.
- Asegúrate de que los filtros aplicados sean válidos según la API de Pokémon.


