from datetime import datetime
from typing import Annotated
from pydantic import BaseModel, Field, ConfigDict


class SubCategoryBase(BaseModel):
    category_id : int
    subcategory: Annotated[str, Field(min_length=1, max_length=50)]
    description: Annotated[str | None, Field(max_length=255, default=None)]
    

class SubCategoryCreate(SubCategoryBase):
    model_config = ConfigDict(extra="forbid")


class SubCategoryRead(SubCategoryBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    created_at: datetime


class SubCategoryUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    subcategory: Annotated[str | None, Field(min_length=1, max_length=50, default=None)]
    description: Annotated[str | None, Field(max_length=255, default=None)]

class SubCategoryCreateInternal(SubCategoryCreate):
    pass

class SubCategoryUpdateInternal(SubCategoryUpdate):
    updated_at: datetime


class SubCategoryDelete(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    is_deleted: bool
    deleted_at: datetime