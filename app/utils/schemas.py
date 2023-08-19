from datetime import date, datetime
from pydantic import BaseModel, ConfigDict


class BaseOutput(BaseModel):
    config = ConfigDict(from_attributes=True)

    def model_dump(self, *args, **kwargs):
        values = super().model_dump(*args, **kwargs)
        for k, v in values.items():
            if isinstance(v, (datetime, date)):
                values[k] = v.replace(tzinfo=None)

        return values
