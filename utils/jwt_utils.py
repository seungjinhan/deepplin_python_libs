import secrets
import jwt
from datetime import datetime, timedelta, timezone
from exceptions.custom_exceptions import InvalidInputError, AuthenticationError

def validate_string_input(input_value, parameter_name="입력값"):
    if not isinstance(input_value, str):
        raise InvalidInputError(parameter_name, f"{parameter_name}은 문자열이어야 합니다. 받은 값: {input_value}")

def validate_integer_input(input_value, parameter_name="입력값"):
    if not isinstance(input_value, int):
        raise InvalidInputError(parameter_name, f"{parameter_name}은 정수여야 합니다. 받은 값: {input_value}")
    if input_value <= 0:
        raise InvalidInputError(parameter_name, f"{parameter_name}은 양의 정수여야 합니다. 받은 값: {input_value}")

def generate_jwt(payload: dict, secret: str, expiration_minutes: int = 60, issued_at: datetime = None, expiration: datetime = None) -> str:
    """
    JWT(Json Web Token)를 생성합니다.
    
    :param payload: JWT에 포함할 데이터.
    :param secret: JWT를 서명하기 위한 비밀키.
    :param expiration_minutes: 토큰 만료 시간(분 단위).
    :param issued_at: 토큰이 발급된 시간 (기본값은 현재 시간).
    :param expiration: 토큰이 만료되는 시간 (기본값은 issued_at + expiration_minutes).
    :return: 생성된 JWT.
    """
    if not isinstance(payload, dict):
        raise InvalidInputError("payload", "payload는 딕셔너리여야 합니다.")
    validate_string_input(secret, "비밀키")
    validate_integer_input(expiration_minutes, "만료 시간")

    if issued_at is None:
        issued_at = datetime.now(timezone.utc)
    elif not isinstance(issued_at, datetime):
        raise InvalidInputError("issued_at", "issued_at은 datetime 객체여야 합니다.")
    if issued_at.tzinfo is None:
        raise InvalidInputError("issued_at", "issued_at은 시간대 정보가 포함된 datetime 객체여야 합니다.")

    if expiration is None:
        expiration = issued_at + timedelta(minutes=expiration_minutes)
    elif not isinstance(expiration, datetime):
        raise InvalidInputError("expiration", "expiration은 datetime 객체여야 합니다.")
    if expiration.tzinfo is None:
        raise InvalidInputError("expiration", "expiration은 시간대 정보가 포함된 datetime 객체여야 합니다.")

    payload.update({"exp": expiration, "iat": issued_at})
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token

def verify_jwt(token: str, secret: str) -> dict:
    """
    JWT(Json Web Token)를 검증하고, 유효한 경우 payload를 반환합니다.
    
    :param token: 검증할 JWT.
    :param secret: JWT를 서명하기 위한 비밀키.
    :return: JWT의 payload.
    """
    validate_string_input(token, "JWT")
    validate_string_input(secret, "비밀키")
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationError("JWT의 서명이 만료되었습니다.")
    except jwt.InvalidTokenError:
        raise AuthenticationError("유효하지 않은 JWT입니다.")

def generate_csrf_token() -> str:
    """
    CSRF 토큰을 생성합니다.
    
    :return: 생성된 CSRF 토큰.
    """
    return secrets.token_hex(32)

def verify_csrf_token(token: str, expected_token: str) -> bool:
    """
    CSRF 토큰이 예상한 토큰과 일치하는지 확인합니다.
    
    :param token: 검증할 CSRF 토큰.
    :param expected_token: 예상된 CSRF 토큰.
    :return: 토큰이 일치하면 True, 아니면 False.
    """
    validate_string_input(token, "CSRF 토큰")
    validate_string_input(expected_token, "예상된 CSRF 토큰")
    return secrets.compare_digest(token, expected_token)

# Example usage
if __name__ == "__main__":
    secret_key = "supersecretkey"
    payload = {"user_id": 123, "username": "test_user"}
    issued_at_time = datetime.now(timezone.utc)
    expiration_time = issued_at_time + timedelta(minutes=120)
    jwt_token = generate_jwt(payload, secret_key, issued_at=issued_at_time, expiration=expiration_time)
    print(f"Generated JWT: {jwt_token}")
    
    try:
        decoded_payload = verify_jwt(jwt_token, secret_key)
        print(f"Decoded JWT payload: {decoded_payload}")
    except AuthenticationError as e:
        print(f"JWT 검증 실패: {e}")
    
    csrf_token = generate_csrf_token()
    print(f"Generated CSRF Token: {csrf_token}")
    
    is_valid_csrf = verify_csrf_token(csrf_token, csrf_token)
    print(f"CSRF Token Verification: {is_valid_csrf}")