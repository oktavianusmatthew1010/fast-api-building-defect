from fastcrud import FastCRUD

from ..models.defect import Defect
from ..schemas.defect import DefectCreateInternal,DefectCreate, DefectUpdate, DefectUpdateInternal, DefectDelete

CRUDDefect = FastCRUD[Defect, DefectCreate, DefectUpdate, DefectUpdateInternal, DefectDelete,DefectCreateInternal]
crud_defect = CRUDDefect(Defect)