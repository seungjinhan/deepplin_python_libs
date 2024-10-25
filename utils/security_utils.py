import hashlib
import hmac
import secrets
from exceptions.custom_exceptions import InvalidInputError

def validate_string_input(input_value, parameter_name="입력값"):
    if not isinstance(input_value, str):
        raise InvalidInputError(f"{parameter_name}은 문자열이어야 합니다. 받은 값: {input_value}")

def validate_integer_input(input_value, parameter_name="입력값"):
    if not isinstance(input_value, int):
        raise InvalidInputError(f"{parameter_name}은 정수여야 합니다. 받은 값: {input_value}")
    if input_value <= 0:
        raise InvalidInputError(f"{parameter_name}은 양의 정수여야 합니다. 받은 값: {input_value}")

def hash_password(password: str, salt: str = None) -> str:
    """
    비밀번호를 해시합니다.
    
    :param password: 해시할 비밀번호.
    :param salt: 추가적인 보안성을 위한 솔트 값 (없을 경우 자동 생성).
    :return: 해시된 비밀번호 (솔트 포함).
    """
    validate_string_input(password, "비밀번호")
    if salt is not None:
        validate_string_input(salt, "솔트")
    if salt is None:
        salt = secrets.token_hex(16)
    hash_object = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return f"{salt}${hash_object.hex()}"

def verify_password(password: str, hashed_password: str) -> bool:
    """
    주어진 비밀번호가 해시된 비밀번호와 일치하는지 확인합니다.
    
    :param password: 확인할 비밀번호.
    :param hashed_password: 저장된 해시된 비밀번호.
    :return: 비밀번호가 일치하면 True, 아니면 False.
    """
    validate_string_input(password, "비밀번호")
    validate_string_input(hashed_password, "해시된 비밀번호")
    try:
        salt, hashed = hashed_password.split('$')
        return hash_password(password, salt) == hashed_password
    except ValueError:
        raise InvalidInputError("올바르지 않은 해시된 비밀번호 형식입니다.")

def generate_secure_token(length: int = 32) -> str:
    """
    안전한 토큰을 생성합니다.
    
    :param length: 생성할 토큰의 길이.
    :return: 생성된 토큰.
    """
    validate_integer_input(length, "토큰 길이")
    return secrets.token_hex(length)

def hmac_sign(message: str, key: str) -> str:
    """
    주어진 메시지를 HMAC 방식으로 서명합니다.
    
    :param message: 서명할 메시지.
    :param key: HMAC에 사용할 키.
    :return: 생성된 HMAC 서명.
    """
    validate_string_input(message, "메시지")
    validate_string_input(key, "키")
    hmac_obj = hmac.new(key.encode(), message.encode(), hashlib.sha256)
    return hmac_obj.hexdigest()

def verify_hmac(message: str, key: str, signature: str) -> bool:
    """
    HMAC 서명이 주어진 메시지와 키로부터 생성된 서명과 일치하는지 확인합니다.
    
    :param message: 확인할 메시지.
    :param key: HMAC에 사용할 키.
    :param signature: 확인할 서명.
    :return: 서명이 일치하면 True, 아니면 False.
    """
    validate_string_input(message, "메시지")
    validate_string_input(key, "키")
    validate_string_input(signature, "서명")
    expected_signature = hmac_sign(message, key)
    return hmac.compare_digest(expected_signature, signature)

def hash_data(data: str) -> str:
    """
    주어진 데이터를 SHA-256 방식으로 해시합니다.
    
    :param data: 해시할 데이터.
    :return: 해시된 데이터.
    """
    validate_string_input(data, "데이터")
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
