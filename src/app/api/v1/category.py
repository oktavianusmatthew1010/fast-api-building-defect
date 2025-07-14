from typing import Annotated, Any, cast

from fastapi import APIRouter, Depends, Request
from fastcrud.paginated import PaginatedListResponse, compute_offset, paginated_response
from sqlalchemy.ext.asyncio import AsyncSession

from ...api.dependencies import get_current_superuser
from ...core.db.database import async_get_db
from ...core.exceptions.http_exceptions import DuplicateValueException, NotFoundException
from ...crud.crud_category import crud_category
from ...schemas.category import CategoryCreate, CategoryCreateInternal, CategoryRead, CategoryUpdate

router = APIRouter(tags=["category"])


@router.post("/category", dependencies=[Depends(get_current_superuser)], status_code=201)
async def write_tier(
    request: Request, category: CategoryCreate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> CategoryRead:
    category_internal_dict = category.model_dump()
    db_category = await crud_category.exists(db=db, name=category_internal_dict["name"])
    if db_category:
        raise DuplicateValueException("Category Name not available")

    category_internal = CategoryCreateInternal(**category_internal_dict)
    created_category = await crud_category.create(db=db, object=category_internal)

    category_read = await crud_category.get(db=db, id=created_category.id, schema_to_select=CategoryRead)
    if category_read is None:
        raise NotFoundException("Created Category not found")

    return cast(CategoryRead, category_read)


@router.get("/categories", response_model=PaginatedListResponse[CategoryRead])
async def read_category(
    request: Request, db: Annotated[AsyncSession, Depends(async_get_db)], page: int = 1, items_per_page: int = 10
) -> dict:
    category_data = await crud_category.get_multi(db=db, offset=compute_offset(page, items_per_page), limit=items_per_page)

    response: dict[str, Any] = paginated_response(crud_data=category_data, page=page, items_per_page=items_per_page)
    return response


@router.get("/category/{name}", response_model=CategoryRead)
async def read_category(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> CategoryRead:
    db_cateogry = await crud_category.get(db=db, name=name, schema_to_select=CategoryRead)
    if db_cateogry is None:
        raise NotFoundException("Category not found")

    return cast(CategoryRead, db_cateogry)


@router.patch("/category/{name}", dependencies=[Depends(get_current_superuser)])
async def patch_category(
    request: Request, name: str, values: CategoryUpdate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> dict[str, str]:
    db_category = await crud_category.get(db=db, name=name, schema_to_select=CategoryRead)
    if db_category is None:
        raise NotFoundException("Category not found")

    await crud_category.update(db=db, object=values, name=name)
    return {"message": "Category updated"}


@router.delete("/category/{name}", dependencies=[Depends(get_current_superuser)])
async def erase_category(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> dict[str, str]:
    db_category = await crud_category.get(db=db, name=name, schema_to_select=CategoryRead)
    if db_category is None:
        raise NotFoundException("Category not found")

    await crud_category.delete(db=db, name=name)
    return {"message": "Category deleted"}
