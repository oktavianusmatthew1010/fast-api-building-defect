from fastapi import APIRouter

from .login import router as login_router
from .logout import router as logout_router
from .posts import router as posts_router
from .rate_limits import router as rate_limits_router
from .tasks import router as tasks_router
from .tiers import router as tiers_router
from .users import router as users_router
from .project import router as projects_router
from .building import router as buildings_router
from .category import router as category_router
from .sub_category import router as subcategory_router
from .building_level import router as building_level_router
from .building_type import router as building_type_router
from .building_side import router as building_side_router
from .defect_type import router as defect_type_router
from .defect import router as defect_router

router = APIRouter(prefix="/v1")
router.include_router(login_router)
router.include_router(logout_router)
router.include_router(users_router)
router.include_router(posts_router)
router.include_router(tasks_router)
router.include_router(tiers_router)
router.include_router(rate_limits_router)
router.include_router(projects_router)
router.include_router(buildings_router)
router.include_router(category_router)
router.include_router(subcategory_router)
router.include_router(building_level_router)
router.include_router(building_type_router)
router.include_router(building_side_router)
router.include_router(defect_type_router)
router.include_router(defect_router)
