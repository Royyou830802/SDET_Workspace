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
    # TODO
    pass


def test_stream_content_all_retries_fail():
    """2-2: All 3 attempts raise Timeout → exception propagates."""
    # TODO
    pass


def test_stream_content_verify_retry_count():
    """2-3: First two calls fail, third succeeds → verify call_count == 3."""
    # TODO
    pass


# ============================================================
# Exercise 3: Test Polling Mechanism
# Function: wait_for_video_processing(video_id, timeout=60)
#
# Hint: mock requests.get, time.time, and time.sleep
#       @patch order (bottom-up) maps to function args (left-to-right)
# ============================================================

def test_wait_for_video_processing_success():
    """3-1: Status changes processing → ready → returns True."""
    # TODO
    pass


def test_wait_for_video_processing_failed():
    """3-2: Status is 'failed' → returns False."""
    # TODO
    pass


def test_wait_for_video_processing_timeout():
    """3-3: time.time exceeds timeout before status is ready → returns False."""
    # TODO
    pass


# ============================================================
# Exercise 4: Test Error Handling
# Function: get_channel_list(user_id)
# ============================================================

def test_get_channel_list_timeout():
    """4-1: requests.Timeout → returns {"error": "Request timeout"}"""
    # TODO
    pass


def test_get_channel_list_connection_error():
    """4-2: requests.ConnectionError → returns {"error": "Connection failed"}"""
    # TODO
    pass


def test_get_channel_list_unknown_error():
    """4-3: Generic Exception → error message contains "Unknown error"."""
    # TODO
    pass


# ============================================================
# Exercise 5: Integration Test Scenario
# Function: user_watch_flow(username, password)
#
# Hint: mock both requests.post (called twice) and requests.get (called once)
# ============================================================

def test_user_watch_flow_success():
    """5-1: Full happy path — auth → recommendations → play."""
    # TODO
    pass


def test_user_watch_flow_auth_failed():
    """5-2: Auth returns success=False → returns error, GET never called."""
    # TODO
    pass


def test_user_watch_flow_no_recommendations():
    """5-3: Auth succeeds but recommendations list is empty → returns error."""
    # TODO
    pass
