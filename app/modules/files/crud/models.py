from uuid import UUID
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.postgresql.base import Base
from app.db.postgresql.models import ID, TIMESTAMP, Deleted
from app.types.files import FileStatus

if TYPE_CHECKING:
    from app.modules.users.crud.models import User


class File(Base, ID, TIMESTAMP, Deleted):
    __tablename__ = "files"

    STATUS = FileStatus

    path: Mapped[str]
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.uuid"))
    status: Mapped[FileStatus] = mapped_column(
        "status",
        FileStatus.as_pg_enum(
            name=FileStatus.pg_name(),
        ),
        nullable=False,
    )

    user: Mapped["User"] = relationship(back_populates="files")

    def __repr__(self) -> str:
        return f"File(id={self.uuid}, email={self.path})"
