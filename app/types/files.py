from sqlalchemy import event

from app.db.postgresql.base import Base
from .base import BaseEnum


class FileStatus(BaseEnum):
    NEW = "new"
    CHANGED = "changed"

    @classmethod
    def pg_name(cls):
        return "files_status"


@event.listens_for(Base.metadata, "before_create")
def _create_enums(metadata, conn, **kwargs):
    FileStatus.as_pg_enum(name=FileStatus.pg_name()).create(conn, checkfirst=True)
