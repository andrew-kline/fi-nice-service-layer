from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from finice.models import BaseModel


class Account(BaseModel):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    vendor = Column(String(120))
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")
