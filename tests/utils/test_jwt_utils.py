import pytest
from datetime import datetime, timedelta, timezone
from libs.utils.jwt_utils import generate_jwt, verify_jwt, generate_csrf_token, verify_csrf_token
from libs.exceptions.custom_exceptions import InvalidInputError, AuthenticationError

def test_generate_jwt_valid():
    # Arrange
    payload = {"user_id": 123, "username": "test_user"}
    secret = "supersecretkey"
    issued_at = datetime.now(timezone.utc)
    expiration = issued_at + timedelta(minutes=60)
    
    # Act
    token = generate_jwt(payload, secret, issued_at=issued_at, expiration=expiration)
    
    # Assert
    assert isinstance(token, str)

def test_generate_jwt_invalid_payload():
    # Arrange
    payload = "invalid_payload"
    secret = "supersecretkey"
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        generate_jwt(payload, secret)

def test_generate_jwt_invalid_secret():
    # Arrange
    payload = {"user_id": 123, "username": "test_user"}
    secret = 12345
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        generate_jwt(payload, secret)

def test_generate_jwt_invalid_expiration_minutes():
    # Arrange
    payload = {"user_id": 123, "username": "test_user"}
    secret = "supersecretkey"
    expiration_minutes = "sixty"
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        generate_jwt(payload, secret, expiration_minutes=expiration_minutes)

def test_generate_jwt_invalid_issued_at():
    # Arrange
    payload = {"user_id": 123, "username": "test_user"}
    secret = "supersecretkey"
    issued_at = "invalid_datetime"
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        generate_jwt(payload, secret, issued_at=issued_at)

def test_generate_jwt_invalid_expiration():
    # Arrange
    payload = {"user_id": 123, "username": "test_user"}
    secret = "supersecretkey"
    expiration = "invalid_datetime"
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        generate_jwt(payload, secret, expiration=expiration)

def test_generate_jwt_issued_at_not_timezone_aware():
    # Arrange
    payload = {"user_id": 123, "username": "test_user"}
    secret = "supersecretkey"
    issued_at = datetime.now()
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        generate_jwt(payload, secret, issued_at=issued_at)

def test_generate_jwt_expiration_not_timezone_aware():
    # Arrange
    payload = {"user_id": 123, "username": "test_user"}
    secret = "supersecretkey"
    issued_at = datetime.now(timezone.utc)
    expiration = datetime.now()
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        
        generate_jwt(payload, secret, issued_at=issued_at, expiration=expiration)
        
def test_verify_jwt_valid():
    # Arrange
    payload = {"user_id": 123, "username": "test_user"}
    secret = "supersecretkey"
    issued_at = datetime.now(timezone.utc)
    expiration = issued_at + timedelta(minutes=60)
    token = generate_jwt(payload, secret, issued_at=issued_at, expiration=expiration)
    
    # Act
    decoded_payload = verify_jwt(token, secret)
    
    # Assert
    assert decoded_payload["user_id"] == 123
    assert decoded_payload["username"] == "test_user"

def test_verify_jwt_expired():
    # Arrange
    payload = {"user_id": 123, "username": "test_user"}
    secret = "supersecretkey"
    issued_at = datetime.now(timezone.utc) - timedelta(hours=2)
    expiration = issued_at + timedelta(minutes=60)
    token = generate_jwt(payload, secret, issued_at=issued_at, expiration=expiration)
    
    # Act & Assert
    with pytest.raises(AuthenticationError, match="The JWT signature has expired."):
        verify_jwt(token, secret)

def test_verify_jwt_invalid_token():
    # Arrange
    token = "invalid.token.value"
    secret = "supersecretkey"
    
    # Act & Assert
    with pytest.raises(AuthenticationError, match="Invalid JWT."):
        verify_jwt(token, secret)

def test_verify_jwt_invalid_secret():
    # Arrange
    payload = {"user_id": 123, "username": "test_user"}
    secret = "supersecretkey"
    issued_at = datetime.now(timezone.utc)
    expiration = issued_at + timedelta(minutes=60)
    token = generate_jwt(payload, secret, issued_at=issued_at, expiration=expiration)
    invalid_secret = "wrongsecretkey"
    
    # Act & Assert
    with pytest.raises(AuthenticationError, match="Invalid JWT."):
        verify_jwt(token, invalid_secret)

def test_generate_csrf_token_length():
    # Act
    csrf_token = generate_csrf_token()
    
    # Assert
    assert isinstance(csrf_token, str)
    assert len(csrf_token) == 64  # 32 bytes hex-encoded is 64 characters

def test_generate_csrf_token_uniqueness():
    # Act
    csrf_token_1 = generate_csrf_token()
    csrf_token_2 = generate_csrf_token()
    
    # Assert
    assert csrf_token_1 != csrf_token_2

def test_verify_csrf_token_valid():
    # Arrange
    csrf_token = generate_csrf_token()
    
    # Act
    is_valid = verify_csrf_token(csrf_token, csrf_token)
    
    # Assert
    assert is_valid is True

def test_verify_csrf_token_invalid():
    # Arrange
    csrf_token = generate_csrf_token()
    invalid_token = generate_csrf_token()
    
    # Act
    is_valid = verify_csrf_token(csrf_token, invalid_token)
    
    # Assert
    assert is_valid is False

def test_verify_csrf_token_invalid_input():
    # Arrange
    csrf_token = generate_csrf_token()
    invalid_token = 12345  # Not a string
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        verify_csrf_token(csrf_token, invalid_token)