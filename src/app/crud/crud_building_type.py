from fastcrud import FastCRUD

from ..models.building_type import BuildingType
from ..schemas.building_type import BuildingTypeCreateInternal, BuildingTypeDelete, BuildingTypeRead, BuildingTypeUpdate, BuildingTypeUpdateInternal

CRUDBuildingType = FastCRUD[BuildingType, BuildingTypeCreateInternal, BuildingTypeUpdate, BuildingTypeUpdateInternal, BuildingTypeDelete, BuildingTypeRead]
crud_building_type = CRUDBuildingType(BuildingType)
