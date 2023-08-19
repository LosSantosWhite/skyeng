from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.users.crud.base import UserCRUD


class UserService:
    def __init__(self, session: "AsyncSession"):
        self.session = session
        self.user = UserCRUD(session=self.session)
