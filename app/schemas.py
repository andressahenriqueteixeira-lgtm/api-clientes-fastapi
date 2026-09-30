import re
from pydantic import BaseModel, EmailStr, Field, field_validator


class ClienteBase(BaseModel):
    nome: str = Field(min_length=2, max_length=120)
    email: EmailStr
    telefone: str | None = Field(default=None, max_length=20)

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor: str) -> str:
        valor = " ".join(valor.split())
        if len(valor) < 2:
            raise ValueError("O nome deve possuir pelo menos 2 caracteres.")
        return valor

    @field_validator("telefone")
    @classmethod
    def validar_telefone(cls, valor: str | None) -> str | None:
        if valor is None or not valor.strip():
            return None
        somente_digitos = re.sub(r"\D", "", valor)
        if len(somente_digitos) < 10 or len(somente_digitos) > 13:
            raise ValueError("Informe um telefone válido com DDD.")
        return somente_digitos


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    nome: str | None = Field(default=None, min_length=2, max_length=120)
    email: EmailStr | None = None
    telefone: str | None = Field(default=None, max_length=20)

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor: str | None) -> str | None:
        if valor is None:
            return None
        valor = " ".join(valor.split())
        if len(valor) < 2:
            raise ValueError("O nome deve possuir pelo menos 2 caracteres.")
        return valor

    @field_validator("telefone")
    @classmethod
    def validar_telefone(cls, valor: str | None) -> str | None:
        if valor is None or not valor.strip():
            return None
        somente_digitos = re.sub(r"\D", "", valor)
        if len(somente_digitos) < 10 or len(somente_digitos) > 13:
            raise ValueError("Informe um telefone válido com DDD.")
        return somente_digitos


class ClienteResponse(ClienteBase):
    id: int

    model_config = {"from_attributes": True}
