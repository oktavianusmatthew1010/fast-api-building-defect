from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from ..core.schemas import TimestampSchema


class DefectTypeBase(BaseModel):
    name: Annotated[str, Field(examples=["Crack"])]


class DefectType(TimestampSchema, DefectTypeBase):
    pass


class DefectTypeRead(DefectTypeBase):
    id: int
    created_at: datetime


class DefectTypeCreate(DefectTypeBase):
    pass


class DefectTypeCreateInternal(DefectTypeCreate):
    pass


class DefectTypeUpdate(BaseModel):
    name: str | None = None


class DefectTypeUpdateInternal(DefectTypeUpdate):
    updated_at: datetime


class DefectTypeDelete(BaseModel):
    pass
