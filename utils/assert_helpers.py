# utils/assert_helpers.py
def assert_response(response: object, expected_status_code: object, expected_message: object = None) -> object:
    assert response.status_code == expected_status_code, f"Expected {expected_status_code}, got {response.status_code}"
    if expected_message:
        assert response.json()['message'] == expected_message, f"Expected message '{expected_message}', got '{response.json().get('message')}'"
