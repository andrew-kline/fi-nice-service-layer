import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from finice.models import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    password = Column(String(500), nullable=False)
    name = Column(String(500), nullable=False, unique=True)
    email = Column(String(120), nullable=False, unique=True)
    created = Column(DateTime, default=datetime.datetime.utcnow, nullable=True)
    accounts = relationship("Account", back_populates="user")

    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")

    def __repr__(self):
        """
        The __repr__ function is used to return a string representation of the object

        Returns:
            The username of the user.
        """
        return "<User {}>".format(self.username)

    def hash_password(self):
        """
        It takes the password that the user has entered, hashes it, and then stores the hashed password in
        the database
        """
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password: str) -> bool:
        """
        It takes a plaintext password, hashes it, and compares it to the hashed password in the database

        Args:
            password (str): The password to be hashed and checked

        Returns:
            bool if password is valid
        """
        return check_password_hash(self.password, password)
