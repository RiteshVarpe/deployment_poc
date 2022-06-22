import requests


def test_get_courses_check_status_code_equals_200():
    response = requests.get("https://u7wmksc2aa.execute-api.us-east-2.amazonaws.com/dev/courses")
    assert response.status_code == 200