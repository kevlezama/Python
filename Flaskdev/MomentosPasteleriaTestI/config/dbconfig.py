from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


# Configuration of ORM DB models 

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
