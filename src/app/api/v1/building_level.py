from typing import Annotated, Any, cast

from fastapi import APIRouter, Depends, Request
from fastcrud.paginated import PaginatedListResponse, compute_offset, paginated_response
from sqlalchemy.ext.asyncio import AsyncSession

from ...api.dependencies import get_current_superuser
from ...core.db.database import async_get_db
from ...core.exceptions.http_exceptions import DuplicateValueException, NotFoundException
from ...crud.crud_building_level import crud_building_level
from ...schemas.building_level import BuildingLevelCreate, BuildingLevelCreateInternal, BuildingLevelRead, BuildingLevelUpdate

router = APIRouter(tags=["building_level"])


@router.post("/buildinglevel", dependencies=[Depends(get_current_superuser)], status_code=201)
async def write_building_level(
    request: Request, building_level: BuildingLevelCreate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> BuildingLevelRead:
    building_level_internal_dict = building_level.model_dump()
    building_level_internal = BuildingLevelCreateInternal(**building_level_internal_dict)
    created_building_level = await crud_building_level.create(db=db, object=building_level_internal)

    building_level_read = await crud_building_level.get(db=db, id=created_building_level.id, schema_to_select=BuildingLevelRead)
    if building_level_read is None:
        raise NotFoundException("Created Building Level not found")

    return cast(BuildingLevelRead, building_level_read)


@router.get("/buildinglevels", response_model=PaginatedListResponse[BuildingLevelRead])
async def read_building_levels(
    request: Request, db: Annotated[AsyncSession, Depends(async_get_db)], page: int = 1, items_per_page: int = 10
) -> dict:
    building_level_data = await crud_building_level.get_multi(db=db, offset=compute_offset(page, items_per_page), limit=items_per_page)

    response: dict[str, Any] = paginated_response(crud_data=building_level_data, page=page, items_per_page=items_per_page)
    return response


@router.get("/buildinglevel/{building_id}", response_model=PaginatedListResponse[BuildingLevelRead])
async def read_building_levels(
    request: Request,
    building_id: int,
    db: Annotated[AsyncSession, Depends(async_get_db)],
    page: int = 1,
    items_per_page: int = 10
) -> dict:
    building_level_data = await crud_building_level.get_multi(
        db=db,
        building_id=building_id,
        offset=compute_offset(page, items_per_page),
        limit=items_per_page
    )
    response = paginated_response(crud_data=building_level_data, page=page, items_per_page=items_per_page)
    return response



@router.patch("/buildinglevel/{name}", dependencies=[Depends(get_current_superuser)])
async def patch_building_level(
    request: Request, name: str, values: BuildingLevelUpdate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> dict[str, str]:
    db_building_level = await crud_building_level.get(db=db, name=name, schema_to_select=BuildingLevelRead)
    if db_building_level is None:
        raise NotFoundException("Building Level not found")

    await crud_building_level.update(db=db, object=values, name=name)
    return {"message": "Building Level updated"}


@router.delete("/buildinglevel/{name}", dependencies=[Depends(get_current_superuser)])
async def erase_building_level(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> dict[str, str]:
    db_building_level = await crud_building_level.get(db=db, name=name, schema_to_select=BuildingLevelRead)
    if db_building_level is None:
        raise NotFoundException("Building Level not found")

    await crud_building_level.delete(db=db, name=name)
    return {"message": "Building Level deleted"}
