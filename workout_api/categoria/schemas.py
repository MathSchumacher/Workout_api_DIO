from workout_api.contrib.schemas import BaseSchemas
from typing import Annotated
from pydantic import UUID4, Field

class CategoriaIn(BaseSchemas):
    nome: Annotated[str, Field(description = 'Nome da Categoria', example = 'Scale', max_lenght=10)]

class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description='Identificador da categoria')]