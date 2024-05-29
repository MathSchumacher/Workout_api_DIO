from workout_api.contrib.schemas import BaseSchemas
from typing import Annotated
from pydantic import Field
import pydantic
from workout_api.centro_treinamento.schemas import CentroTreinamento

class CentroTreinamentoIn(BaseSchemas):
    nome: Annotated[str, Field(description = 'Nome do centro de treinamento', example = 'CT King', max_lenght=20)]
    endereco: Annotated[str, Field(description = 'Endereço do centro de treinamento', example = 'Rua X, 002', max_lenght=60)]
    proprietario: Annotated[str, Field(description = 'Proprietario do centro de treinamento', example = 'Marcos', max_lenght=30)]

class CentroTreinamentoAtleta(BaseSchemas):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]

class CentroTreinamentoOut(BaseSchemas):
    id: Annotated[pydantic.UUID4, pydantic.Field(description='Identificador do centro de treinamento')]