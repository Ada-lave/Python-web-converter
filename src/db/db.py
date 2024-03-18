from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_scoped_session,
    async_sessionmaker,
    AsyncSession,
)

from asyncio import current_task


class DataBase:
    def __init__(self) -> None:
        self.engine = create_async_engine(url="sqlite+aiosqlite:///db.sqlite3")
        self.session_factory = async_sessionmaker(
            bind=self.engine, autoflush=False, expire_on_commit=False, autocommit=False
        )

    def get_current_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory, scopefunc=current_task
        )
        return session

    async def session_depends(self):
        session = self.get_current_session()
        async with session() as sess:
            yield sess
            await session.remove()


db = DataBase()
