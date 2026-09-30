from sqlalchemy.orm import Session
from . import models, schemas


def criar_cliente(db: Session, dados: schemas.ClienteCreate):
    cliente = models.Cliente(**dados.model_dump())
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente


def listar_clientes(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Cliente)
        .order_by(models.Cliente.nome)
        .offset(skip)
        .limit(limit)
        .all()
    )


def obter_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()


def obter_por_email(db: Session, email: str):
    return db.query(models.Cliente).filter(models.Cliente.email == email).first()


def buscar_por_nome(db: Session, nome: str):
    return (
        db.query(models.Cliente)
        .filter(models.Cliente.nome.ilike(f"%{nome}%"))
        .order_by(models.Cliente.nome)
        .all()
    )


def atualizar_cliente(db: Session, cliente, dados: schemas.ClienteUpdate):
    alteracoes = dados.model_dump(exclude_unset=True)
    for campo, valor in alteracoes.items():
        setattr(cliente, campo, valor)
    db.commit()
    db.refresh(cliente)
    return cliente


def excluir_cliente(db: Session, cliente):
    db.delete(cliente)
    db.commit()
