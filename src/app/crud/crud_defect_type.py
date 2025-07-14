from fastcrud import FastCRUD

from ..models.defect_type import DefectType
from ..schemas.defect_type import DefectTypeCreateInternal,DefectTypeCreate, DefectTypeUpdate, DefectTypeUpdateInternal, DefectTypeDelete

CRUDDefectType = FastCRUD[DefectType, DefectTypeCreate, DefectTypeUpdate, DefectTypeUpdateInternal, DefectTypeDelete,DefectTypeCreateInternal]
crud_defect_type = CRUDDefectType(DefectType)