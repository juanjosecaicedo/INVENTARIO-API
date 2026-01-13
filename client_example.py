import os
import requests
import json
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener URL base de las variables de entorno o usar local por defecto
HOST = os.getenv("HOST", "localhost")
PORT = os.getenv("PORT", "8000")
BASE_URL = f"http://{HOST}:{PORT}/articulos/"

def agregar_articulo(codigo, nombre, marca, unidades, bodega):
    data = {
        "codigo": codigo,
        "nombre": nombre,
        "marca": marca,
        "unidades": unidades,
        "nombre_bodega": bodega
    }
    response = requests.post(BASE_URL, json=data)
    return response.json()

def listar_articulos():
    response = requests.get(BASE_URL)
    return response.json()

def actualizar_articulo(codigo, nombre, marca, unidades, bodega):
    data = {
        "codigo": codigo,
        "nombre": nombre,
        "marca": marca,
        "unidades": unidades,
        "nombre_bodega": bodega
    }
    response = requests.put(f"{BASE_URL}{codigo}", json=data)
    return response.json()

def eliminar_articulo(codigo):
    response = requests.delete(f"{BASE_URL}{codigo}")
    return response.json()

if __name__ == "__main__":
    print("--- Ejemplo de uso de la API ---")
    
    # Nota: La API debe estar corriendo para que esto funcione
    try:
        # 1. Agregar un artículo
        print("\nAgregando artículo 101...")
        print(agregar_articulo(101, "Monitor 24", "LG", 10, "Bodega Norte"))
        
        # 2. Listar artículos
        print("\nListado de artículos:")
        print(json.dumps(listar_articulos(), indent=2))
        
        # 3. Actualizar artículo
        print("\nActualizando artículo 101...")
        print(actualizar_articulo(101, "Monitor 27", "LG", 5, "Bodega Sur"))
        
        # 4. Eliminar artículo
        print("\nEliminando artículo 101...")
        print(eliminar_articulo(101))
        
    except requests.exceptions.ConnectionError:
        print("\nError: No se pudo conectar con la API. Asegúrate de ejecutar 'python main.py' primero.")
