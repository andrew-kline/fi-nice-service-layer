from sqlalchemy import Column, Integer, String

from finice.db import Base


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    name = Column(String)
