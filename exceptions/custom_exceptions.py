import json
from enum import Enum

class ErrorCode(Enum):
    API_REQUEST_FAILED = "API_REQUEST_FAILED"
    INVALID_INPUT = "INVALID_INPUT"
    AUTHENTICATION_FAILED = "AUTHENTICATION_FAILED"

class RootException(Exception):
    def __init__(self, error_code: ErrorCode, message: str):
        error_message = json.dumps({"code": error_code.value, "message": message})
        super().__init__(error_message)
        
class APIRequestError(RootException):
    """
    Custom exception raised when an API request fails.
    """
    def __init__(self, request_type: str, url: str, status_code: int = None, message: str = "API request failed"):
        self.request_type = request_type
        self.url = url
        self.status_code = status_code
        self.message = message
        error_message = f"Failed {request_type} request. URL: {url}"
        if status_code:
            error_message += f", Status Code: {status_code}"
        error_message += f", Message: {message}"
        super().__init__(error_code=ErrorCode.API_REQUEST_FAILED, message= error_message)

class InvalidInputError(RootException):
    """
    Custom exception raised when input data is invalid.
    """
    def __init__(self, parameter_name: str, message: str = "Invalid input value"):
        self.parameter_name = parameter_name
        self.message = message
        super().__init__(error_code=ErrorCode.INVALID_INPUT, message= f"{parameter_name}: {message}")

class AuthenticationError(RootException):
    """
    Custom exception raised when an authentication error occurs.
    """
    def __init__(self, message: str = "Authentication failed"):
        self.message = message
        super().__init__(error_code=ErrorCode.AUTHENTICATION_FAILED, message= message)

class CustomError(RootException):
    """
    Custom exception raised when input data is invalid.
    """
    def __init__(self, code:ErrorCode, message: str = "Invalid input value"):
        self.code = code
        self.message = message
        super().__init__(error_code=code, message= "message")
        
# Example usage of custom exceptions
if __name__ == "__main__":
    try:
        raise APIRequestError("GET", "https://example.com/api", status_code=404)
    except APIRequestError as e:
        print(e)
    
    try:
        raise InvalidInputError("username")
    except InvalidInputError as e:
        print(e)
    
    try:
        raise AuthenticationError("Invalid token.")
    except AuthenticationError as e:
        print(e)
