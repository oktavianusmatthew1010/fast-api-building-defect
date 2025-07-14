from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from ..core.schemas import TimestampSchema


class BuildingSideBase(BaseModel):
    name: Annotated[str, Field(examples=["North, East"])]


class BuildingSide(TimestampSchema, BuildingSideBase):
    pass


class BuildingSideRead(BuildingSideBase):
    id: int
    created_at: datetime


class BuildingSideCreate(BuildingSideBase):
    pass


class BuildingSideCreateInternal(BuildingSideCreate):
    pass


class BuildingSideUpdate(BaseModel):
    name: str | None = None


class BuildingSideUpdateInternal(BuildingSideUpdate):
    updated_at: datetime


class BuildingSideDelete(BaseModel):
    pass
