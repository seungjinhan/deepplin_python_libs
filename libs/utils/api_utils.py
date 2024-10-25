import requests
from typing import Optional, Dict, Any
import logging

from libs.exceptions.custom_exceptions import APIRequestError, InvalidInputError, AuthenticationError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Private functions
def __add_token_to_headers(headers: Optional[Dict[str, str]], token: Optional[str]) -> Dict[str, str]:
    """
    Add the authorization token to the headers if provided.
    
    Args:
        headers (Optional[Dict[str, str]]): The headers dictionary.
        token (Optional[str]): The authorization token.
    
    Returns:
        Dict[str, str]: The updated headers dictionary.
    """
    if token:
        headers['Authorization'] = f"Bearer {token}"
    return headers

def __handle_request_exception(e: requests.exceptions.RequestException, request_type: str, url: str):
    """
    Handle exceptions raised during the request.
    
    Args:
        e (requests.exceptions.RequestException): The exception raised.
        request_type (str): The type of request (GET, POST, etc.).
        url (str): The URL of the request.
    
    Raises:
        APIRequestError: Custom exception for API request errors.
    """
    logger.error(f"Failed to make {request_type} request. URL: {url}, Error: {e}")
    raise APIRequestError(request_type, url, message=str(e))

def __set_default_headers(headers: Optional[Dict[str, str]]) -> Dict[str, str]:
    """
    Set default headers if none are provided.
    
    Args:
        headers (Optional[Dict[str, str]]): The headers dictionary.
    
    Returns:
        Dict[str, str]: The updated headers dictionary with default headers.
    """
    if headers is None:
        headers = {}
    headers['Content-Type'] = 'application/json'
    return headers

def __call(fn, url: str, headers: Optional[Dict[str, str]] = None, token: Optional[str] = None) -> requests.Response:
    """
    Make an HTTP request using the provided function and parameters.
    
    Args:
        fn: The requests function to call (e.g., requests.get).
        url (str): The URL for the request.
        headers (Optional[Dict[str, str]]): The headers for the request.
        token (Optional[str]): The authorization token.
    
    Returns:
        requests.Response: The response from the request.
    
    Raises:
        APIRequestError: Custom exception for API request errors.
    """
    headers = __set_default_headers(headers)    
    if token:
        headers = __add_token_to_headers(headers, token)
    
    logger.info(f"Making request to URL: {url} with headers: {headers}")
    
    try:
        response = fn(url, headers=headers)
        response.raise_for_status()
        logger.info(f"Request to URL: {url} succeeded with status code: {response.status_code}")
        return response
    except requests.exceptions.RequestException as e:
        __handle_request_exception(e, "DELETE", url)

# Public functions      

def call_get(url: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, str]] = None, token: Optional[str] = None) -> requests.Response:
    """
    Make a GET request to the specified URL.
    
    Args:
        url (str): The URL for the GET request.
        headers (Optional[Dict[str, str]]): The headers for the request.
        params (Optional[Dict[str, str]]): The query parameters for the request.
        token (Optional[str]): The authorization token.
    
    Returns:
        requests.Response: The response from the GET request.
    """
    return __call(requests.get, url, headers, token)

def call_post(url: str, data: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, json: Optional[Dict[str, Any]] = None, token: Optional[str] = None) -> requests.Response:
    """
    Make a POST request to the specified URL.
    
    Args:
        url (str): The URL for the POST request.
        data (Optional[Dict[str, Any]]): The form data for the request.
        headers (Optional[Dict[str, str]]): The headers for the request.
        json (Optional[Dict[str, Any]]): The JSON payload for the request.
        token (Optional[str]): The authorization token.
    
    Returns:
        requests.Response: The response from the POST request.
    """
    return __call(requests.post, url, headers, token)

def call_put(url: str, data: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, json: Optional[Dict[str, Any]] = None, token: Optional[str] = None) -> requests.Response:
    """
    Make a PUT request to the specified URL.
    
    Args:
        url (str): The URL for the PUT request.
        data (Optional[Dict[str, Any]]): The form data for the request.
        headers (Optional[Dict[str, str]]): The headers for the request.
        json (Optional[Dict[str, Any]]): The JSON payload for the request.
        token (Optional[str]): The authorization token.
    
    Returns:
        requests.Response: The response from the PUT request.
    """
    return __call(requests.put, url, headers, token)

def call_delete(url: str, headers: Optional[Dict[str, str]] = None, token: Optional[str] = None) -> requests.Response:
    """
    Make a DELETE request to the specified URL.
    
    Args:
        url (str): The URL for the DELETE request.
        headers (Optional[Dict[str, str]]): The headers for the request.
        token (Optional[str]): The authorization token.
    
    Returns:
        requests.Response: The response from the DELETE request.
    """
    return __call(fn=requests.delete, url=url, headers=headers, token=token)

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    token = "your_token_here"
    try:
        delete_response = call_delete(f"{url}/1", token=token)
        print(f"DELETE request successful: Status code {delete_response.status_code}")
    except (APIRequestError, InvalidInputError, AuthenticationError) as e:
        logger.error(e)
