import time

import pytest
import requests
import json
import test_case_generator
import os

def test_story_flow():
    context = {}
    story_id = os.getenv("STORY_ID", "SCRUM-1")
    test_cases = test_case_generator.generate_test_cases(story_id)

    time.sleep(3)

    for test_case in test_cases:
        url = test_case["url"]
        method = test_case["method"]
        headers = test_case.get("headers", {})
        headers.setdefault("Accept", "application/json")
        body = test_case.get("body", None)

        # Replace placeholders like {petId}
        for key, val in context.items():
            url = url.replace(f"{{{key}}}", str(val))

        # Prepare headers
        if method == "POST" and "Content-Type" not in headers:
            headers["Content-Type"] = "application/json"

        # Execute request
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=json.dumps(body))
        else:
            pytest.skip(f"Unsupported method: {method}")

        # Debug
        print("\n==== DEBUG INFO ====")
        print(f"Request URL: {url}")
        print(f"Method: {method}")
        print(f"Headers: {headers}")
        print(f"Payload: {json.dumps(body, indent=2) if body else 'None'}")
        print(f"Expected Status: {test_case['expected_status_code']}")
        print(f"Actual Status: {response.status_code}")
        print(f"Response Body: {response.text}")
        print("====================\n")

        # Assert status
        assert response.status_code == test_case["expected_status_code"], (
            f"Expected {test_case['expected_status_code']}, got {response.status_code}"
        )

        # Capture petId after POST
        if method == "POST" and response.status_code in [200, 201]:
            try:
                resp_json = response.json()
                if "id" in resp_json:
                    context["petId"] = resp_json["id"]
            except Exception as e:
                print(f"Error parsing POST response: {e}")

        # Validate response body
        expected_response = test_case.get("expected_response")
        if expected_response:
            actual_response = response.json()
            # (Do your condition-based validations here if needed)
