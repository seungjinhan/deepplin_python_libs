import pytest
from libs.utils.network_utils import get_ip_address, check_port_open, get_ssl_certificate_info, is_valid_url
from libs.exceptions.custom_exceptions import InvalidInputError

def test_get_ip_address_valid_hostname():
    # Arrange
    hostname = "www.google.com"
    
    # Act
    ip_address = get_ip_address(hostname)
    
    # Assert
    assert isinstance(ip_address, str)
    assert ip_address.count('.') == 3  # Basic check for IPv4 address format

def test_get_ip_address_invalid_hostname():
    # Arrange
    hostname = "invalid.hostname"
    
    # Act & Assert
    with pytest.raises(ValueError, match=f"Invalid hostname: {hostname}"):
        get_ip_address(hostname)

def test_get_ip_address_empty_hostname():
    # Arrange
    hostname = ""
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        get_ip_address(hostname)

def test_get_ip_address_non_string_hostname():
    # Arrange
    hostname = 12345
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        get_ip_address(hostname)

def test_check_port_open_valid_hostname_open_port():
    # Arrange
    hostname = "www.google.com"
    port = 443
    
    # Act
    result = check_port_open(hostname, port)
    
    # Assert
    assert result is True

def test_check_port_open_valid_hostname_closed_port():
    # Arrange
    hostname = "www.google.com"
    port = 9999  # Assuming this port is closed
    
    # Act
    result = check_port_open(hostname, port)
    
    # Assert
    assert result is False

def test_check_port_open_invalid_hostname():
    # Arrange
    hostname = "invalid.hostname"
    port = 443
    
    # Act & Assert
    with pytest.raises(ValueError, match=f"Invalid hostname: {hostname}"):
        check_port_open(hostname, port)

def test_check_port_open_invalid_port():
    # Arrange
    hostname = "www.google.com"
    port = 70000  # Invalid port number
    
    # Act & Assert
    with pytest.raises(ValueError, match=f"Port number must be an integer between 1 and 65535. Received: {port}"):
        check_port_open(hostname, port)

def test_check_port_open_non_string_hostname():
    # Arrange
    hostname = 12345
    port = 443
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        check_port_open(hostname, port)
        
def test_get_ssl_certificate_info_valid_hostname():
    # Arrange
    hostname = "www.google.com"
    
    # Act
    cert_info = get_ssl_certificate_info(hostname)
    
    # Assert
    assert isinstance(cert_info, dict)
    assert "subject" in cert_info
    assert "issuer" in cert_info

def test_get_ssl_certificate_info_invalid_hostname():
    # Arrange
    hostname = "invalid.hostname"
    
    # Act & Assert
    with pytest.raises(ValueError, match=f"Failed to retrieve SSL certificate information: .*"):
        get_ssl_certificate_info(hostname)

def test_get_ssl_certificate_info_empty_hostname():
    # Arrange
    hostname = ""
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        get_ssl_certificate_info(hostname)

def test_get_ssl_certificate_info_non_string_hostname():
    # Arrange
    hostname = 12345
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        get_ssl_certificate_info(hostname)

def test_get_ssl_certificate_info_invalid_port():
    # Arrange
    hostname = "www.google.com"
    port = 70000  # Invalid port number
    
    # Act & Assert
    with pytest.raises(ValueError, match=f"Port number must be an integer between 1 and 65535. Received: {port}"):
        get_ssl_certificate_info(hostname, port)
def test_is_valid_url_valid_http():
    # Arrange
    url = "http://www.example.com"
    
    # Act
    result = is_valid_url(url)
    
    # Assert
    assert result is True

def test_is_valid_url_valid_https():
    # Arrange
    url = "https://www.example.com"
    
    # Act
    result = is_valid_url(url)
    
    # Assert
    assert result is True

def test_is_valid_url_no_scheme():
    # Arrange
    url = "www.example.com"
    
    # Act
    result = is_valid_url(url)
    
    # Assert
    assert result is False

def test_is_valid_url_no_netloc():
    # Arrange
    url = "http:///path"
    
    # Act
    result = is_valid_url(url)
    
    # Assert
    assert result is False

def test_is_valid_url_empty_string():
    # Arrange
    url = ""
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        is_valid_url(url)

def test_is_valid_url_non_string_input():
    # Arrange
    url = 12345
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        is_valid_url(url)