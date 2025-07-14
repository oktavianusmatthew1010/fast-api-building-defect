from typing import Annotated, Any, cast

from fastapi import APIRouter, Depends, Request
from fastcrud.paginated import PaginatedListResponse, compute_offset, paginated_response
from sqlalchemy.ext.asyncio import AsyncSession

from ...api.dependencies import get_current_superuser
from ...core.db.database import async_get_db
from ...core.exceptions.http_exceptions import DuplicateValueException, NotFoundException
from ...crud.crud_defect_type import crud_defect_type
from ...schemas.defect_type import DefectTypeCreate, DefectTypeCreateInternal, DefectTypeRead, DefectTypeUpdate

router = APIRouter(tags=["defect_type"])


@router.post("/defecttype", dependencies=[Depends(get_current_superuser)], status_code=201)
async def write_defect_type(
    request: Request, buildingtype: DefectTypeCreate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> DefectTypeRead:
    defect_type_internal_dict = buildingtype.model_dump()
    db_building_type = await crud_defect_type.exists(db=db, name=defect_type_internal_dict["name"])
    if db_building_type:
        raise DuplicateValueException("Building Type not available")

    defect_type_internal = DefectTypeCreateInternal(**defect_type_internal_dict)
    created_defect_type = await crud_defect_type.create(db=db, object=defect_type_internal)

    defect_type_read = await crud_defect_type.get(db=db, id=created_defect_type.id, schema_to_select=DefectTypeRead)
    if defect_type_read is None:
        raise NotFoundException("Created Building Type not found")

    return cast(DefectTypeRead, defect_type_read)


@router.get("/defecttypes", response_model=PaginatedListResponse[DefectTypeRead])
async def read_defect_types(
    request: Request, db: Annotated[AsyncSession, Depends(async_get_db)], page: int = 1, items_per_page: int = 10
) -> dict:
    defect_type_data = await crud_defect_type.get_multi(db=db, offset=compute_offset(page, items_per_page), limit=items_per_page)

    response: dict[str, Any] = paginated_response(crud_data=defect_type_data, page=page, items_per_page=items_per_page)
    return response


@router.get("/defecttype/{name}", response_model=DefectTypeRead)
async def read_defect_type(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> DefectTypeRead:
    db_defect_type = await crud_defect_type.get(db=db, name=name, schema_to_select=DefectTypeRead)
    if db_defect_type is None:
        raise NotFoundException("Building Type not found")

    return cast(DefectTypeRead, db_defect_type)


@router.patch("/defecttype/{name}", dependencies=[Depends(get_current_superuser)])
async def patch_defect_type(
    request: Request, name: str, values: DefectTypeUpdate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> dict[str, str]:
    db_defect_type = await crud_defect_type.get(db=db, name=name, schema_to_select=DefectTypeRead)
    if db_defect_type is None:
        raise NotFoundException("Building Type not found")

    await crud_defect_type.update(db=db, object=values, name=name)
    return {"message": "Building Type updated"}


@router.delete("/defecttype/{name}", dependencies=[Depends(get_current_superuser)])
async def erase_defect_type(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> dict[str, str]:
    db_defect_type = await crud_defect_type.get(db=db, name=name, schema_to_select=DefectTypeRead)
    if db_defect_type is None:
        raise NotFoundException("Building Type not found")

    await crud_defect_type.delete(db=db, name=name)
    return {"message": "Building Type deleted"}
