from sqlalchemy import Table, Column, ForeignKey, Integer, UniqueConstraint

from .base import Base

recipe_ingredient_association_table = Table(
    "recipe_ingredient_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("recipe_id", ForeignKey("recipe.id"), nullable=False),
    Column("ingredient_id", ForeignKey("ingredient.id"), nullable=False),
    UniqueConstraint("recipe_id", "ingredient_id", name="idx_unique_recipe_ingredient"),
)
