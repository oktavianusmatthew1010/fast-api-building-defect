from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from ..core.schemas import TimestampSchema


class ProjectBase(BaseModel):
    name: Annotated[str, Field(examples=["Project Name"])]
    description: Annotated[str, Field(min_length=1, max_length=63206, examples=["This is the des "])]
    address_detail: Annotated[str, Field(min_length=1, max_length=63206, examples=["This is address"])]
    
    status:int | None = None
    created_by: int
    


class Project(TimestampSchema, ProjectBase):
    created_by: int


class ProjectRead(ProjectBase):
    id: int
    created_at: datetime
    created_by: int


class ProjectCreate(ProjectBase):
    pass


class ProjectCreateInternal(ProjectCreate):
    pass


class ProjectUpdate(BaseModel):
    name: str | None = None


class ProjectUpdateInternal(ProjectUpdate):
    updated_at: datetime
    created_by: int


class ProjectDelete(BaseModel):
    pass
