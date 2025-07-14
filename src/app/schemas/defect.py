from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from ..core.schemas import TimestampSchema


class DefectBase(BaseModel):
    name: Annotated[str, Field(examples=["Crack"])]
    defect_type_id : int


class Defect(TimestampSchema, DefectBase):
    pass


class DefectRead(DefectBase):
    id: int
    created_at: datetime


class DefectCreate(DefectBase):
    pass


class DefectCreateInternal(DefectCreate):
    pass


class DefectUpdate(BaseModel):
    name: str | None = None


class DefectUpdateInternal(DefectUpdate):
    updated_at: datetime


class DefectDelete(BaseModel):
    pass
