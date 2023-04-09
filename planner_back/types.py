from datetime import datetime

from pydantic import BaseModel


class GetEvent(BaseModel):
    id: int | None
    title: str
    description: str | None
    start_date: datetime
    end_date: datetime
    location: str | None

    class Config:
        orm_mode = True


class CreateEvent(GetEvent):
    pass
