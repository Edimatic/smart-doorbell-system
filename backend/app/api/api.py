from fastapi import APIRouter
from .endpoints import auth, doorbell, events, notifications

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(doorbell.router, prefix="/doorbell", tags=["doorbell"])
api_router.include_router(events.router, prefix="/events", tags=["events"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["notifications"])

