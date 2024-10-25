import pytest
from libs.utils.security_utils import hash_password, verify_password, generate_secure_token, hmac_sign, verify_hmac, hash_data
from libs.exceptions.custom_exceptions import InvalidInputError

def test_hash_password_valid_input():
    # Arrange
    password = "securepassword123"
    
    # Act
    hashed_password = hash_password(password)
    
    # Assert
    assert isinstance(hashed_password, str)
    assert '$' in hashed_password
    salt, hashed = hashed_password.split('$')
    assert len(salt) == 32  # 16 bytes hex-encoded

def test_hash_password_with_salt():
    # Arrange
    password = "securepassword123"
    salt = "a1b2c3d4e5f6g7h8"
    
    # Act
    hashed_password = hash_password(password, salt)
    
    # Assert
    assert isinstance(hashed_password, str)
    assert hashed_password.startswith(salt + '$')

def test_hash_password_empty_password():
    # Arrange
    password = ""
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        hash_password(password)

def test_hash_password_non_string_password():
    # Arrange
    password = 12345
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        hash_password(password)

def test_hash_password_invalid_salt():
    # Arrange
    password = "securepassword123"
    salt = 12345
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        hash_password(password, salt)
        
def test_verify_password_valid():
    # Arrange
    password = "securepassword123"
    hashed_password = hash_password(password)
    
    # Act
    result = verify_password(password, hashed_password)
    
    # Assert
    assert result is True

def test_verify_password_invalid():
    # Arrange
    password = "securepassword123"
    wrong_password = "wrongpassword"
    hashed_password = hash_password(password)
    
    # Act
    result = verify_password(wrong_password, hashed_password)
    
    # Assert
    assert result is False

def test_verify_password_invalid_hashed_format():
    # Arrange
    password = "securepassword123"
    invalid_hashed_password = "invalidhashedpassword"
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        verify_password(password, invalid_hashed_password)

def test_verify_password_empty_password():
    # Arrange
    password = ""
    hashed_password = hash_password("securepassword123")
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        verify_password(password, hashed_password)

def test_verify_password_empty_hashed_password():
    # Arrange
    password = "securepassword123"
    hashed_password = ""
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        verify_password(password, hashed_password)
        
def test_generate_secure_token_default_length():
    # Act
    token = generate_secure_token()
    
    # Assert
    assert isinstance(token, str)
    assert len(token) == 64  # 32 bytes hex-encoded

def test_generate_secure_token_custom_length():
    # Arrange
    length = 16
    
    # Act
    token = generate_secure_token(length)
    
    # Assert
    assert isinstance(token, str)
    assert len(token) == 32  # 16 bytes hex-encoded

def test_generate_secure_token_invalid_length():
    # Arrange
    length = -1
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        generate_secure_token(length)

def test_hmac_sign_valid():
    # Arrange
    message = "This is a secret message"
    key = "supersecretkey"
    
    # Act
    signature = hmac_sign(message, key)
    
    # Assert
    assert isinstance(signature, str)
    assert len(signature) == 64  # SHA-256 produces a 64-character hex string

def test_hmac_sign_empty_message():
    # Arrange
    message = ""
    key = "supersecretkey"
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        hmac_sign(message, key)

def test_hmac_sign_empty_key():
    # Arrange
    message = "This is a secret message"
    key = ""
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        hmac_sign(message, key)

def test_hmac_sign_non_string_message():
    # Arrange
    message = 12345
    key = "supersecretkey"
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        hmac_sign(message, key)

def test_hmac_sign_non_string_key():
    # Arrange
    message = "This is a secret message"
    key = 12345
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        hmac_sign(message, key)

def test_verify_hmac_valid():
    # Arrange
    message = "This is a secret message"
    key = "supersecretkey"
    signature = hmac_sign(message, key)
    
    # Act
    result = verify_hmac(message, key, signature)
    
    # Assert
    assert result is True

def test_verify_hmac_invalid_signature():
    # Arrange
    message = "This is a secret message"
    key = "supersecretkey"
    invalid_signature = "invalidsignature"
    
    # Act
    result = verify_hmac(message, key, invalid_signature)
    
    # Assert
    assert result is False

def test_verify_hmac_empty_message():
    # Arrange
    message = ""
    key = "supersecretkey"
    signature = hmac_sign("This is a secret message", key)
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        verify_hmac(message, key, signature)

def test_verify_hmac_empty_key():
    # Arrange
    message = "This is a secret message"
    key = ""
    signature = hmac_sign(message, "supersecretkey")
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        verify_hmac(message, key, signature)

def test_verify_hmac_empty_signature():
    # Arrange
    message = "This is a secret message"
    key = "supersecretkey"
    signature = ""
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        verify_hmac(message, key, signature)

def test_verify_hmac_non_string_message():
    # Arrange
    message = 12345
    key = "supersecretkey"
    signature = hmac_sign("This is a secret message", key)
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        verify_hmac(message, key, signature)

def test_verify_hmac_non_string_key():
    # Arrange
    message = "This is a secret message"
    key = 12345
    signature = hmac_sign(message, "supersecretkey")
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        verify_hmac(message, key, signature)

def test_verify_hmac_non_string_signature():
    # Arrange
    message = "This is a secret message"
    key = "supersecretkey"
    signature = 12345
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        verify_hmac(message, key, signature)
        

def test_hash_data_valid_input():
    # Arrange
    data = "Sensitive data"
    
    # Act
    hashed_data = hash_data(data)
    
    # Assert
    assert isinstance(hashed_data, str)
    assert len(hashed_data) == 64  # SHA-256 produces a 64-character hex string

def test_hash_data_empty_input():
    # Arrange
    data = ""
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        hash_data(data)

def test_hash_data_non_string_input():
    # Arrange
    data = 12345
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        hash_data(data)