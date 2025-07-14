from datetime import datetime
from typing import Annotated
from pydantic import BaseModel, Field, ConfigDict


class CategoryBase(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=50)]
    description: Annotated[str | None, Field(max_length=255, default=None)]


class CategoryCreate(CategoryBase):
    model_config = ConfigDict(extra="forbid")


class CategoryRead(CategoryBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    created_at: datetime

class CategoryCreateInternal(CategoryCreate):
    pass

class CategoryUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    name: Annotated[str | None, Field(min_length=1, max_length=50, default=None)]
    description: Annotated[str | None, Field(max_length=255, default=None)]


class CategoryUpdateInternal(CategoryUpdate):
    updated_at: datetime


class CategoryDelete(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    is_deleted: bool
    deleted_at: datetime

