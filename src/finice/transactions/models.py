from sqlalchemy import Date, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from finice.models import BaseModel


class Transaction(BaseModel):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    amount = Column(Float)
    vendor = Column(String(120))
    category_account = Column(String(120))
    category_user = Column(String(120))
    description = Column(String(120))
    type = Column(String(50))
    account_id = Column(Integer, ForeignKey("accounts.id"))
    account = relationship("Account", back_populates="transactions")
