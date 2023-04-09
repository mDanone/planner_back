# from abc import ABC
# from typing import Generic, TypeVar

# from fastapi import APIRouter
# from starlette.routing import Router
# from pydantic import BaseModel

# from planner_back.repositories import BaseRepository, EventRepository

# RT = TypeVar("RT", bound=Router)
# RepoT = TypeVar("RepoT", bound=BaseRepository)


# class BaseService(ABC, Generic[RT, RepoT]):
#     def __init__(self, router: RT, repository: BaseRepository):
#         self._router = router
#         self._repo = repository

#     async def create(self, model: BaseModel):
#         data = model.dict(exclude_none=True, exclude_unset=True)
#         event_id = await self._repo.create(data)
#         return {
#             "entity_path": self._router
#         }


# class EventService(BaseService[APIRouter, EventRepository]):
#     pass
