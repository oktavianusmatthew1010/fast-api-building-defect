from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from ..core.schemas import TimestampSchema


class BuildingLevelBase(BaseModel):
    level_name: Annotated[str, Field(examples=["Level 1, Level 2"])]
    building_id: int | None
   
    description: str | None = None
    primary_usage: str | None = None


class BuildingLevel(TimestampSchema, BuildingLevelBase):
    pass


class BuildingLevelRead(BuildingLevelBase):
    building_id: int | None

    



class BuildingLevelCreate(BuildingLevelBase):
    pass


class BuildingLevelCreateInternal(BuildingLevelCreate):
    pass


class BuildingLevelUpdate(BaseModel):
    level_number: str | None = None


class BuildingLevelUpdateInternal(BuildingLevelUpdate):
    updated_at: datetime


class BuildingLevelDelete(BaseModel):
    pass
