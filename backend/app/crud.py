from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username, 
        email=user.email, 
        password=user.password, 
        created_at=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_doorbell(db: Session, doorbell: schemas.DoorbellCreate, user_id: int):
    db_doorbell = models.Doorbell(
        **doorbell.dict(), 
        user_id=user_id, 
        created_at=datetime.utcnow()
    )
    db.add(db_doorbell)
    db.commit()
    db.refresh(db_doorbell)
    return db_doorbell

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

