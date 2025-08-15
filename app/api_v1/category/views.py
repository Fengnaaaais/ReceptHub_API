from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from core.models import db_helper
from .schemas import Category, CategoryCreate
from . import crud


router = APIRouter()


@router.get("/", response_model=list[Category])
async def get_categories(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> list[Category]:
    return await crud.get_categories(session)


@router.post("/create/", response_model=CategoryCreate)
async def create_category(
    category: CategoryCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_category(
        session,
        category,
    )
