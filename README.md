# 👥 API de Gerenciamento de Clientes

API REST desenvolvida em **Python** para cadastro e gerenciamento de clientes.

Este projeto foi desenvolvido como parte dos meus estudos em desenvolvimento **Back-end**, com o objetivo de aplicar na prática conceitos de APIs REST, banco de dados, validação de dados, organização de código e testes automatizados.

---

## 🚀 Tecnologias utilizadas

- 🐍 Python
- ⚡ FastAPI
- 🗄️ SQLAlchemy
- 💾 SQLite
- ✅ Pydantic
- 🧪 Pytest
- 🌐 Uvicorn
- 📖 Swagger / OpenAPI

## 💻 Funcionalidades

- Cadastrar, listar, consultar, buscar, atualizar e excluir clientes
- Validar nome, e-mail e telefone
- Impedir e-mails duplicados
- Paginar a listagem
- Documentação interativa com Swagger

## 🔄 CRUD

| Operação | Método HTTP | Função |
|---|---|---|
| Create | POST | Cadastrar cliente |
| Read | GET | Consultar clientes |
| Update | PUT | Atualizar cliente |
| Delete | DELETE | Excluir cliente |

## 🌐 Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/` | Informações básicas da API |
| `GET` | `/health` | Verifica se a API está funcionando |
| `POST` | `/clientes` | Cadastra um novo cliente |
| `GET` | `/clientes` | Lista os clientes |
| `GET` | `/clientes/buscar?nome=` | Busca clientes pelo nome |
| `GET` | `/clientes/{id}` | Consulta cliente por ID |
| `PUT` | `/clientes/{id}` | Atualiza um cliente |
| `DELETE` | `/clientes/{id}` | Exclui um cliente |

## 📦 Exemplo de cadastro

### Requisição

`POST /clientes`

```json
{
  "nome": "Maria Silva",
  "email": "maria@email.com",
  "telefone": "51999999999"
}
```

### Resposta

```json
{
  "nome": "Maria Silva",
  "email": "maria@email.com",
  "telefone": "51999999999",
  "id": 1
}
```

## 🗄️ Banco de dados

O projeto utiliza **SQLite** para persistência dos dados.

| Campo | Descrição |
|---|---|
| `id` | Identificador único |
| `nome` | Nome do cliente |
| `email` | E-mail do cliente |
| `telefone` | Telefone do cliente |

O campo `email` possui restrição de unicidade.

## 📁 Estrutura do projeto

```text
app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
└── routers/
    └── clientes.py

tests/
└── test_api.py
```

## ▶️ Como executar

```bash
git clone https://github.com/andressahenriqueteixeira-lgtm/api-clientes-fastapi.git
cd api-clientes-fastapi
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências e execute:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API: `http://127.0.0.1:8000`

Swagger: `http://127.0.0.1:8000/docs`

ReDoc: `http://127.0.0.1:8000/redoc`

## 🧪 Testes

```bash
pytest
```

Os testes verificam o status da API, CRUD e tentativa de cadastrar e-mail duplicado.

## 💡 O que aprendi com este projeto

- Estruturação de API REST
- Métodos HTTP e CRUD
- Validação e persistência de dados
- ORM com SQLAlchemy
- Organização modular da aplicação
- Tratamento de erros HTTP
- Documentação automática
- Testes automatizados
- Git e GitHub

## 🔜 Próximas evoluções

- PostgreSQL
- Autenticação e JWT
- Alembic
- Docker
- Variáveis de ambiente
- Deploy em nuvem

## 👩‍💻 Autora

**Andressa Henrique Teixeira**

🎓 Análise e Desenvolvimento de Sistemas — UNINTER  
🎓 Engenharia de Software — UNIASSELVI  
💻 Foco: **Back-end | Python | APIs | Banco de Dados | Power BI**  
📍 Porto Alegre - RS  
📧 andressahenriqueteixeira@gmail.com
