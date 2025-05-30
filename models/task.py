from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from models.base import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    due_date = Column(Date)
    status = Column(String, default="Pending")
    project_id = Column(Integer, ForeignKey("projects.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

project = relationship("Project", back_populates="tasks")
category = relationship("Category", back_populates="tasks")
