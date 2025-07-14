from fastcrud import FastCRUD

from ..models.building import Building
from ..schemas.building import BuildingCreateInternal, BuildingDelete, BuildingRead, BuildingUpdate, BuildingUpdateInternal

CRUDBuilding = FastCRUD[Building, BuildingCreateInternal, BuildingUpdate, BuildingUpdateInternal, BuildingDelete, BuildingRead]
crud_building = CRUDBuilding(Building)
