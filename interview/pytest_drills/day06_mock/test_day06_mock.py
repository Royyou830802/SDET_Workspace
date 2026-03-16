"""
Day 06 Mock - Test Exercises
=============================
Replace each TODO with your own implementation.
Run: pytest interview/pytest_drills/day06_mock/test_day06_mock.py -v
"""

import pytest
import requests
from unittest.mock import patch, Mock

from .exercises import (
    get_device_info,
    stream_content,
    wait_for_video_processing,
    get_channel_list,
    user_watch_flow,
)

MODULE = "interview.pytest_drills.day06_mock.exercises"


# ============================================================
# Exercise 1: Mock an External API Call
# Function: get_device_info(device_id)
# ============================================================

def test_get_device_info_success():
    """1-1: status_code = 200 → returns device data"""
    with patch(f"{MODULE}.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "id": "roku-001",
            "name": "Roku Ultra"
        }
        result = get_device_info("roku-001")
        assert result["id"] == "roku-001"
        assert result["name"] == "Roku Ultra"
        mock_get.assert_called_once()
        mock_get.assert_called_with("https://api.roku.com/devices/roku-001")


@patch(f"{MODULE}.requests.get")
def test_get_device_info_not_found(mock_get):
    """1-2: status_code = 404 → returns error dict"""
    mock_get.return_value.status_code = 404
    result = get_device_info("unknown-device")
    assert "error" in result
    assert result["error"] == "Device not found"


@patch(f"{MODULE}.requests.get")
def test_get_device_info_api_error(mock_get):
    """1-3: status_code = 500 → raises Exception"""
    mock_get.return_value.status_code = 500
    with pytest.raises(Exception) as exc_info:
        get_device_info("roku-001")
    assert exc_info.type == Exception
    assert "API Error" in str(exc_info.value)


# ============================================================
# Exercise 2: Test Retry Mechanism
# Function: stream_content(content_id, max_retries=3)
# ============================================================

def test_stream_content_retry_then_success():
    """2-1: First call raises Timeout, second call succeeds."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = "Success"
    with patch(f"{MODULE}.requests.get") as mock_get:
        mock_get.side_effect = [
            requests.Timeout("Request Time Out."),
            mock_response
        ]
        result = stream_content("Test_Timeout_Recall")
        assert result == "Success"
        assert mock_get.call_count == 2
        mock_get.assert_called_with("https://api.roku.com/stream/Test_Timeout_Recall")

@patch(f"{MODULE}.requests.get")
def test_stream_content_all_retries_fail(mock_get):
    """2-2: All 3 attempts raise Timeout → exception propagates."""
    mock_get.side_effect = [
        requests.Timeout("Time out 1st.."),
        requests.Timeout("Time out 2nd.."),
        requests.Timeout("Time out 3rd..")
    ]
    with pytest.raises(Exception) as exacInfo:
        stream_content("Test_Timeout_Recall")
    assert exacInfo.type == requests.ConnectionError
    assert "time out" in str(exacInfo.value)
    assert mock_get.call_count == 3
    mock_get.assert_called_with("https://api.roku.com/stream/Test_Timeout_Recall")

@patch(f"{MODULE}.requests.get")
def test_stream_content_verify_retry_count(mock_get):
    """2-3: First two calls fail, third succeeds → verify call_count == 3."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = "success"
    mock_get.side_effect = [
        requests.Timeout("Time out 1st.."),
        requests.Timeout("Time out 2nd.."),
        mock_response
    ]
    result = stream_content("Test_Timeout_FinalSuccess")
    assert result == "success"
    assert mock_get.call_count == 3
    mock_get.assert_called_with("https://api.roku.com/stream/Test_Timeout_FinalSuccess")

# ============================================================
# Exercise 3: Test Polling Mechanism
# Function: wait_for_video_processing(video_id, timeout=60)
#
# Hint: mock requests.get, time.time, and time.sleep
#       @patch order (bottom-up) maps to function args (left-to-right)
# ============================================================
@patch(f"{MODULE}.time.time")
@patch(f"{MODULE}.time.sleep")
@patch(f"{MODULE}.requests.get")
def test_wait_for_video_processing_success(mock_get, mock_sleep, mock_time):
    """3-1: Status changes processing → ready → returns True."""
    # Mock the time() to prevent actual time waste
    mock_time.side_effect = [0, 1, 2]
    # Mock the requests.get result 
    video_id = "MockTest_VideoProcess"
    # Set the return value when the method json() called
    mock_get.return_value.json.side_effect = [
        {"video_id": video_id, "status": "processing"},
        {"video_id": video_id, "status": "ready"},
    ]
    result = wait_for_video_processing(video_id)

    assert result == True
    assert mock_get.call_count == 2
    mock_get.assert_called_with(f"https://api.roku.com/videos/{video_id}/status")

@patch(f"{MODULE}.time.time")
@patch(f"{MODULE}.time.sleep")
@patch(f"{MODULE}.requests.get")
def test_wait_for_video_processing_failed(mock_get, mock_sleep, mock_time):
    """3-2: Status is 'failed' → returns False."""
    mock_time.side_effect = [0, 1]
    video_id = "MockTest_VideoProcess_failed"
    mock_get.return_value.json.return_value = {"video_id": video_id, "status": "failed"}
    result = wait_for_video_processing(video_id)

    assert result == False
    assert mock_get.call_count == 1
    mock_get.assert_called_with(f"https://api.roku.com/videos/{video_id}/status")

@patch(f"{MODULE}.time.time")
def test_wait_for_video_processing_timeout(mock_time):
    """3-3: time.time exceeds timeout before status is ready → returns False."""
    mock_time.side_effect = [0, 61]
    video_id = "MockTest_VideoProcess_Timeout"
    result = wait_for_video_processing(video_id)

    assert result == False
    assert mock_time.call_count == 2

# ============================================================
# Exercise 4: Test Error Handling
# Function: get_channel_list(user_id)
# ============================================================

@patch(f"{MODULE}.requests.get")
def test_get_channel_list_timeout(mock_get):
    """4-1: requests.Timeout → returns {"error": "Request timeout"}"""
    mock_get.side_effect = requests.Timeout("Timeout mock")
    user_id = "Test_for_get_channel_list_Timeout"
    result = get_channel_list(user_id)
    
    assert result["error"] == "Request timeout"
    mock_get.assert_called_once_with(f"https://api.roku.com/users/{user_id}/channels", timeout=10)

@patch(f"{MODULE}.requests.get")
def test_get_channel_list_connection_error(mock_get):
    """4-2: requests.ConnectionError → returns {"error": "Connection failed"}"""
    mock_get.side_effect = requests.ConnectionError("Connection error mock")
    user_id = "Test_for_get_channel_list_Connection_Error"
    result = get_channel_list(user_id)
    
    assert result["error"] == "Connection failed"
    mock_get.assert_called_once_with(f"https://api.roku.com/users/{user_id}/channels", timeout=10)

@patch(f"{MODULE}.requests.get")
def test_get_channel_list_unknown_error(mock_get):
    """4-3: Generic Exception → error message contains "Unknown error"."""
    Expect_ErrorMsg = [
        "Test value error",
        "Test type error",
        "Test for unknown error"
    ]
    mock_get.side_effect = [
        ValueError(Expect_ErrorMsg[0]),
        TypeError(Expect_ErrorMsg[1]),
        Exception(Expect_ErrorMsg[2])
    ]
    user_id = "Test_for_not_varified_error"
    for idx in range(3):
        # Ask for 3 times to test 3 different unexpected error
        result = get_channel_list(user_id)
        assert result["error"] == f"Unknown error: {Expect_ErrorMsg[idx]}"
    assert mock_get.call_count == 3   

# ============================================================
# Exercise 5: Integration Test Scenario
# Function: user_watch_flow(username, password)
#
# Hint: mock both requests.post (called twice) and requests.get (called once)
# ============================================================

@patch(f"{MODULE}.requests.post")
@patch(f"{MODULE}.requests.get")
def test_user_watch_flow_success(mock_get, mock_post):
    """5-1: Full happy path — auth → recommendations → play."""
    # Define the mock responses for all the 3 function in this user_watch_flow
    mock_response_auth = Mock()
    mock_response_recom = Mock()
    mock_response_play = Mock()
    ## mock response as auth_result
    mock_response_auth.json.return_value = {
        "user_id": "Test_auth_happypath",
        "success": True # get success result to prevent the error
    }
    ## mock response as recommendations
    mock_response_recom.json.return_value = [{"id": "Test_recom_happypath"}] # A list with [0]["id"]
    ## mock response as first_content
    mock_response_play.json.return_value = {"content": "Test_content_name" }
    mock_post.side_effect = [
        mock_response_auth, 
        mock_response_play
    ]
    mock_get.return_value = mock_response_recom
    result = user_watch_flow("testuser", "testpassword")

    assert result["content"] == "Test_content_name"
    assert mock_post.call_count == 2
    mock_post.assert_any_call(
        "https://api.roku.com/auth/login",
        json={"username": "testuser", "password": "testpassword"}
    )
    mock_get.assert_called_once_with("https://api.roku.com/users/Test_auth_happypath/recommendations")
    mock_post.assert_any_call("https://api.roku.com/play/Test_recom_happypath")

def test_user_watch_flow_auth_failed():
    """5-2: Auth returns success=False → returns error, GET never called."""
    # TODO
    pass


def test_user_watch_flow_no_recommendations():
    """5-3: Auth succeeds but recommendations list is empty → returns error."""
    # TODO
    pass
