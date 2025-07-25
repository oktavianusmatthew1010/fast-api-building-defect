from datetime import datetime
from typing import Annotated, Optional
from pydantic import BaseModel, Field
from ..core.schemas import TimestampSchema
from ..schemas.project import ProjectRead


class ProjectRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

class BuildingBase(BaseModel):
    name: Annotated[str, Field(examples=["My Building"])]
    address: Annotated[str, Field(examples=["123 Example Street"])]
    year_built: Annotated[int, Field(examples=[2005])]
    building_type: Annotated[int, Field(examples=[1])]
    area_sq_meters: Annotated[float, Field(examples=[1234.56])]
    levels_count: Annotated[int, Field(examples=[5])]
    sides_count: Annotated[int, Field(examples=[4])]
    owner_id: Annotated[int, Field(examples=[1])]
    project_id: Annotated[int, Field(examples=[1001])]
    latitude: Annotated[float, Field(examples=[1.2345])]
    longitude: Annotated[float, Field(examples=[103.5678])]
    status_construction: Annotated[float, Field(examples=[0.5])]
    construction_start_date: Optional[datetime] = None
    construction_end_date: Optional[datetime] = None
    

class Building(TimestampSchema, BuildingBase):
    id: int
    is_deleted: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class BuildingRead(Building):
    project: Optional[ProjectRead] = None

    class Config:
        orm_mode = True


class BuildingCreate(BuildingBase):
    pass


class BuildingCreateInternal(BuildingCreate):
    pass


class BuildingUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    year_built: Optional[int] = None
    building_type: Optional[int] = None
    area_sq_meters: Optional[float] = None
    levels_count: Optional[int] = None
    sides_count: Optional[int] = None
    owner_id: Optional[int] = None
    project_id: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    status_construction: Optional[float] = None
    construction_start_date: Optional[datetime] = None
    construction_end_date: Optional[datetime] = None


class BuildingUpdateInternal(BuildingUpdate):
    updated_at: datetime


class BuildingDelete(BaseModel):
    pass
