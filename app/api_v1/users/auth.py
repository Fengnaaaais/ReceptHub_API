from fastapi import APIRouter

from api_v1.dependencies.authentication.fastapi_users import fastapi_users

from api_v1.dependencies.authentication.backend import authentication_backend
from core.schemas.user import UserCreate, UserRead


router = APIRouter()


# /login
# /logout
router.include_router(
    fastapi_users.get_auth_router(authentication_backend),
)

# /register
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)

router.include_router(
    fastapi_users.get_verify_router(UserRead),
)

router.include_router(
    fastapi_users.get_reset_password_router(),
)
