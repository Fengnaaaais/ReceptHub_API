from typing import TYPE_CHECKING

from fastapi_users.db import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)
from sqlalchemy.orm import Mapped, relationship

from .base import Base
from core.types import UserIdType
from core.mixins.Idx_column import Idx_Mixin


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from .recipe import Recipe


class User(Base, Idx_Mixin, SQLAlchemyBaseUserTable[UserIdType]):

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)

    recipes: Mapped[list["Recipe"]] = relationship(
        "Recipe",
        back_populates="author",
    )
