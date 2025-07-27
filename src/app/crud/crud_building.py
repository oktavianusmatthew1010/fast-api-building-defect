from fastcrud import FastCRUD
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.building import Building
from ..models.building import Building
from ..schemas.building import BuildingCreateInternal, BuildingDelete, BuildingRead, BuildingUpdate, BuildingUpdateInternal

CRUDBuilding = FastCRUD[Building, BuildingCreateInternal, BuildingUpdate, BuildingUpdateInternal, BuildingDelete, BuildingRead]
crud_building = CRUDBuilding(Building)


async def get_multi(db: AsyncSession, *, offset: int = 0, limit: int = 100):
    result = await db.execute(
        select(Building)
        .options(selectinload(Building.project))  # Explicitly load the project
        .offset(offset)
        .limit(limit)
    )
    return result.scalars().all()


