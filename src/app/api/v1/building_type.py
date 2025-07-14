from typing import Annotated, Any, cast

from fastapi import APIRouter, Depends, Request
from fastcrud.paginated import PaginatedListResponse, compute_offset, paginated_response
from sqlalchemy.ext.asyncio import AsyncSession

from ...api.dependencies import get_current_superuser
from ...core.db.database import async_get_db
from ...core.exceptions.http_exceptions import DuplicateValueException, NotFoundException
from ...crud.crud_building_type import crud_building_type
from ...schemas.building_type import BuildingTypeCreate, BuildingTypeCreateInternal, BuildingTypeRead, BuildingTypeUpdate

router = APIRouter(tags=["building_types"])


@router.post("/buildingtype", dependencies=[Depends(get_current_superuser)], status_code=201)
async def write_building_type(
    request: Request, buildingtype: BuildingTypeCreate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> BuildingTypeRead:
    building_type_internal_dict = buildingtype.model_dump()
    db_building_type = await crud_building_type.exists(db=db, name=building_type_internal_dict["name"])
    if db_building_type:
        raise DuplicateValueException("Building Type not available")

    building_type_internal = BuildingTypeCreateInternal(**building_type_internal_dict)
    created_building_type = await crud_building_type.create(db=db, object=building_type_internal)

    building_type_read = await crud_building_type.get(db=db, id=created_building_type.id, schema_to_select=BuildingTypeRead)
    if building_type_read is None:
        raise NotFoundException("Created Building Type not found")

    return cast(BuildingTypeRead, building_type_read)


@router.get("/buildingtypes", response_model=PaginatedListResponse[BuildingTypeRead])
async def read_building_types(
    request: Request, db: Annotated[AsyncSession, Depends(async_get_db)], page: int = 1, items_per_page: int = 10
) -> dict:
    building_type_data = await crud_building_type.get_multi(db=db, offset=compute_offset(page, items_per_page), limit=items_per_page)

    response: dict[str, Any] = paginated_response(crud_data=building_type_data, page=page, items_per_page=items_per_page)
    return response


@router.get("/buildingtype/{name}", response_model=BuildingTypeRead)
async def read_building_type(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> BuildingTypeRead:
    db_building_type = await crud_building_type.get(db=db, name=name, schema_to_select=BuildingTypeRead)
    if db_building_type is None:
        raise NotFoundException("Building Type not found")

    return cast(BuildingTypeRead, db_building_type)


@router.patch("/buildingtype/{name}", dependencies=[Depends(get_current_superuser)])
async def patch_building_type(
    request: Request, name: str, values: BuildingTypeUpdate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> dict[str, str]:
    db_building_type = await crud_building_type.get(db=db, name=name, schema_to_select=BuildingTypeRead)
    if db_building_type is None:
        raise NotFoundException("Building Type not found")

    await crud_building_type.update(db=db, object=values, name=name)
    return {"message": "Building Type updated"}


@router.delete("/buildingtype/{name}", dependencies=[Depends(get_current_superuser)])
async def erase_building_type(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> dict[str, str]:
    db_building_type = await crud_building_type.get(db=db, name=name, schema_to_select=BuildingTypeRead)
    if db_building_type is None:
        raise NotFoundException("Building Type not found")

    await crud_building_type.delete(db=db, name=name)
    return {"message": "Building Type deleted"}
