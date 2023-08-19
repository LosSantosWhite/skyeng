from .models import User
from app.db.postgresql.crud import CRUD


class UserCRUD(CRUD[User]):
    ...
