from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/settings")
def update_notification_settings(notification_settings: schemas.NotificationSettings, db: Session = Depends(get_db)):
    # Logic to update notification settings
    return {"message": "Notification settings updated"}

