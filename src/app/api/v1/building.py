from typing import Annotated, Any, cast

from fastapi import APIRouter, Depends, Request
from fastcrud.paginated import PaginatedListResponse, compute_offset, paginated_response
from sqlalchemy.ext.asyncio import AsyncSession

from ...api.dependencies import get_current_superuser
from ...core.db.database import async_get_db
from ...core.exceptions.http_exceptions import DuplicateValueException, NotFoundException
from ...crud.crud_building import crud_building
from ...schemas.building import BuildingCreate, BuildingCreateInternal, BuildingRead, BuildingUpdate

router = APIRouter(tags=["buildings"])


@router.post("/building", dependencies=[Depends(get_current_superuser)], status_code=201)
async def write_building(
    request: Request, building: BuildingCreate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> BuildingRead:
    building_internal_dict = building.model_dump()
    db_building = await crud_building.exists(db=db, name=building_internal_dict["name"])
    if db_building:
        raise DuplicateValueException("Building Name not available")

    building_internal = BuildingCreateInternal(**building_internal_dict)
    created_building = await crud_building.create(db=db, object=building_internal)

    building_read = await crud_building.get(db=db, id=created_building.id, schema_to_select=BuildingRead)
    if building_read is None:
        raise NotFoundException("Created Building not found")

    return cast(BuildingRead, building_read)


@router.get("/buildings", response_model=PaginatedListResponse[BuildingRead])
async def read_buildings(
    request: Request, db: Annotated[AsyncSession, Depends(async_get_db)], page: int = 1, items_per_page: int = 10
) -> dict:
    buildings_data = await crud_building.get_multi(db=db, offset=compute_offset(page, items_per_page), limit=items_per_page)

    response: dict[str, Any] = paginated_response(crud_data=buildings_data, page=page, items_per_page=items_per_page)
    return response


@router.get("/building/{name}", response_model=BuildingRead)
async def read_building(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> BuildingRead:
    db_building = await crud_building.get(db=db, name=name, schema_to_select=BuildingRead)
    if db_building is None:
        raise NotFoundException("Building not found")

    return cast(BuildingRead, db_building)


@router.patch("/building/{name}", dependencies=[Depends(get_current_superuser)])
async def patch_building(
    request: Request, name: str, values: BuildingUpdate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> dict[str, str]:
    db_building = await crud_building.get(db=db, name=name, schema_to_select=BuildingRead)
    if db_building is None:
        raise NotFoundException("Building not found")

    await crud_building.update(db=db, object=values, name=name)
    return {"message": "Building updated"}


@router.delete("/building/{name}", dependencies=[Depends(get_current_superuser)])
async def erase_building(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> dict[str, str]:
    db_building = await crud_building.get(db=db, name=name, schema_to_select=BuildingRead)
    if db_building is None:
        raise NotFoundException("Building not found")

    await crud_building.delete(db=db, name=name)
    return {"message": "Building deleted"}
