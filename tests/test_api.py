import os

os.environ["TESTING"] = "1"

from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

client = TestClient(app)


def setup_function():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def test_health():
    resposta = client.get("/health")
    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok"}


def test_crud_cliente():
    novo = {
        "nome": "Maria Silva",
        "email": "maria@example.com",
        "telefone": "51999999999",
    }

    resposta = client.post("/clientes", json=novo)
    assert resposta.status_code == 201
    cliente_id = resposta.json()["id"]

    resposta = client.get("/clientes")
    assert resposta.status_code == 200
    assert len(resposta.json()) == 1

    resposta = client.get(f"/clientes/{cliente_id}")
    assert resposta.status_code == 200

    resposta = client.put(
        f"/clientes/{cliente_id}",
        json={"nome": "Maria de Souza"},
    )
    assert resposta.status_code == 200
    assert resposta.json()["nome"] == "Maria de Souza"

    resposta = client.delete(f"/clientes/{cliente_id}")
    assert resposta.status_code == 204

    resposta = client.get(f"/clientes/{cliente_id}")
    assert resposta.status_code == 404


def test_email_duplicado():
    cliente = {
        "nome": "Cliente Um",
        "email": "duplicado@example.com",
        "telefone": "51999999999",
    }
    assert client.post("/clientes", json=cliente).status_code == 201

    cliente["nome"] = "Cliente Dois"
    resposta = client.post("/clientes", json=cliente)
    assert resposta.status_code == 409
