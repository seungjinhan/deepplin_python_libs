class APIRequestError(Exception):
    """
    API 요청에 실패했을 때 발생하는 커스텀 예외입니다.
    """
    def __init__(self, request_type: str, url: str, status_code: int = None, message: str = "API 요청 실패"):
        self.request_type = request_type
        self.url = url
        self.status_code = status_code
        self.message = message
        error_message = f"{request_type} 요청에 실패했습니다. URL: {url}"
        if status_code:
            error_message += f", 상태 코드: {status_code}"
        error_message += f", 메시지: {message}"
        super().__init__(error_message)

class InvalidInputError(Exception):
    """
    입력 데이터가 유효하지 않을 때 발생하는 커스텀 예외입니다.
    """
    def __init__(self, parameter_name: str, message: str = "유효하지 않은 입력 값"):
        self.parameter_name = parameter_name
        self.message = message
        super().__init__(f"{parameter_name}: {message}")

class AuthenticationError(Exception):
    """
    인증 관련 오류가 발생했을 때 발생하는 커스텀 예외입니다.
    """
    def __init__(self, message: str = "인증 실패"):
        self.message = message
        super().__init__(message)

# Example usage of custom exceptions
if __name__ == "__main__":
    try:
        raise APIRequestError("GET", "https://example.com/api", status_code=404)
    except APIRequestError as e:
        print(e)
    
    try:
        raise InvalidInputError("사용자 이름")
    except InvalidInputError as e:
        print(e)
    
    try:
        raise AuthenticationError("유효하지 않은 토큰입니다.")
    except AuthenticationError as e:
        print(e)
