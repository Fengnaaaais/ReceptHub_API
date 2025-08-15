from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)

from core.config import settings


class DBHelper:
    def __init__(
        self,
        url: str,
        echo: bool,
    ):
        self.engine = create_async_engine(
            url=settings.db.url,
            echo=settings.db.echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self):
        async with self.session_factory() as session:
            yield session

            await session.close()


db_helper = DBHelper(
    settings.db.url,
    settings.db.echo,
)
