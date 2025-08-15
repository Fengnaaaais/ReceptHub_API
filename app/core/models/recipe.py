from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, DateTime, func, event
from sqlalchemy.orm import Mapped, relationship, mapped_column

from core.mixins.slug import SlugMixin

from .base import Base
from .recipe_ingredient_association import recipe_ingredient_association_table
from core.mixins.Idx_column import Idx_Mixin


if TYPE_CHECKING:
    from .ingredient import Ingredient
    from .user import User
    from .category import Category


class Recipe(Base, Idx_Mixin, SlugMixin):
    name: Mapped[str]
    description: Mapped[str]
    image: Mapped[str]

    ingredients: Mapped[list["Ingredient"]] = relationship(
        "Ingredient",
        secondary=recipe_ingredient_association_table,
        back_populates="recipes",
    )

    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship(
        "User",
        back_populates="recipes",
    )

    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="recipes",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    prep_time: Mapped[int]
    is_published: Mapped[bool] = mapped_column(default=False)
