from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

# Configuration of ORM DB models 
class Base(DeclarativeBase, MappedAsDataclass):
  pass
