from fastapi import APIRouter

from ..dependencies.authentication.fastapi_users import fastapi_users

from core.schemas.user import UserUpdate, UserRead


router = APIRouter()

# /me
# /{id}
router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
