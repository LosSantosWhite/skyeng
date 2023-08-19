from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.postgresql.base import Base
from app.db.postgresql.models import ID, TIMESTAMP, Deleted

if TYPE_CHECKING:
    from app.modules.files.crud.models import File


class User(Base, ID, TIMESTAMP, Deleted):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password_hash: Mapped[str]

    files: Mapped[List["File"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.uuid}, email={self.email})"
