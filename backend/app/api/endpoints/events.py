from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/create", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db, event)

