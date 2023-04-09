from typing import AsyncGenerator

from aiopg.sa import Engine, SAConnection, create_engine
from fastapi import Depends

from planner_back.repositories import EventRepository
from planner_back.settings import Settings


async def get_settings() -> Settings:
    return Settings()  # type: ignore


async def get_engine(settings: Settings = Depends(get_settings)) -> AsyncGenerator:
    async with create_engine(settings.postgres_dsn) as engine:
        yield engine


async def get_connection(engine: Engine = Depends(get_engine)) -> AsyncGenerator:
    async with engine.acquire() as conn:
        async with conn.begin():
            yield conn


async def get_event_repository(
    connection: SAConnection = Depends(get_connection),
) -> EventRepository:
    return EventRepository(conn=connection)
