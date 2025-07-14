from fastcrud import FastCRUD

from ..models.category import Category
from ..schemas.category import CategoryCreateInternal,CategoryCreate, CategoryUpdate, CategoryUpdateInternal, CategoryDelete

CRUDCategory = FastCRUD[Category, CategoryCreate, CategoryUpdate, CategoryUpdateInternal, CategoryDelete,CategoryCreateInternal]
crud_category = CRUDCategory(Category)