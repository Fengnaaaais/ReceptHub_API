from typing import TYPE_CHECKING

from sqlalchemy import String, event
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.mixins.slug import SlugMixin

from .base import Base
from ..slugify import slugify
from core.mixins.Idx_column import Idx_Mixin

if TYPE_CHECKING:
    from .recipe import Recipe


class Category(Base, Idx_Mixin, SlugMixin):
    name: Mapped[str]
    image: Mapped[str]

    recipes: Mapped[list["Recipe"]] = relationship(
        "Recipe",
        back_populates="category",
    )
