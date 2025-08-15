from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import Ingredient, IngredientCreate


router = APIRouter()


@router.get("/", response_model=list[Ingredient])
async def get_ingredients(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> list[Ingredient]:
    return await crud.get_ingredients(session=session)


@router.post("/create/", response_model=Ingredient)
async def create_ingredient(
    ingredient: IngredientCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Ingredient:
    return await crud.create_ingredient(
        session=session,
        ingredient_in=ingredient,
    )
