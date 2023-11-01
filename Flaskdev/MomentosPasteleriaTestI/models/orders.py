from config.dbconfig import db
from typing import Optional, List
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid
import datetime



class Orders(db.Model):

    pass
