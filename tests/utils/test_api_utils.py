import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pytest
import requests
from libs.utils.api_utils import call_post, call_get, call_put, call_delete
from libs.exceptions.custom_exceptions import APIRequestError

from unittest.mock import patch


# Test for API call using mocker
def test_call_post_success(mocker):
    url = "https://jsonplaceholder.typicode.com/posts"
    token = "test_token"
    headers = {"Custom-Header": "value"}
    json_data = {"title": "foo", "body": "bar", "userId": 1}

    mock_response = mocker.Mock()
    mock_response.status_code = 201
    mock_response.json.return_value = {"id": 101}
    mocker.patch("requests.post", return_value=mock_response)

    response = call_post(url, headers=headers, json=json_data, token=token)

    assert response.status_code == 201
    assert response.json() == {"id": 101}

# Test for API call using mocker
def test_call_post_failure(mocker):
    url = "https://jsonplaceholder.typicode.com/posts"
    token = "test_token"
    headers = {"Custom-Header": "value"}
    json_data = {"title": "foo", "body": "bar", "userId": 1}

    mock_response = mocker.Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("500 Server Error")
    mocker.patch("requests.post", return_value=mock_response)

    with pytest.raises(APIRequestError):
        call_post(url, headers=headers, json=json_data, token=token)
        # Test for API call using mocker
        

def test_call_get_success(mocker):
    url = "https://jsonplaceholder.typicode.com/posts/1"
    token = "test_token"
    headers = {"Custom-Header": "value"}

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "title": "foo", "body": "bar", "userId": 1}
    mocker.patch("requests.get", return_value=mock_response)

    response = call_get(url, headers=headers, token=token)

    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "foo", "body": "bar", "userId": 1}

# Test for API call using mocker
def test_call_get_failure(mocker):
    url = "https://jsonplaceholder.typicode.com/posts/1"
    token = "test_token"
    headers = {"Custom-Header": "value"}

    mock_response = mocker.Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
    mocker.patch("requests.get", return_value=mock_response)

    with pytest.raises(APIRequestError):
        call_get(url, headers=headers, token=token)
        # Test for API call using mocker
        
def test_call_put_success(mocker):
    url = "https://jsonplaceholder.typicode.com/posts/1"
    token = "test_token"
    headers = {"Custom-Header": "value"}
    json_data = {"title": "foo", "body": "bar", "userId": 1}

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "title": "foo", "body": "bar", "userId": 1}
    mocker.patch("requests.put", return_value=mock_response)

    response = call_put(url, headers=headers, json=json_data, token=token)

    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "foo", "body": "bar", "userId": 1}

# Test for API call using mocker
def test_call_put_failure(mocker):
    url = "https://jsonplaceholder.typicode.com/posts/1"
    token = "test_token"
    headers = {"Custom-Header": "value"}
    json_data = {"title": "foo", "body": "bar", "userId": 1}

    mock_response = mocker.Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("500 Server Error")
    mocker.patch("requests.put", return_value=mock_response)

    with pytest.raises(APIRequestError):
        call_put(url, headers=headers, json=json_data, token=token)
        # Test for API call using mocker
def test_call_delete_success(mocker):
    url = "https://jsonplaceholder.typicode.com/posts/1"
    token = "test_token"
    headers = {"Custom-Header": "value"}

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mocker.patch("requests.delete", return_value=mock_response)

    response = call_delete(url, headers=headers, token=token)

    assert response.status_code == 200

# Test for API call using mocker
def test_call_delete_failure(mocker):
    url = "https://jsonplaceholder.typicode.com/posts/1"
    token = "test_token"
    headers = {"Custom-Header": "value"}

    mock_response = mocker.Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
    mocker.patch("requests.delete", return_value=mock_response)

    with pytest.raises(APIRequestError):
        call_delete(url, headers=headers, token=token)
