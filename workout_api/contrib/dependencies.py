from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from workout_api.configs.database import get_session

DatabaseDependency = Annotated(AsyncSession, Depends(get_session))
