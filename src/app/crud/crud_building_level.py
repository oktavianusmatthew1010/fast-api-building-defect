from fastcrud import FastCRUD

from ..models.building_level import BuildingLevel
from ..schemas.building_level import BuildingLevelCreateInternal, BuildingLevelDelete, BuildingLevelRead, BuildingLevelUpdate, BuildingLevelUpdateInternal

CRUDBuildingLevel = FastCRUD[BuildingLevel, BuildingLevelCreateInternal, BuildingLevelUpdate, BuildingLevelUpdateInternal, BuildingLevelDelete, BuildingLevelRead]
crud_building_level = CRUDBuildingLevel(BuildingLevel)
