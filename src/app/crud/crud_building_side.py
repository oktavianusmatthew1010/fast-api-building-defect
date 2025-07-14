from fastcrud import FastCRUD

from ..models.building_side import BuildingSide
from ..schemas.building_side import BuildingSideCreateInternal, BuildingSideDelete, BuildingSideRead, BuildingSideUpdate, BuildingSideUpdateInternal

CRUDBuildingSide = FastCRUD[BuildingSide, BuildingSideCreateInternal, BuildingSideUpdate, BuildingSideUpdateInternal, BuildingSideDelete, BuildingSideRead]
crud_building_side = CRUDBuildingSide(BuildingSide)
