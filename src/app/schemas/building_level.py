from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from ..core.schemas import TimestampSchema


class BuildingLevelBase(BaseModel):
    name: Annotated[str, Field(examples=["Level 1, Level 2"])]


class BuildingLevel(TimestampSchema, BuildingLevelBase):
    pass


class BuildingLevelRead(BuildingLevelBase):
    id: int
    created_at: datetime


class BuildingLevelCreate(BuildingLevelBase):
    pass


class BuildingLevelCreateInternal(BuildingLevelCreate):
    pass


class BuildingLevelUpdate(BaseModel):
    name: str | None = None


class BuildingLevelUpdateInternal(BuildingLevelUpdate):
    updated_at: datetime


class BuildingLevelDelete(BaseModel):
    pass
