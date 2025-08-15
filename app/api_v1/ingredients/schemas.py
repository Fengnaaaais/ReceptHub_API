from typing import Annotated
from annotated_types import MaxLen

from pydantic import BaseModel, ConfigDict


class IngredientBase(BaseModel):
    name: Annotated[
        str,
        MaxLen(150),
    ]


class IngredientCreate(IngredientBase):
    pass


class Ingredient(IngredientBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
