import requests
from typing import Optional, Dict, Any
import logging
from exceptions.custom_exceptions import APIRequestError, InvalidInputError, AuthenticationError

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_string_input(input_value, parameter_name="입력값"):
    if not isinstance(input_value, str):
        raise InvalidInputError(parameter_name, f"{parameter_name}은 문자열이어야 합니다. 받은 값: {input_value}")

def add_token_to_headers(headers: Optional[Dict[str, str]], token: Optional[str]) -> Dict[str, str]:
    """
    주어진 헤더에 Authorization 토큰을 추가합니다.
    
    :param headers: 기존 헤더들 (옵션).
    :param token: 추가할 토큰 (옵션).
    :return: 토큰이 추가된 헤더 딕셔너리.
    """
    if headers is None:
        headers = {}
    if token:
        try:
            validate_string_input(token, "토큰")
        except InvalidInputError as e:
            logger.error(e)
            raise AuthenticationError("유효하지 않은 토큰입니다.")
        headers['Authorization'] = f"Bearer {token}"
    return headers

def handle_request_exception(e: requests.exceptions.RequestException, request_type: str, url: str):
    """
    요청 중 발생한 예외를 처리하고 로깅합니다.
    
    :param e: 발생한 RequestException.
    :param request_type: 요청의 종류 (GET, POST, PUT, DELETE).
    :param url: 요청을 보낸 URL.
    """
    logger.error(f"{request_type} 요청에 실패했습니다. URL: {url}, 에러: {e}")
    raise APIRequestError(request_type, url, message=str(e))

def make_get_request(url: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, str]] = None, token: Optional[str] = None) -> requests.Response:
    """
    주어진 URL로 GET 요청을 보냅니다.
    
    :param url: 요청을 보낼 URL.
    :param headers: 요청에 사용할 헤더들 (옵션).
    :param params: 요청에 사용할 쿼리 파라미터들 (옵션).
    :param token: 요청에 사용할 토큰 (옵션).
    :return: 요청에 대한 Response 객체.
    """
    validate_string_input(url, "URL")
    headers = add_token_to_headers(headers, token)
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        handle_request_exception(e, "GET", url)

def make_post_request(url: str, data: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, json: Optional[Dict[str, Any]] = None, token: Optional[str] = None) -> requests.Response:
    """
    주어진 URL로 POST 요청을 보냅니다.
    
    :param url: 요청을 보낼 URL.
    :param data: 요청에 사용할 데이터 (옵션).
    :param headers: 요청에 사용할 헤더들 (옵션).
    :param json: 요청에 사용할 JSON 데이터 (옵션).
    :param token: 요청에 사용할 토큰 (옵션).
    :return: 요청에 대한 Response 객체.
    """
    validate_string_input(url, "URL")
    headers = add_token_to_headers(headers, token)
    try:
        response = requests.post(url, data=data, headers=headers, json=json)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        handle_request_exception(e, "POST", url)

def make_put_request(url: str, data: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, json: Optional[Dict[str, Any]] = None, token: Optional[str] = None) -> requests.Response:
    """
    주어진 URL로 PUT 요청을 보냅니다.
    
    :param url: 요청을 보낼 URL.
    :param data: 요청에 사용할 데이터 (옵션).
    :param headers: 요청에 사용할 헤더들 (옵션).
    :param json: 요청에 사용할 JSON 데이터 (옵션).
    :param token: 요청에 사용할 토큰 (옵션).
    :return: 요청에 대한 Response 객체.
    """
    validate_string_input(url, "URL")
    headers = add_token_to_headers(headers, token)
    try:
        response = requests.put(url, data=data, headers=headers, json=json)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        handle_request_exception(e, "PUT", url)

def make_delete_request(url: str, headers: Optional[Dict[str, str]] = None, token: Optional[str] = None) -> requests.Response:
    """
    주어진 URL로 DELETE 요청을 보냅니다.
    
    :param url: 요청을 보낼 URL.
    :param headers: 요청에 사용할 헤더들 (옵션).
    :param token: 요청에 사용할 토큰 (옵션).
    :return: 요청에 대한 Response 객체.
    """
    validate_string_input(url, "URL")
    headers = add_token_to_headers(headers, token)
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        handle_request_exception(e, "DELETE", url)

# Example usage
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    token = "your_token_here"
    try:
        get_response = make_get_request(url, token=token)
        print(f"GET 요청 성공: {get_response.json()[:1]}")  # 첫 번째 결과만 출력
        
        post_data = {"title": "foo", "body": "bar", "userId": 1}
        post_response = make_post_request(url, json=post_data, token=token)
        print(f"POST 요청 성공: {post_response.json()}")
        
        put_data = {"id": 1, "title": "updated title", "body": "updated body", "userId": 1}
        put_response = make_put_request(f"{url}/1", json=put_data, token=token)
        print(f"PUT 요청 성공: {put_response.json()}")
        
        delete_response = make_delete_request(f"{url}/1", token=token)
        print(f"DELETE 요청 성공: 상태 코드 {delete_response.status_code}")
    except (APIRequestError, InvalidInputError, AuthenticationError) as e:
        logger.error(e)
