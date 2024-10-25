import secrets
import jwt
from datetime import datetime, timedelta, timezone

from global_utils import global_init
global_init()

from exceptions.custom_exceptions import InvalidInputError, AuthenticationError
from __common import __validate_string_input, __validate_integer_input

def generate_jwt(payload: dict, secret: str, expiration_minutes: int = 60, issued_at: datetime = None, expiration: datetime = None) -> str:
    """
    Generate a JSON Web Token (JWT).

    Args:
        payload (dict): The payload to encode in the JWT.
        secret (str): The secret key to sign the JWT.
        expiration_minutes (int, optional): The expiration time in minutes. Defaults to 60.
        issued_at (datetime, optional): The time the JWT is issued at. Defaults to None.
        expiration (datetime, optional): The expiration time of the JWT. Defaults to None.

    Raises:
        InvalidInputError: If any of the inputs are invalid.

    Returns:
        str: The encoded JWT.
    """
    if not isinstance(payload, dict):
        raise InvalidInputError("payload", "payload must be a dictionary.")
    __validate_string_input(secret, "secret key")
    __validate_integer_input(expiration_minutes, "expiration time")

    if issued_at is None:
        issued_at = datetime.now(timezone.utc)
    elif not isinstance(issued_at, datetime):
        raise InvalidInputError("issued_at", "issued_at must be a datetime object.")
    if issued_at.tzinfo is None:
        raise InvalidInputError("issued_at", "issued_at must be a timezone-aware datetime object.")

    if expiration is None:
        expiration = issued_at + timedelta(minutes=expiration_minutes)
    elif not isinstance(expiration, datetime):
        raise InvalidInputError("expiration", "expiration must be a datetime object.")
    if expiration.tzinfo is None:
        raise InvalidInputError("expiration", "expiration must be a timezone-aware datetime object.")

    payload.update({"exp": expiration, "iat": issued_at})
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token

def verify_jwt(token: str, secret: str) -> dict:
    """
    Verify a JSON Web Token (JWT).

    Args:
        token (str): The JWT to verify.
        secret (str): The secret key to verify the JWT.

    Raises:
        AuthenticationError: If the JWT is invalid or expired.

    Returns:
        dict: The decoded payload.
    """
    __validate_string_input(token, "JWT")
    __validate_string_input(secret, "secret key")
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationError("The JWT signature has expired.")
    except jwt.InvalidTokenError:
        raise AuthenticationError("Invalid JWT.")

def generate_csrf_token() -> str:
    """
    Generate a CSRF token.

    Returns:
        str: The generated CSRF token.
    """
    return secrets.token_hex(32)

def verify_csrf_token(token: str, expected_token: str) -> bool:
    """
    Verify a CSRF token.

    Args:
        token (str): The CSRF token to verify.
        expected_token (str): The expected CSRF token.

    Returns:
        bool: True if the tokens match, False otherwise.
    """
    __validate_string_input(token, "CSRF token")
    __validate_string_input(expected_token, "expected CSRF token")
    return secrets.compare_digest(token, expected_token)

if __name__ == "__main__":
    secret_key = "supersecretkey"
    payload = {"user_id": 123, "username": "test_user"}
    issued_at_time = datetime.now(timezone.utc)
    expiration_time = issued_at_time + timedelta(minutes=120)
    
    # Generate a JWT
    jwt_token = generate_jwt(payload, secret_key, issued_at=issued_at_time, expiration=expiration_time)
    print(f"Generated JWT: {jwt_token}")
    
    try:
        # Verify the generated JWT
        decoded_payload = verify_jwt(jwt_token, secret_key)
        print(f"Decoded JWT payload: {decoded_payload}")
    except AuthenticationError as e:
        print(f"JWT verification failed: {e}")
    
    # Generate a CSRF token
    csrf_token = generate_csrf_token()
    print(f"Generated CSRF Token: {csrf_token}")
    
    # Verify the CSRF token
    is_valid_csrf = verify_csrf_token(csrf_token, csrf_token)
    print(f"CSRF Token Verification: {is_valid_csrf}")
