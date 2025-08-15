from typing import TYPE_CHECKING
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Recipe
from .schemas import RecipeCreate
from ..ingredients.crud import get_ingredients_by_ids


if TYPE_CHECKING:
    from core.models import User


async def get_recipes(session: AsyncSession) -> list[Recipe]:
    stmt = select(Recipe).order_by(Recipe.id)
    result: Result = await session.execute(stmt)
    recipes = result.scalars().all()

    return list(recipes)


async def get_recipe(session: AsyncSession, recipe_id: int) -> Recipe | None:
    return await session.get(Recipe, recipe_id)


from fastapi import HTTPException, status


async def create_recipe(
    session: AsyncSession,
    recipe_in: RecipeCreate,
    user: "User",
) -> Recipe:
    recipe = Recipe(
        name=recipe_in.name,
        description=recipe_in.description,
        image=recipe_in.image,
        prep_time=recipe_in.prep_time,
        category_id=recipe_in.category_id,
        is_published=recipe_in.is_published,
        author_id=user.id,
    )

    if recipe_in.ingredient_ids:
        ingredients = await get_ingredients_by_ids(session, recipe_in.ingredient_ids)

        if len(ingredients) != len(recipe_in.ingredient_ids):
            found_ids = {ing.id for ing in ingredients}
            missing_ids = set(recipe_in.ingredient_ids) - found_ids
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Ingredients not found: {missing_ids}",
            )

        recipe.ingredients = ingredients

    session.add(recipe)
    await session.commit()
    await session.refresh(recipe)

    return recipe
