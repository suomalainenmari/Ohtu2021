from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        username_is_taken = self._user_repository.find_by_username(username)
        if username_is_taken:
          raise AuthenticationError("Username is already taken")
        
        if len(username)<3:
          raise UserInputError("Username has to be a minimum of 3 characters")

        if len(password)<8:
          raise UserInputError("Password has to be a minimum of 8 characters")

        valid_password_form = re.compile("[A-Za-z]+")
        if re.fullmatch(valid_password_form,password):
          raise UserInputError("Password must contain numbers")

        valid_username_form = re.compile("[a-z]+")
        if re.fullmatch(valid_username_form,username)==None:
          raise UserInputError("Username can only consist of a-z characters")
