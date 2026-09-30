from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.post(
    "",
    response_model=schemas.ClienteResponse,
    status_code=status.HTTP_201_CREATED,
)
def criar_cliente(dados: schemas.ClienteCreate, db: Session = Depends(get_db)):
    if crud.obter_por_email(db, str(dados.email)):
        raise HTTPException(status_code=409, detail="E-mail já cadastrado.")
    return crud.criar_cliente(db, dados)


@router.get("", response_model=list[schemas.ClienteResponse])
def listar_clientes(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return crud.listar_clientes(db, skip, limit)


@router.get("/buscar", response_model=list[schemas.ClienteResponse])
def buscar_clientes(
    nome: str = Query(min_length=1),
    db: Session = Depends(get_db),
):
    return crud.buscar_por_nome(db, nome)


@router.get("/{cliente_id}", response_model=schemas.ClienteResponse)
def obter_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = crud.obter_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    return cliente


@router.put("/{cliente_id}", response_model=schemas.ClienteResponse)
def atualizar_cliente(
    cliente_id: int,
    dados: schemas.ClienteUpdate,
    db: Session = Depends(get_db),
):
    cliente = crud.obter_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")

    if dados.email is not None:
        existente = crud.obter_por_email(db, str(dados.email))
        if existente and existente.id != cliente_id:
            raise HTTPException(status_code=409, detail="E-mail já cadastrado.")

    return crud.atualizar_cliente(db, cliente, dados)


@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = crud.obter_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    crud.excluir_cliente(db, cliente)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
