from fastapi import FastAPI
from . import models
from .database import engine
from .routers import clientes

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Gerenciamento de Clientes",
    description=(
        "Projeto de portfólio em Python para cadastro e gerenciamento "
        "de clientes usando FastAPI, SQLAlchemy e SQLite."
    ),
    version="1.0.0",
)

app.include_router(clientes.router)


@app.get("/", tags=["Status"])
def raiz():
    return {
        "projeto": "API de Gerenciamento de Clientes",
        "status": "online",
        "documentacao": "/docs",
    }


@app.get("/health", tags=["Status"])
def health():
    return {"status": "ok"}
