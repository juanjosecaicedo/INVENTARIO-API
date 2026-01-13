from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import FileResponse
from sqlmodel import Field, SQLModel, Session, create_engine, select
from fastapi.middleware.cors import CORSMiddleware

# Modelo de Datos
class Articulo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: int = Field(unique=True, index=True)
    nombre: str
    marca: str
    unidades: int
    nombre_bodega: str

# Configuración de la Base de Datos
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

# Inicialización de FastAPI
app = FastAPI(
    title="API de Gestión de Inventario",
    description="API para gestionar artículos de un inventario",
    version="1.0.0"
)

# Configuración de CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Endpoint para el Frontend
@app.get("/", response_class=FileResponse)
def read_index():
    return "index.html"

# Endpoints
@app.post("/articulos/", response_model=Articulo)
def crear_articulo(articulo: Articulo, session: Session = Depends(get_session)):
    statement = select(Articulo).where(Articulo.codigo == articulo.codigo)
    db_articulo = session.exec(statement).first()
    if db_articulo:
        raise HTTPException(status_code=400, detail="El código de artículo ya existe")
    session.add(articulo)
    session.commit()
    session.refresh(articulo)
    return articulo

@app.get("/articulos/", response_model=List[Articulo])
def leer_articulos(session: Session = Depends(get_session)):
    articulos = session.exec(select(Articulo)).all()
    return articulos

@app.get("/articulos/{codigo}", response_model=Articulo)
def leer_articulo(codigo: int, session: Session = Depends(get_session)):
    statement = select(Articulo).where(Articulo.codigo == codigo)
    articulo = session.exec(statement).first()
    if not articulo:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    return articulo

@app.put("/articulos/{codigo}", response_model=Articulo)
def actualizar_articulo(codigo: int, articulo_data: Articulo, session: Session = Depends(get_session)):
    statement = select(Articulo).where(Articulo.codigo == codigo)
    db_articulo = session.exec(statement).first()
    if not db_articulo:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    
    # Actualizar campos
    articulo_dict = articulo_data.dict(exclude_unset=True)
    for key, value in articulo_dict.items():
        if key != "id": # No permitir cambiar el id autoincremental
            setattr(db_articulo, key, value)
            
    session.add(db_articulo)
    session.commit()
    session.refresh(db_articulo)
    return db_articulo

@app.delete("/articulos/{codigo}")
def eliminar_articulo(codigo: int, session: Session = Depends(get_session)):
    statement = select(Articulo).where(Articulo.codigo == codigo)
    articulo = session.exec(statement).first()
    if not articulo:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    session.delete(articulo)
    session.commit()
    return {"message": "Artículo eliminado exitosamente"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
