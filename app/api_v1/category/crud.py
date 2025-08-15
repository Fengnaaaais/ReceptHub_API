from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Category
from .schemas import CategoryCreate


async def get_categories(session: AsyncSession):
    stmt = select(Category).order_by(Category.id)
    result: Result = await session.execute(stmt)
    categories = result.scalars().all()

    return list(categories)


async def create_category(
    session: AsyncSession,
    category_in: CategoryCreate,
):
    category = Category(**category_in.model_dump())

    session.add(category)
    await session.commit()

    return category
