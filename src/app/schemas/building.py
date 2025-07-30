from datetime import datetime
from typing import Annotated, Optional
from pydantic import BaseModel, Field
from ..core.schemas import TimestampSchema
from ..schemas.project import Project, ProjectRead


class ProjectRead(BaseModel):
    name: str
    description: str
    address_detail: str
    status: int
    created_by: int
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
    

class BuildingBase(BaseModel):
    name: Annotated[str, Field(examples=["My Building"])]
    address: Annotated[str, Field(examples=["123 Example Street"])]
    year_built: Annotated[int, Field(examples=[2005])]
    building_type: Annotated[int, Field(examples=[1])]
    area_sq_meters: Annotated[float, Field(examples=[1234.56])]
    levels_count: Annotated[int, Field(examples=[5])]
    sides_count: Annotated[int, Field(examples=[4])]
    owner_id: Annotated[int, Field(examples=[1])]
    project_id: Optional[int] = None
    latitude: Annotated[float, Field(examples=[1.2345])]
    longitude: Annotated[float, Field(examples=[103.5678])]
    status_construction: Annotated[float, Field(examples=[0.5])]
    construction_start_date: Optional[datetime] = None
    construction_end_date: Optional[datetime] = None
    
    class Config:
        from_attributes = True
        
class BuildingWithProject(BuildingBase):
    project: Optional["ProjectRead"] = None  # Reference to project schema

    

class Building(TimestampSchema, BuildingBase):
    
    id: int
    is_deleted: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class BuildingRead(Building):
    
    project: Optional[ProjectRead] = None
    
    class Config:
        from_attributes = True
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
BuildingWithProject.update_forward_refs()


def format_building_response(building: BuildingBase) -> dict:
    return {
        "name": building.name,
        "address": building.address,
        "year_built": building.year_built,
        "building_type": building.building_type,
        "area_sq_meters": building.area_sq_meters,
        "levels_count": building.levels_count,
        "sides_count": building.sides_count,
        "owner_id": building.owner_id,
        "project_id": building.project_id if building.project_id else 0,
        "latitude": building.latitude,
        "longitude": building.longitude,
        "status_construction": building.status_construction,
        "construction_start_date": building.construction_start_date.isoformat() + "Z" if building.construction_start_date else None,
        "construction_end_date": building.construction_end_date.isoformat() + "Z" if building.construction_end_date else None,
        "created_at": "string",  # Or use actual value
        "updated_at": "string",  # Or use actual value
        "id": building.id,
        "is_deleted": building.is_deleted,
        "deleted_at": building.deleted_at.isoformat() + "Z" if building.deleted_at else None,
        "project": {
            "name": building.project.name if building.project else "string",
            "description": building.project.description if building.project else "string",
            "address_detail": building.project.address_detail if building.project else "string",
            "status": building.project.status if building.project else 0,
            "created_by": building.project.created_by if building.project else 0,
            "id": building.project.id if building.project else 0,
            "created_at": building.project.created_at.isoformat() + "Z" if building.project and building.project.created_at else "2025-07-27T04:44:00.859Z"
        } if building.project_id else {
            "name": "string",
            "description": "string",
            "address_detail": "string",
            "status": 0,
            "created_by": 0,
            "id": 0,
            "created_at": "2025-07-27T04:44:00.859Z"
        }
    }

def format_building_add_response(building: BuildingBase) -> dict:
    return {
        "name": building.name,
        "address": building.address,
        "year_built": building.year_built,
        "building_type": building.building_type,
        "area_sq_meters": building.area_sq_meters,
        "levels_count": building.levels_count,
        "sides_count": building.sides_count,
        "owner_id": building.owner_id,
        "project_id": building.project_id if building.project_id else 0,
        "latitude": building.latitude,
        "longitude": building.longitude,
        "status_construction": building.status_construction,
        "construction_start_date": building.construction_start_date.isoformat() + "Z" if building.construction_start_date else None,
        "construction_end_date": building.construction_end_date.isoformat() + "Z" if building.construction_end_date else None,
        "created_at": "string",  # Or use actual value
        "updated_at": "string",  # Or use actual value
        "id": building.id,
        "is_deleted": building.is_deleted,
        "deleted_at": building.deleted_at.isoformat() + "Z" if building.deleted_at else None,
        "project": {
            "name": building.project.name if building.project else "string",
            "description": building.project.description if building.project else "string",
            "address_detail": building.project.address_detail if building.project else "string",
            "status": building.project.status if building.project else 0,
            "created_by": building.project.created_by if building.project else 0,
            "id": building.project.id if building.project else 0,
            "created_at": building.project.created_at.isoformat() + "Z" if building.project and building.project.created_at else "2025-07-27T04:44:00.859Z"
        } if building.project_id else {
            "name": "string",
            "description": "string",
            "address_detail": "string",
            "status": 0,
            "created_by": 0,
            "id": 0,
            "created_at": "2025-07-27T04:44:00.859Z"
        }
    }