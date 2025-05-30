from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column (String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    projects = relationship("Project", back_populates="user")