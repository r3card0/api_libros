from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Libro(BaseModel):
    titulo : str
    autor : str
    pagina : int
    editorial : Optional[str]

@app.get("/")
def index():
    return {'mensaje': 'Hola Python 🐍'}

@app.get("/libros/{id}")
def mostrar_libro(id:int):
    return {'data': id}

@app.post('/libros')
def insertar_libro(libro:Libro):
    return {'mensaje' : f"libro {libro.titulo} insertado"}
