# API de Gerenciamento de Clientes

Projeto de portfólio desenvolvido em Python com FastAPI, SQLAlchemy e SQLite.

## Funcionalidades
- Criar cliente
- Listar clientes
- Consultar cliente por ID
- Buscar clientes por nome
- Atualizar cliente
- Excluir cliente
- Validação de nome, e-mail e telefone
- Bloqueio de e-mail duplicado
- Documentação automática Swagger/OpenAPI
- Testes básicos com Pytest

## Tecnologias
Python, FastAPI, SQLAlchemy, SQLite, Pydantic, Uvicorn e Pytest.

## Como executar

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

Instale:
```bash
pip install -r requirements.txt
```

Execute:
```bash
uvicorn app.main:app --reload
```

Acesse:
- API: http://127.0.0.1:8000
- Swagger: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Testes
```bash
pytest
```

## Autora
Andressa Henrique Teixeira
Estudante de Análise e Desenvolvimento de Sistemas e Engenharia de Software.
Foco: Back-end, Python e Power BI.
