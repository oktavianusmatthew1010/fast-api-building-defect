from typing import Annotated, Any, cast

from fastapi import APIRouter, Depends, Request
from fastcrud.paginated import PaginatedListResponse, compute_offset, paginated_response
from sqlalchemy.ext.asyncio import AsyncSession

from ...api.dependencies import get_current_superuser
from ...core.db.database import async_get_db
from ...core.exceptions.http_exceptions import DuplicateValueException, NotFoundException
from ...crud.crud_sub_category import crud_sub_category
from ...schemas.subcategory import SubCategoryCreate, SubCategoryCreateInternal, SubCategoryRead, SubCategoryUpdate

router = APIRouter(tags=["subcategory"])


@router.post("/subcategory", dependencies=[Depends(get_current_superuser)], status_code=201)
async def write_subcategory(
    request: Request, subcategory: SubCategoryCreate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> SubCategoryRead:
    subcategory_internal_dict = subcategory.model_dump()
    db_subcategory = await crud_sub_category.exists(db=db, name=subcategory_internal_dict["name"])
    if db_subcategory:
        raise DuplicateValueException("Sub Category Name not available")

    subcategory_internal = SubCategoryCreateInternal(**subcategory_internal_dict)
    created_subcategory = await crud_sub_category.create(db=db, object=subcategory_internal)

    subcategory_read = await crud_sub_category.get(db=db, id=created_subcategory.id, schema_to_select=SubCategoryRead)
    if subcategory_read is None:
        raise NotFoundException("Created SubCategory not found")

    return cast(SubCategoryRead, subcategory_read)


@router.get("/subcategories", response_model=PaginatedListResponse[SubCategoryRead])
async def read_subcategory(
    request: Request, db: Annotated[AsyncSession, Depends(async_get_db)], page: int = 1, items_per_page: int = 10
) -> dict:
    subcategory_data = await crud_sub_category.get_multi(db=db, offset=compute_offset(page, items_per_page), limit=items_per_page)

    response: dict[str, Any] = paginated_response(crud_data=subcategory_data, page=page, items_per_page=items_per_page)
    return response


@router.get("/subcategory/{name}", response_model=SubCategoryRead)
async def read_subcategory(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> SubCategoryRead:
    db_subcateogry = await crud_sub_category.get(db=db, name=name, schema_to_select=SubCategoryRead)
    if db_subcateogry is None:
        raise NotFoundException("SubCategory not found")

    return cast(SubCategoryRead, db_subcateogry)


@router.patch("/subcategory/{name}", dependencies=[Depends(get_current_superuser)])
async def patch_subcategory(
    request: Request, name: str, values: SubCategoryUpdate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> dict[str, str]:
    db_subcategory = await crud_sub_category.get(db=db, name=name, schema_to_select=SubCategoryRead)
    db_category = await crud_sub_category.get(db=db, name=name, schema_to_select=SubCategoryRead)
    if db_category is None:
        raise NotFoundException("SubCategory not found")

    await crud_sub_category.update(db=db, object=values, name=name)
    return {"message": "SubCategory updated"}


@router.delete("/subcategory/{name}", dependencies=[Depends(get_current_superuser)])
async def erase_subcategory(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> dict[str, str]:
    db_subcategory = await crud_sub_category.get(db=db, name=name, schema_to_select=SubCategoryRead)
    if db_subcategory is None:
        raise NotFoundException("SubCategory not found")

    await crud_sub_category.delete(db=db, name=name)
    return {"message": "Category deleted"}
