from .models import File
from app.db.postgresql.crud import CRUD


class FileCRUD(CRUD[File]):
    ...
