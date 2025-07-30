from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from ..core.schemas import TimestampSchema


class BuildingSideBase(BaseModel):
    name: Annotated[str, Field(examples=["North, East"])]
    building_id: Annotated[int, Field(examples=["1"])]
    description: Annotated[str | None, Field(max_length=255, default=None)]
    orientation_degrees:Annotated[float, Field(examples=["0.0"])]
class BuildingSide(TimestampSchema, BuildingSideBase):
    pass


class BuildingSideRead(BuildingSideBase):
    id: int
    created_at: datetime


class BuildingSideCreate(BuildingSideBase):
    building_id: int


class BuildingSideCreateInternal(BuildingSideCreate):
    pass


class BuildingSideUpdate(BaseModel):
    name: str | None = None


class BuildingSideUpdateInternal(BuildingSideUpdate):
    updated_at: datetime


class BuildingSideDelete(BaseModel):
    pass
