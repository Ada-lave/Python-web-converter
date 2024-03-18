from abc import ABC, abstractmethod

from sqlalchemy import insert, select
from db.db import db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict):

        session = db.get_current_session()
        async with session() as sess:
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await sess.execute(stmt)
            await sess.commit()

        return res.all()

    async def find_all(self):
        session = db.get_current_session()
        async with session() as sess:
            stmt = select(self.model)
            res = await sess.scalars(stmt)

            return list(res)
