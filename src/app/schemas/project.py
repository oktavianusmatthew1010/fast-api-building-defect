from datetime import datetime
from typing import Annotated, Optional

from pydantic import BaseModel, Field

from ..core.schemas import TimestampSchema


class ProjectBase(BaseModel):
    name: Annotated[str, Field(examples=["Project Name"])]
    description: Annotated[str, Field(min_length=1, max_length=63206, examples=["This is the des "])]
    address_detail: Optional[str] = ""
    status:int | None = None
   
    


class Project(TimestampSchema, ProjectBase):
    id: int
    is_deleted: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class ProjectRead(ProjectBase):
    id: int
  


class ProjectCreate(ProjectBase):
    pass


class ProjectCreateInternal(ProjectCreate):
    created_by: int


class ProjectUpdate(BaseModel):
    name: str | None = None


class ProjectUpdateInternal(ProjectUpdate):
    updated_at: datetime
   


class ProjectDelete(BaseModel):
    pass
