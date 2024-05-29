from uuid import uuid4, UUID
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

# Definir a base declarativa
Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, primary_key=True, nullable=False)

# Exemplo de modelo que herda de BaseModel
class User(BaseModel):
    __tablename__ = 'users'
    name: Mapped[str] = mapped_column(String, nullable=False)

# Configuração do motor de conexão (Substitua 'username', 'password' e 'mydatabase' pelas suas credenciais)
#engine = create_engine('postgresql+asyncpg://workout:workout@localhost/workout')

# Criar todas as tabelas
#Base.metadata.create_all(engine)
