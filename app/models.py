from sqlalchemy import Column, Integer, String
from .database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(120), nullable=False, index=True)
    email = Column(String(180), nullable=False, unique=True, index=True)
    telefone = Column(String(20), nullable=True)
