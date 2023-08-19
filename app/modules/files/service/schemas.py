from uuid import UUID

from app.utils.schemas import BaseOutput


class FileRetrieve(BaseOutput):
    uuid: UUID | str
    path: str
