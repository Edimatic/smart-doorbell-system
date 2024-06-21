from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/create", response_model=schemas.Doorbell)
def create_doorbell(doorbell: schemas.DoorbellCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_doorbell(db, doorbell, user_id)

