from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

from finice.users.exceptions import UserAlreadyExists, UserDoesNotExist
from finice.users.models import User


class UserHandler:
    def __init__(
        self, session: "Session", email: str, name: Optional[str] = None
    ) -> None:
        """
        Handle common operations for a user

        Args:
            session (Session): sqlalchemy Session object
            email (str): email for the user
            name (Optional[str]): name for the user
        """
        self.session = session
        self.name = name
        self.email = email

    def get(self) -> User:
        """
        Get a user from its email

        Returns:
            User object

        Raises:
            UserDoesNotExist: if the user is not found
        """
        user = self.session.query(User).filter_by(email=self.email).first()
        if not user:
            raise UserDoesNotExist(self.email)
        return user

    def create(self, password: str) -> User:
        """
        Create a new user

        Args:
            password (str): password to attach to the user

        Returns:
            User object
        """
        try:
            self.get(self.email)
        except UserDoesNotExist:
            pass
        else:
            raise UserAlreadyExists(self.email)

        new_user = User(email=self.email, password=password)
        new_user.hash_password()
        self.session.add(new_user)
        self.session.commit()

        return new_user

    def reset_password(self, password: str) -> User:
        """
        Reset the password on the user

        Args:
            password (str): password to attach to the user

        Returns:
            User object
        """
        user = self.get()
        user.password = password
        user.hash_password()
        self.session.commit()

        return user
