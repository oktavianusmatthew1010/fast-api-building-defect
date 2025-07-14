from fastcrud import FastCRUD

from ..models.subcategory import SubCategory
from ..schemas.subcategory import SubCategoryCreateInternal,SubCategoryCreate, SubCategoryUpdate, SubCategoryUpdateInternal, SubCategoryDelete

CRUDCSubategory = FastCRUD[SubCategory, SubCategoryCreate, SubCategoryUpdate, SubCategoryUpdateInternal, SubCategoryDelete,SubCategoryCreateInternal]
crud_sub_category = CRUDCSubategory(SubCategory)