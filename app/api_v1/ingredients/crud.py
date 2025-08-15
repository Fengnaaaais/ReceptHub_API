from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)

from core.models import Recipe, Ingredient
from .schemas import IngredientCreate


async def get_ingredients(session: AsyncSession) -> list[Ingredient]:
    stmt = select(Ingredient).order_by(Ingredient.id)
    result: Result = await session.execute(stmt)
    ingredients = result.scalars().all()

    return list(ingredients)


async def get_ingredients_with_recipe(
    session: AsyncSession, recipe_id: int
) -> Recipe | None:
    stmt = (
        select(Recipe)
        .options(selectinload(Recipe.ingredients))
        .where(Recipe.id == recipe_id)
    )
    result: Result = await session.execue(stmt)
    return result.scalar_one_or_none()


async def create_ingredient(
    session: AsyncSession,
    ingredient_in: IngredientCreate,
) -> Ingredient:
    ingredient = Ingredient(**ingredient_in.model_dump())
    session.add(ingredient)
    await session.commit()
    # await session.refresh()
    return ingredient


async def get_ingredients_by_ids(
    session: AsyncSession, ingredient_ids: list[int]
) -> list[Ingredient]:
    result = await session.execute(
        select(Ingredient).where(Ingredient.id.in_(ingredient_ids))
    )
    return result.scalars().all()
