import hashlib
import hmac
import secrets

from global_utils import global_init
global_init()

from exceptions.custom_exceptions import InvalidInputError
from __validate import __validate_string_input, __validate_integer_input


def hash_password(password: str, salt: str = None) -> str:
    """
    Hashes a password.
    
    :param password: The password to hash.
    :param salt: Optional salt for added security (auto-generated if not provided).
    :return: The hashed password (including the salt).
    """
    __validate_string_input(password, "password")
    if salt is not None:
        validate_string_input(salt, "salt")
    if salt is None:
        salt = secrets.token_hex(16)
    hash_object = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return f"{salt}${hash_object.hex()}"

def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verifies if the given password matches the hashed password.
    
    :param password: The password to verify.
    :param hashed_password: The stored hashed password.
    :return: True if the password matches, False otherwise.
    """
    __validate_string_input(password, "password")
    __validate_string_input(hashed_password, "hashed password")
    try:
        salt, hashed = hashed_password.split('$')
        return hash_password(password, salt) == hashed_password
    except ValueError:
        raise InvalidInputError("Invalid hashed password format.")

def generate_secure_token(length: int = 32) -> str:
    """
    Generates a secure token.
    
    :param length: The length of the token to generate.
    :return: The generated token.
    """
    __validate_integer_input(length, "token length")
    return secrets.token_hex(length)

def hmac_sign(message: str, key: str) -> str:
    """
    Signs a message using HMAC.
    
    :param message: The message to sign.
    :param key: The key to use for HMAC.
    :return: The generated HMAC signature.
    """
    __validate_string_input(message, "message")
    __validate_string_input(key, "key")
    hmac_obj = hmac.new(key.encode(), message.encode(), hashlib.sha256)
    return hmac_obj.hexdigest()

def verify_hmac(message: str, key: str, signature: str) -> bool:
    """
    Verifies if the HMAC signature matches the given message and key.
    
    :param message: The message to verify.
    :param key: The key to use for HMAC.
    :param signature: The signature to verify.
    :return: True if the signature matches, False otherwise.
    """
    __validate_string_input(message, "message")
    __validate_string_input(key, "key")
    __validate_string_input(signature, "signature")
    expected_signature = hmac_sign(message, key)
    return hmac.compare_digest(expected_signature, signature)

def hash_data(data: str) -> str:
    """
    Hashes the given data using SHA-256.
    
    :param data: The data to hash.
    :return: The hashed data.
    """
    __validate_string_input(data, "data")
    return hashlib.sha256(data.encode()).hexdigest()

# Example usage
if __name__ == "__main__":
    password = "securepassword123"
    hashed = hash_password(password)
    print(f"Hashed password: {hashed}")
    print(f"Password verification: {verify_password(password, hashed)}")
    
    token = generate_secure_token()
    print(f"Generated secure token: {token}")
    
    message = "This is a secret message"
    key = "supersecretkey"
    signature = hmac_sign(message, key)
    print(f"HMAC Signature: {signature}")
    print(f"HMAC Verification: {verify_hmac(message, key, signature)}")
    
    data = "Sensitive data"
    hashed_data = hash_data(data)
    print(f"Hashed data: {hashed_data}")
