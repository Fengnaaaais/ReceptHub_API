from sqlalchemy import event, String
from sqlalchemy.orm import Mapped, mapped_column

from ..slugify import slugify


class SlugMixin:
    slug: Mapped[str] = mapped_column(String(255), unique=True, index=True)

    @classmethod
    def __declare_last__(cls):
        event.listen(cls, "before_insert", cls._generate_slug)
        event.listen(cls, "before_update", cls._generate_slug)

    @staticmethod
    def _generate_slug(mapper, connection, target):
        if (
            hasattr(target, "name")
            and target.name
            and (not target.slug or slugify(target.name) != target.slug)
        ):
            target.slug = slugify(target.name)
