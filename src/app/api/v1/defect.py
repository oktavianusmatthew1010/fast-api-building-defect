from typing import Annotated, Any, cast

from fastapi import APIRouter, Depends, Request
from fastcrud.paginated import PaginatedListResponse, compute_offset, paginated_response
from sqlalchemy.ext.asyncio import AsyncSession

from ...api.dependencies import get_current_superuser
from ...core.db.database import async_get_db
from ...core.exceptions.http_exceptions import DuplicateValueException, NotFoundException
from ...crud.crud_defect import crud_defect
from ...schemas.defect import DefectCreate, DefectCreateInternal, DefectRead, DefectUpdate

router = APIRouter(tags=["defect"])


@router.post("/defect", dependencies=[Depends(get_current_superuser)], status_code=201)
async def write_defect(
    request: Request, defect: DefectCreate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> DefectRead:
    defect_internal_dict = defect.model_dump()
    db_defect = await crud_defect.exists(db=db, name=defect_internal_dict["name"])
    if db_defect:
        raise DuplicateValueException("Defect not available")

    defect_internal = DefectCreateInternal(**defect_internal_dict)
    created_defect = await crud_defect.create(db=db, object=defect_internal)

    defect_read = await crud_defect.get(db=db, id=created_defect.id, schema_to_select=DefectRead)
    if defect_read is None:
        raise NotFoundException("Created Defect not found")

    return cast(DefectRead, defect_read)


@router.get("/defect", response_model=PaginatedListResponse[DefectRead])
async def read_defect(
    request: Request, db: Annotated[AsyncSession, Depends(async_get_db)], page: int = 1, items_per_page: int = 10
) -> dict:
    defect_data = await crud_defect.get_multi(db=db, offset=compute_offset(page, items_per_page), limit=items_per_page)

    response: dict[str, Any] = paginated_response(crud_data=defect_data, page=page, items_per_page=items_per_page)
    return response


@router.get("/defect/{name}", response_model=DefectRead)
async def read_defect(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> DefectRead:
    db_defect = await crud_defect.get(db=db, name=name, schema_to_select=DefectRead)
    if db_defect is None:
        raise NotFoundException("Defect not found")

    return cast(DefectRead, db_defect)


@router.patch("/defect/{name}", dependencies=[Depends(get_current_superuser)])
async def patch_defect(
    request: Request, name: str, values: DefectUpdate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> dict[str, str]:
    db_defect = await crud_defect.get(db=db, name=name, schema_to_select=DefectRead)
    if db_defect is None:
        raise NotFoundException("Defect not found")

    await crud_defect.update(db=db, object=values, name=name)
    return {"message": "Defect updated"}


@router.delete("/defect/{name}", dependencies=[Depends(get_current_superuser)])
async def erase_defect(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> dict[str, str]:
    db_defect = await crud_defect.get(db=db, name=name, schema_to_select=DefectRead)
    if db_defect is None:
        raise NotFoundException("Defect not found")

    await crud_defect.delete(db=db, name=name)
    return {"message": "Defect  deleted"}
