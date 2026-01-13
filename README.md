# API de Gestión de Inventario

Esta es una API Rest completa para la gestión de artículos de un inventario, construida con **FastAPI** y **SQLModel**. Incluye una base de datos SQLite, un frontend simple en HTML/JavaScript y documentación interactiva.

## Requisitos

- Python 3.7+
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clonar el repositorio.
2. Instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

3. Configurar las variables de entorno:
   - Copiar `.env.example` a `.env` y ajustar los valores si es necesario.

## Configuración (Variables de Entorno)

La aplicación utiliza variables de entorno para su configuración. Puedes crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
DATABASE_URL=sqlite:///database.db
PORT=8000
HOST=0.0.0.0
```

- `DATABASE_URL`: URL de conexión a la base de datos (por defecto SQLite).
- `PORT`: Puerto en el que correrá la API.
- `HOST`: Dirección de escucha (0.0.0.0 para todas las interfaces).

## Ejecución de la API

Para iniciar el servidor de la API, ejecuta:

```bash
python main.py
```

El servidor se iniciará en `http://localhost:8000`.

## Características

- **Agregar un artículo**: Permite registrar nuevos artículos con código, nombre, marca, unidades y bodega.
- **Consultar artículos**: Obtener la lista completa de artículos o buscar uno específico por su código.
- **Modificar un artículo**: Actualizar la información de un artículo existente mediante su código.
- **Eliminar un artículo**: Remover un artículo del inventario usando su código.
- **Frontend Integrado**: Interfaz de usuario accesible desde la raíz de la API.

## Acceso al Proyecto

Una vez que la API esté corriendo, puedes acceder a:

- **Frontend (Interfaz de Usuario)**: [http://localhost:8000/](http://localhost:8000/)
- **Documentación Interactiva (Swagger UI)**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Documentación Alternativa (Redoc)**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Estructura del Proyecto

- `main.py`: Código fuente de la API FastAPI y definición del modelo SQLModel.
- `index.html`: Aplicativo frontend simple para gestionar el inventario desde el navegador.
- `database.db`: Base de datos SQLite (se genera automáticamente al iniciar).
- `client_example.py`: Script de ejemplo en Python para interactuar con la API.
- `docs.html`: Documentación estática de la API.
- `README.md`: Este archivo de documentación.

## Ejemplo de Uso del Cliente Python

Puedes probar la API programáticamente ejecutando:

```bash
python client_example.py
```
