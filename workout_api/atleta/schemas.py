from typing import Annotated
from pydantic import Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchemas, OutMixin
from workout_api.categoria.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta

class Atleta(BaseSchemas): 
    nome: Annotated[str, Field(description = 'Nome do Atleta', example = 'Joao', max_lenght=50)]
    cpf: Annotated[str, Field(description = 'CPF do Atleta', example = '12345678900', max_lenght=11)]
    idade: Annotated[int, Field(description = 'Idade do Atleta', example = 25, max_lenght=50)]
    peso: Annotated[PositiveFloat, Field(description = 'Peso do Atleta', example = 75.5)]
    altura: Annotated[PositiveFloat, Field(description = 'Altura do Atleta', example = 1.70)]
    sexo: Annotated[str, Field(description = 'Sexo do Atleta', example = 'M', max_lenght=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]

class AtletaIn(Atleta):
    pass

class AtletaOut(AtletaIn, OutMixin):
    pass