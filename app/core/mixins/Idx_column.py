from sqlalchemy.orm import Mapped, mapped_column


class Idx_Mixin:
    id: Mapped[int] = mapped_column(primary_key=True)
