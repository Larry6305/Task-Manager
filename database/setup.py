from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

engine = create_engine("sqlite:///taskmanager.db")
SessionLocal = sissionmaker(bind=engine)

def init_db():
     import models.user
     import models.project
     import models.task
     import models.category
     Base.metadata.create_all(bind=engine)