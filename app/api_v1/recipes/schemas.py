from typing import Annotated
from annotated_types import MaxLen, Gt
from pydantic import BaseModel, ConfigDict, Field


class RecipeBase(BaseModel):
    name: Annotated[str, MaxLen(150)]
    description: str
    image: str
    prep_time: Annotated[int, Gt(1)]
    category_id: int
    is_published: bool = False


class Recipe(RecipeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class RecipeCreate(RecipeBase):
    ingredient_ids: list[int] = Field(default_factory=list)
