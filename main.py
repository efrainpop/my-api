from fastapi import FastAPI, Body #importa la clase fastapi de la libreria fastapi
from fastapi.responses import HTMLResponse #importa la clase HTMLResponse de la libreria fastapi
from movies_list import movies_list
app = FastAPI() #crea una instancia de la clase fastapi
app.title = "Mi primera aplicacion de peliculas y Analisis de Datos"
app.version = "0.0.1"
@app.get('/', tags=['Home']) #definiendo una ruta
def message():# definimos una funcion de la ruta
    return  HTMLResponse('<h1>Hola mundo</h1>') #retorna un objeto de la clase HTMLResponse

@app.get('/movies', tags=['Movies']) #definiendo una ruta
def movies():# definimos una funcion de la ruta
    return  movies_list

@app.get('/movies/{id}', tags=['Movies']) #app get consultar por id
def get_movies(id: int):# definimos una funcion de la ruta
    for item in movies_list:
        if item["id"] == id:
            return item
    return[]

@app.get('/movies/', tags=['Movies']) #definiendo una ruta
def get_movies_by_category(category: str = "All", year: int = 0):# definimos una funcion de la ruta #app get consultar por categoria y anio():# definimos una funcion de la ruta
    return [ item for item in movies_list if item["category"] == category and item["year"] == year]

@app.post('/movies/', tags=['Movies']) #definiendo una ruta
def create_movie(movie: dict = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):# definimos una funcion de la ruta
    movies_list.append({
        "id": len(movies_list) + 1,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies_list
