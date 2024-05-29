from uuid import uuid4
from fastapi import APIRouter, HTTPException, status, Body
from pydantic import UUID4
from workout_api.contrib.dependencies import DatabaseDependency
from workout_api.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from sqlalchemy.future import select

router = APIRouter()
@router.post('/', summary='Criar um novo centro de Treinamento', status_code=status.HTTP_201_CREATED, response_model=CentroTreinamentoOut,)
async def post(db_session: DatabaseDependency, centrotreino_in: CentroTreinamentoIn = Body(...)) -> CentroTreinamentoOut:
    centrotreino_out=CentroTreinamentoOut(id=uuid4(), **centrotreino_in.model_dump())
    centrotreino_model=CentroTreinamentoModel(**centrotreino_out.model_dump())
    
    db_session.add(centrotreino_model)
    await db_session.commit()

    return centrotreino_out

@router.get('/', summary='Consultar todos os centros de treinamento', status_code=status.HTTP_200_OK, response_model=list[CentroTreinamentoOut])
async def query(db_session: DatabaseDependency, ) -> list[CentroTreinamentoOut]:
    categorias: list[CentroTreinamentoOut] = (await db_session.execute(select(CentroTreinamentoOut))).scalars().all()
    return categorias

@router.get('/{id}', summary='Consulta um Centro de treinamento pelo id', status_code=status.HTTP_200_OK, response_model=CentroTreinamentoOut)
async def query(id: UUID4, db_session: DatabaseDependency, ) -> CentroTreinamentoOut:
    categoria: list[CentroTreinamentoOut] = (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))).scalars().first()
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Centro de treinamento não encontrado no id: {id}')
    return categoria