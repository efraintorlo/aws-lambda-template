
class CustomException(Exception):
    def __init__(self, status, message) -> None:
        self.status = status
        self.message = message

    def __str__(self):
        return f"{self.__class__.__name__}: {self.status} - {self.message}"


class AuthError(CustomException):
    def __init__(self, message) -> None:
        super().__init__(401, f'Auth Error: {message}')


class MethodNotAllowed(CustomException):
    def __init__(self) -> None:
        super().__init__(405, f'Method not Allowed')


class BadRequest(CustomException):
    def __init__(self, message) -> None:
        super().__init__(400, f'Bad Request: {message}') # We could have many reason for produce a 400 error


CustomExceptionAll = (AuthError, CustomException)
