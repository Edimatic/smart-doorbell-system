from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime)

    doorbells = relationship("Doorbell", back_populates="owner")

class Doorbell(Base):
    __tablename__ = "doorbells"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    location = Column(String)
    created_at = Column(DateTime)

    owner = relationship("User", back_populates="doorbells")
    events = relationship("Event", back_populates="doorbell")

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    doorbell_id = Column(Integer, ForeignKey("doorbells.id"))
    event_type = Column(String)
    event_time = Column(DateTime)
    media_url = Column(String)

    doorbell = relationship("Doorbell", back_populates="events")

