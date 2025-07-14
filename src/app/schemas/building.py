from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from ..core.schemas import TimestampSchema


class BuildingBase(BaseModel):
    name: Annotated[str, Field(examples=["free"])]


class Building(TimestampSchema, BuildingBase):
    pass


class BuildingRead(BuildingBase):
    id: int
    created_at: datetime


class BuildingCreate(BuildingBase):
    pass


class BuildingCreateInternal(BuildingCreate):
    pass


class BuildingUpdate(BaseModel):
    name: str | None = None


class BuildingUpdateInternal(BuildingUpdate):
    updated_at: datetime


class BuildingDelete(BaseModel):
    pass
