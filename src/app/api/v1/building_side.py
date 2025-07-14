from typing import Annotated, Any, cast

from fastapi import APIRouter, Depends, Request
from fastcrud.paginated import PaginatedListResponse, compute_offset, paginated_response
from sqlalchemy.ext.asyncio import AsyncSession

from ...api.dependencies import get_current_superuser
from ...core.db.database import async_get_db
from ...core.exceptions.http_exceptions import DuplicateValueException, NotFoundException
from ...crud.crud_building_side import crud_building_side
from ...schemas.building_side import BuildingSideCreate, BuildingSideCreateInternal, BuildingSideRead, BuildingSideUpdate

router = APIRouter(tags=["building_sides"])


@router.post("/buildingside", dependencies=[Depends(get_current_superuser)], status_code=201)
async def write_building_side(
    request: Request, buildingtype: BuildingSideCreate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> BuildingSideRead:
    building_side_internal_dict = buildingtype.model_dump()
    db_building_side = await crud_building_side.exists(db=db, name=building_side_internal_dict["name"])
    if db_building_side:
        raise DuplicateValueException("Building Side not available")

    building_side_internal = BuildingSideCreateInternal(**building_side_internal_dict)
    created_building_side = await crud_building_side.create(db=db, object=building_side_internal)

    building_side_read = await crud_building_side.get(db=db, id=created_building_side.id, schema_to_select=BuildingSideRead)
    if building_side_read is None:
        raise NotFoundException("Created Building Side not found")

    return cast(BuildingSideRead, building_side_read)


@router.get("/buildingsides", response_model=PaginatedListResponse[BuildingSideRead])
async def read_building_sides(
    request: Request, db: Annotated[AsyncSession, Depends(async_get_db)], page: int = 1, items_per_page: int = 10
) -> dict:
    building_side_data = await crud_building_side.get_multi(db=db, offset=compute_offset(page, items_per_page), limit=items_per_page)

    response: dict[str, Any] = paginated_response(crud_data=building_side_data, page=page, items_per_page=items_per_page)
    return response


@router.get("/buildingside/{name}", response_model=BuildingSideRead)
async def read_building_type(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> BuildingSideRead:
    db_building_side = await crud_building_side.get(db=db, name=name, schema_to_select=BuildingSideRead)
    if db_building_side is None:
        raise NotFoundException("Building Side not found")

    return cast(BuildingSideRead, db_building_side)


@router.patch("/buildingside/{name}", dependencies=[Depends(get_current_superuser)])
async def patch_building_side(
    request: Request, name: str, values: BuildingSideUpdate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> dict[str, str]:
    db_building_side = await [[[crud_building_side]]].get(db=db, name=name, schema_to_select=BuildingSideRead)
    if db_building_side is None:
        raise NotFoundException("Building Side not found")

    await crud_building_side.update(db=db, object=values, name=name)
    return {"message": "Building Side updated"}


@router.delete("/buildingside/{name}", dependencies=[Depends(get_current_superuser)])
async def erase_building_type(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> dict[str, str]:
    db_building_type = await crud_building_type.get(db=db, name=name, schema_to_select=BuildingTypeRead)
    if db_building_type is None:
        raise NotFoundException("Building Type not found")

    await crud_building_type.delete(db=db, name=name)
    return {"message": "Building Type deleted"}
