from typing import Sequence

import uvicorn
from fastapi import APIRouter, FastAPI

from planner_back.routes import event_router


def create_app(routers: Sequence[APIRouter], host=1):
    app = FastAPI()
    for router in routers:
        app.include_router(router=router)
    return app


if __name__ == "__main__":
    routers = [event_router]
    app = create_app(routers=routers)
    uvicorn.run(app, host="0.0.0.0", port=8000)
    raise SystemExit(0)
