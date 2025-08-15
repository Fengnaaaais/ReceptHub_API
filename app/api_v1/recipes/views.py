from typing import TYPE_CHECKING
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, status, Depends

from api_v1.dependencies.authentication.fastapi_users import fastapi_users

from . import crud
from .schemas import Recipe, RecipeCreate
from core.models import db_helper


if TYPE_CHECKING:
    from core.models import User

router = APIRouter()


@router.get("/", response_model=list[Recipe])
async def get_recipes(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.get_recipes(session=session)


@router.get("/{recipe_id}/", response_model=Recipe)
async def get_recipes(
    recipe_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    recipe = await crud.get_recipes(session=session, recipe_id=recipe_id)
    if recipe is not None:
        return recipe

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Recipe {recipe_id} not found",
    )


@router.post("/", response_model=Recipe)
async def create_recipe(
    recipe_in: RecipeCreate,
    user: "User" = Depends(fastapi_users.current_user(active=True)),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    try:
        recipe = await crud.create_recipe(
            session=session,
            recipe_in=recipe_in,
            user=user,
        )
        return recipe
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
