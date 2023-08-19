from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.postgresql.dependencies import get_async_session

from .base import UserService


def get_user_service(session: AsyncSession = Depends(get_async_session)) -> UserService:
    return UserService(session=session)
