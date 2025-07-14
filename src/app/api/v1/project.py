from typing import Annotated, Any, cast

from fastapi import APIRouter, Depends, Request
from fastcrud.paginated import PaginatedListResponse, compute_offset, paginated_response
from sqlalchemy.ext.asyncio import AsyncSession

from ...api.dependencies import get_current_superuser,get_current_user
from ...core.db.database import async_get_db
from ...core.exceptions.http_exceptions import DuplicateValueException, NotFoundException
from ...crud.crud_project import crud_project
from ...crud.crud_users import crud_users
from ...schemas.project import ProjectCreate, ProjectCreateInternal, ProjectRead, ProjectUpdate
from ...schemas.user import UserRead

router = APIRouter(tags=["projects"])


@router.post("/project2", response_model=ProjectRead, status_code=201)
async def write_post(
    request: Request,
    post: ProjectCreate,
    current_user: Annotated[dict, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> ProjectRead:
    db_user = await crud_users.get(db=db, id=current_user["id"], is_deleted=False, schema_to_select=UserRead)
    if db_user is None:
        raise NotFoundException("User not found")

    # If db_user is a dict, use db_user["id"]; if it's a Pydantic model, use db_user.id
    user_id = db_user["id"] if isinstance(db_user, dict) else db_user.id

    project_internal_dict = post.model_dump()
    project_internal_dict["created_by"] = user_id

    project_internal = ProjectCreateInternal(**project_internal_dict)
    created_project = await crud_project.create(db=db, object=project_internal)

    project_read = await crud_project.get(db=db, id=created_project.id, schema_to_select=ProjectRead)
    if project_read is None:
        raise NotFoundException("Created Project not found")

    return cast(ProjectRead, project_read)

@router.post("/project", dependencies=[Depends(get_current_superuser)], status_code=201)
async def write_project(    
    request: Request, project: ProjectCreate,current_user: Annotated[dict, Depends(get_current_user)], db: Annotated[AsyncSession, Depends(async_get_db)]
) -> ProjectRead:
    db_user = await crud_users.get(db=db, id=current_user["id"], is_deleted=False, schema_to_select=UserRead)
    
    project_internal_dict = project.model_dump()
    
    db_project = await crud_project.exists(db=db, name=project_internal_dict["name"])

    if db_project:
        raise DuplicateValueException("Project Name not available")
    user_id = db_user["id"] if isinstance(db_user, dict) else db_user["id"]
    project_internal_dict["created_by"] = user_id
    project_internal = ProjectCreateInternal(**project_internal_dict)
    created_project = await crud_project.create(db=db, object=project_internal)

    project_read = await crud_project.get(db=db, id=created_project.id, schema_to_select=ProjectRead)
    if project_read is None:
        raise NotFoundException("Created Project not found")

    return cast(ProjectRead, project_read)


@router.get("/projects", response_model=PaginatedListResponse[ProjectRead])
async def read_projects(
    request: Request, db: Annotated[AsyncSession, Depends(async_get_db)], page: int = 1, items_per_page: int = 10
) -> dict:
    projects_data = await crud_project.get_multi(db=db, offset=compute_offset(page, items_per_page), limit=items_per_page)

    response: dict[str, Any] = paginated_response(crud_data=projects_data, page=page, items_per_page=items_per_page)
    return response


@router.get("/project/{name}", response_model=ProjectRead)
async def read_project(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> ProjectRead:
    db_project = await crud_project.get(db=db, name=name, schema_to_select=ProjectRead)
    if db_project is None:
        raise NotFoundException("Project not found")

    return cast(ProjectRead, db_project)


@router.patch("/project/{name}", dependencies=[Depends(get_current_superuser)])
async def patch_project(
    request: Request, name: str, values: ProjectUpdate, db: Annotated[AsyncSession, Depends(async_get_db)]
) -> dict[str, str]:
    db_project = await crud_project.get(db=db, name=name, schema_to_select=ProjectRead)
    if db_project is None:
        raise NotFoundException("Building not found")

    await crud_project.update(db=db, object=values, name=name)
    return {"message": "Project updated"}


@router.delete("/project/{name}", dependencies=[Depends(get_current_superuser)])
async def erase_project(request: Request, name: str, db: Annotated[AsyncSession, Depends(async_get_db)]) -> dict[str, str]:
    db_project = await crud_project.get(db=db, name=name, schema_to_select=ProjectRead)
    if db_project is None:
        raise NotFoundException("Project not found")

    await crud_project.delete(db=db, name=name)
    return {"message": "Project deleted"}
