from uuid import UUID
from typing import Optional, List

from pydantic import EmailStr, model_validator

from app.modules.files.service.schemas import FileRetrieve
from app.utils.schemas import BaseOutput


class UserRetrieve(BaseOutput):
    uuid: UUID | str
    email: EmailStr
    files: Optional[List[FileRetrieve]] = []


class UserRegistration(BaseOutput):
    email: EmailStr
    password_1: str
    password_2: str

    @model_validator(mode="after")
    def scheck_password(self) -> "UserRegistration":
        if (
            self.password_1 is not None
            and self.password_2 is not None
            and self.password_1 != self.password_2
        ):
            raise ValueError("Пароли не совпадают")
        return self
