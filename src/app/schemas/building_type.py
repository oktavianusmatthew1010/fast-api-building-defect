from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from ..core.schemas import TimestampSchema


class BuildingTypeBase(BaseModel):
    name: Annotated[str, Field(examples=["Apartment"])]


class BuildingType(TimestampSchema, BuildingTypeBase):
    pass


class BuildingTypeRead(BuildingTypeBase):
    id: int
    created_at: datetime


class BuildingTypeCreate(BuildingTypeBase):
    pass


class BuildingTypeCreateInternal(BuildingTypeCreate):
    pass


class BuildingTypeUpdate(BaseModel):
    name: str | None = None


class BuildingTypeUpdateInternal(BuildingTypeUpdate):
    updated_at: datetime


class BuildingTypeDelete(BaseModel):
    pass
