from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return db_user

@router.post("/login")
def login_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user and db_user.password == user.password:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")

