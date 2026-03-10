"""
Day 06 Mock - Exercise Source Code
====================================
This file contains 5 functions/classes to be tested.
Write your tests in test_day06_mock.py.
"""

import requests
import time


# ============================================================
# Exercise 1: Mock an External API Call
# ============================================================

def get_device_info(device_id):
    """Fetch Roku device information by device ID."""
    response = requests.get(f"https://api.roku.com/devices/{device_id}")
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return {"error": "Device not found"}
    else:
        raise Exception("API Error")


# ============================================================
# Exercise 2: Test Retry Mechanism
# ============================================================

def stream_content(content_id, max_retries=3):
    """Stream content with a retry mechanism."""
    for attempt in range(max_retries):
        try:
            response = requests.get(f"https://api.roku.com/stream/{content_id}")
            if response.status_code == 200:
                return response.json()
        except requests.Timeout:
            if attempt == max_retries - 1:
                raise
            continue
    return None


# ============================================================
# Exercise 3: Test Polling / Async API
# ============================================================

def wait_for_video_processing(video_id, timeout=60):
    """Poll until video processing is complete or timeout is reached."""
    start_time = time.time()

    while time.time() - start_time < timeout:
        response = requests.get(f"https://api.roku.com/videos/{video_id}/status")
        status = response.json()["status"]

        if status == "ready":
            return True
        elif status == "failed":
            return False

        time.sleep(5)

    return False  # timed out


# ============================================================
# Exercise 4: Test Error Handling
# ============================================================

def get_channel_list(user_id):
    """Fetch the channel list for a given user."""
    try:
        response = requests.get(
            f"https://api.roku.com/users/{user_id}/channels",
            timeout=10
        )
        return response.json()
    except requests.Timeout:
        return {"error": "Request timeout"}
    except requests.ConnectionError:
        return {"error": "Connection failed"}
    except Exception as e:
        return {"error": f"Unknown error: {str(e)}"}


# ============================================================
# Exercise 5: Integration Test Scenario
# ============================================================

class RokuService:
    def authenticate(self, username, password):
        """Log in a user."""
        response = requests.post(
            "https://api.roku.com/auth/login",
            json={"username": username, "password": password}
        )
        return response.json()

    def get_recommendations(self, user_id):
        """Fetch recommended content for a user."""
        response = requests.get(f"https://api.roku.com/users/{user_id}/recommendations")
        return response.json()

    def play_content(self, content_id):
        """Play a piece of content."""
        response = requests.post(f"https://api.roku.com/play/{content_id}")
        return response.json()


def user_watch_flow(username, password):
    """Full watch flow: authenticate → get recommendations → play first item."""
    service = RokuService()

    # Step 1: authenticate
    auth_result = service.authenticate(username, password)
    if not auth_result.get("success"):
        return {"error": "Authentication failed"}

    user_id = auth_result["user_id"]

    # Step 2: get recommendations
    recommendations = service.get_recommendations(user_id)
    if not recommendations:
        return {"error": "No recommendations"}

    # Step 3: play the first recommended item
    first_content = recommendations[0]["id"]
    play_result = service.play_content(first_content)

    return play_result