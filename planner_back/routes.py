from fastapi import APIRouter, Depends
from pydantic import PositiveInt

from planner_back.dependencies import get_event_repository
from planner_back.repositories import EventRepository
from planner_back.types import CreateEvent, GetEvent

event_router = APIRouter(prefix="/events")


@event_router.get("/", response_model=list[GetEvent])
async def get_events(
    event_repository: EventRepository = Depends(get_event_repository),
) -> list[GetEvent]:
    return await event_repository.get_all()


@event_router.post("/")
async def create_event(
    event_model: CreateEvent,
    event_repository: EventRepository = Depends(get_event_repository),
):
    event_id = await event_repository.create(event_model)
    return {"created_event": event_router.url_path_for("get_event", event_id=event_id)}


@event_router.get("/{event_id}/", response_model=GetEvent)
async def get_event(
    event_id: PositiveInt,
    event_repository: EventRepository = Depends(get_event_repository),
) -> GetEvent:
    return await event_repository.get_one(id=event_id)
