from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from .recipes.views import router as recipe_router
from .ingredients.views import router as ingredient_router
from .category.views import router as category_router
from .users.auth import router as auth_router
from .users.users import router as users_router

from core.config import settings


http_bearer = HTTPBearer(auto_error=False)

router: APIRouter = APIRouter(
    dependencies=[Depends(http_bearer)],
)

router.include_router(
    router=recipe_router,
    prefix="/recipes",
    tags=["Recipes"],
)
router.include_router(
    router=ingredient_router,
    prefix="/ingredients",
    tags=["Ingredients"],
)
router.include_router(
    router=category_router,
    prefix="/categories",
    tags=["Categories"],
)
router.include_router(
    router=auth_router,
    prefix=settings.api_prefix.v1.auth,
    tags=["Auth"],
)
router.include_router(
    router=users_router,
    prefix=settings.api_prefix.v1.users,
    tags=["Users"],
)
