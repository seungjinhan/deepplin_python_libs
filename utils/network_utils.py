import socket
import ssl
from urllib.parse import urlparse
from exceptions.custom_exceptions import InvalidInputError

def validate_string_input(input_value, parameter_name="입력값"):
    if not isinstance(input_value, str):
        raise InvalidInputError(f"{parameter_name}은 문자열이어야 합니다. 받은 값: {input_value}")

def get_ip_address(hostname: str) -> str:
    """
    주어진 호스트 이름의 IP 주소를 반환합니다.
    
    :param hostname: IP 주소를 조회할 호스트 이름.
    :return: 호스트 이름에 해당하는 IP 주소.
    """
    validate_string_input(hostname, "호스트 이름")
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        raise ValueError(f"유효하지 않은 호스트 이름입니다: {hostname}")

def check_port_open(hostname: str, port: int, timeout: int = 5) -> bool:
    """
    주어진 호스트와 포트가 열려 있는지 확인합니다.
    
    :param hostname: 확인할 호스트 이름.
    :param port: 확인할 포트 번호.
    :param timeout: 연결 시도 시간 초과 (초 단위).
    :return: 포트가 열려 있으면 True, 아니면 False.
    """
    validate_string_input(hostname, "호스트 이름")
    if not isinstance(port, int) or not (1 <= port <= 65535):
        raise ValueError(f"포트 번호는 1과 65535 사이의 정수여야 합니다. 받은 값: {port}")
    try:
        with socket.create_connection((hostname, port), timeout=timeout):
            return True
    except (socket.timeout, socket.error):
        return False

def get_ssl_certificate_info(hostname: str, port: int = 443) -> dict:
    """
    주어진 호스트의 SSL 인증서 정보를 반환합니다.
    
    :param hostname: SSL 인증서를 조회할 호스트 이름.
    :param port: HTTPS 포트 (기본값: 443).
    :return: SSL 인증서 정보가 포함된 딕셔너리.
    """
    validate_string_input(hostname, "호스트 이름")
    if not isinstance(port, int) or not (1 <= port <= 65535):
        raise ValueError(f"포트 번호는 1과 65535 사이의 정수여야 합니다. 받은 값: {port}")
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                return cert
    except Exception as e:
        raise ValueError(f"SSL 인증서 정보를 가져오는 데 실패했습니다: {e}")

def is_valid_url(url: str) -> bool:
    """
    주어진 문자열이 유효한 URL인지 확인합니다.
    
    :param url: 확인할 URL 문자열.
    :return: URL이 유효하면 True, 아니면 False.
    """
    validate_string_input(url, "URL")
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

# Example usage
if __name__ == "__main__":
    hostname = "www.google.com"
    print(f"{hostname}의 IP 주소: {get_ip_address(hostname)}")
    
    port = 443
    is_open = check_port_open(hostname, port)
    print(f"{hostname}:{port} 포트 열림 여부: {is_open}")
    
    try:
        cert_info = get_ssl_certificate_info(hostname)
        print(f"{hostname}의 SSL 인증서 정보: {cert_info}")
    except ValueError as e:
        print(e)
    
    url = "https://www.example.com"
    print(f"'{url}'은 유효한 URL인가요?: {is_valid_url(url)}")
