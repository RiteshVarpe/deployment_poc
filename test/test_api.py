import requests


def test_get_courses_check_status_code_equals_200(api_url):
    response = requests.get(api_url)
    assert response.status_code == 200