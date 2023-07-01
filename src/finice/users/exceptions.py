import logging

logger = logging.getLogger(__name__)


class UserError(Exception):
    """
    Exception raised for errors with a user.

    Args:
        user_email (str): email of the user
        message (str): explanation of the error
    """

    def __init__(
        self, user_email: str, event_id: int = 100, message: str = "Generic UserError"
    ):
        self.user_email = user_email
        self.message = message
        self.event_id = event_id
        super().__init__(self.message)
        logger.info(message, extra={"user": user_email, "event_id": event_id})


class LoginError(UserError):
    """
    Exception raised during the login process

    Args:
        user_email (str): email of the user
    """

    def __init__(
        self, user_email: str, event_id: int = 110, message: str = "Login error"
    ):
        self.user_email = user_email
        self.message = message
        self.event_id = event_id
        super().__init__(self.user_email, self.event_id, self.message)


class UserDoesNotExist(LoginError):
    """
    Exception raised when a user does not exist

    Args:
        user_email (str): email of the user
    """

    def __init__(self, user_email: str):
        self.user_email = user_email
        self.message = "Login error (user does not exist)"
        self.event_id = 120
        super().__init__(self.user_email, self.event_id, self.message)


class IncorrectPassword(LoginError):
    """
    Exception raised when a user's password is incorrect

    Args:
        user_email (str): email of the user
    """

    def __init__(self, user_email: str):
        self.user_email = user_email
        self.message = "Login error (incorrect password)"
        self.event_id = 130
        super().__init__(self.user_email, self.event_id, self.message)


class CreateUserError(UserError):
    """
    Exception raised during the user creation process

    Args:
        user_email (str): email of the user
    """

    def __init__(self, user_email: str, message: str = "User creation error"):
        self.user_email = user_email
        self.message = message
        self.event_id = 140
        super().__init__(self.user_email, self.event_id, self.message)


class UserAlreadyExists(UserError):
    """
    Exception raised when a user is attempted to be made but it already exists

    Args:
        user_email (str): email of the user
    """

    def __init__(self, user_email: str):
        self.user_email = user_email
        self.message = "Login error (incorrect password)"
        self.event_id = 150
        super().__init__(self.user_email, self.event_id, self.message)
