#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String


class User(BaseModel, Base):
    """Represents a user for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table users.

    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
