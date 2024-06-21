from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class DoorbellBase(BaseModel):
    location: str

class DoorbellCreate(DoorbellBase):
    pass

class Doorbell(DoorbellBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class EventBase(BaseModel):
    event_type: str
    event_time: datetime
    media_url: str

class EventCreate(EventBase):
    doorbell_id: int

class Event(EventBase):
    id: int
    doorbell_id: int

    class Config:
        orm_mode = True

