import socket
import ssl
from urllib.parse import urlparse

from global_utils import global_init
global_init()

from exceptions.custom_exceptions import InvalidInputError
from __common import __validate_string_input

def get_ip_address(hostname: str) -> str:
    """
    Returns the IP address of the given hostname.
    
    :param hostname: The hostname to look up the IP address for.
    :return: The IP address corresponding to the hostname.
    """
    __validate_string_input(hostname, "hostname")
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        raise ValueError(f"Invalid hostname: {hostname}")

def check_port_open(hostname: str, port: int, timeout: int = 5) -> bool:
    """
    Checks if the given port on the given host is open.
    
    :param hostname: The hostname to check.
    :param port: The port number to check.
    :param timeout: Connection attempt timeout in seconds.
    :return: True if the port is open, False otherwise.
    """
    __validate_string_input(hostname, "hostname")
    if not isinstance(port, int) or not (1 <= port <= 65535):
        raise ValueError(f"Port number must be an integer between 1 and 65535. Received: {port}")
    try:
        with socket.create_connection((hostname, port), timeout=timeout):
            return True
    except (socket.timeout, socket.error):
        return False

def get_ssl_certificate_info(hostname: str, port: int = 443) -> dict:
    """
    Returns the SSL certificate information of the given host.
    
    :param hostname: The hostname to retrieve the SSL certificate for.
    :param port: The HTTPS port (default: 443).
    :return: A dictionary containing the SSL certificate information.
    """
    __validate_string_input(hostname, "hostname")
    if not isinstance(port, int) or not (1 <= port <= 65535):
        raise ValueError(f"Port number must be an integer between 1 and 65535. Received: {port}")
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                return cert
    except Exception as e:
        raise ValueError(f"Failed to retrieve SSL certificate information: {e}")

def is_valid_url(url: str) -> bool:
    """
    Checks if the given string is a valid URL.
    
    :param url: The URL string to check.
    :return: True if the URL is valid, False otherwise.
    """
    __validate_string_input(url, "URL")
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

# Example usage
if __name__ == "__main__":
    hostname = "www.google.com"
    print(f"IP address of {hostname}: {get_ip_address(hostname)}")
    
    port = 443
    is_open = check_port_open(hostname, port)
    print(f"Is port {port} open on {hostname}?: {is_open}")
    
    try:
        cert_info = get_ssl_certificate_info(hostname)
        print(f"SSL certificate information for {hostname}: {cert_info}")
    except ValueError as e:
        print(e)
    
    url = "https://www.example.com"
    print(f"Is '{url}' a valid URL?: {is_valid_url(url)}")
