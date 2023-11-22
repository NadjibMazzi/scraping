import responses
from  src import http_request
from src import ProductProcessor
import pytest
from unittest.mock import patch, mock_open


@responses.activate
def test_http_request():
    # Mock the first request with default User-Agent
    responses.add(responses.POST, "https://httpbin.org/anything", json={"result": "default_response"})

    # Mock the second request with custom User-Agent
    responses.add(responses.POST, "https://httpbin.org/anything", json={"result": "custom_response"})

    # Call the function under test
    body_default, body_custom_ua = http_request()

    # Check the results
    assert body_default == {"result": "default_response"}
    assert body_custom_ua == {"result": "custom_response"}

    # Verify that the requests were made with the expected parameters
    assert len(responses.calls) == 2
    assert responses.calls[0].request.method == "POST"
    assert responses.calls[1].request.method == "POST"

    # Check if the expected URL is a substring of the actual URL
    expected_url = "https://httpbin.org/anything"
    assert expected_url in responses.calls[0].request.url
    assert expected_url in responses.calls[1].request.url




from src import ProductProcessor


def test_process_and_save():
    processor = ProductProcessor()
    processor.process_and_save()
