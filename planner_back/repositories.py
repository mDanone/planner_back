from abc import ABC
from typing import Generic, TypeVar

from aiopg.sa import SAConnection
from aiopg.sa.result import RowProxy
from pydantic import BaseModel
from sqlalchemy import Table

from planner_back.errors import NotFound
from planner_back.tables import event
from planner_back.types import GetEvent

MT = TypeVar("MT", bound=BaseModel)


class BaseRepository(ABC, Generic[MT]):
    def __init__(self, conn: SAConnection):
        self._conn = conn

    @property
    def model_cls(self) -> MT:
        return NotImplemented

    @property
    def table(self) -> Table:
        return NotImplemented

    async def execute(self, query):
        return await self._conn.execute(query)

    async def create(self, model: BaseModel) -> int:
        result_proxy = await self.execute(
            self.table.insert(
                model.dict(exclude_none=True, exclude_unset=True)
            ).returning(self.table.c.id)
        )
        return (await result_proxy.fetchone())[0]

    async def get_all(self) -> list[MT]:
        result_proxy = await self.execute(self.table.select())
        row_proxies = await result_proxy.fetchall()
        return [self.model_cls.from_orm(row) for row in row_proxies]

    async def _get_one(self, query) -> MT:
        result_proxy = await self.execute(query)
        row = await result_proxy.fetchone()
        if not row:
            raise NotFound()
        return self.model_cls.from_orm(row)

    async def get_one(self, id: int) -> MT:
        query = self.table.select().where(self.table.c.id == id)
        return await self._get_one(query)


class EventRepository(BaseRepository):
    @property
    def table(self) -> Table:
        return event

    @property
    def model_cls(self) -> type[GetEvent]:
        return GetEvent
