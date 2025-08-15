from typing import TYPE_CHECKING
from .base import Base

from sqlalchemy.orm import Mapped, relationship

from .recipe_ingredient_association import recipe_ingredient_association_table
from core.mixins.Idx_column import Idx_Mixin


if TYPE_CHECKING:
    from .recipe import Recipe


class Ingredient(Base, Idx_Mixin):
    name: Mapped[str]

    recipes: Mapped[list["Recipe"]] = relationship(
        "Recipe",
        secondary=recipe_ingredient_association_table,
        back_populates="ingredients",
    )
