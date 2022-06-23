import requests
import os
import pytest


# @pytest.fixture()
# def api_url():
#     """Fixture that returns a static weather data."""
#     env_key = os.environ['env_stage']
#     api_url = ""
#
#     if env_key == "stage":
#         api_url = "https://u7wmksc2aa.execute-api.us-east-2.amazonaws.com/dev/courses"
#         return api_url

@pytest.fixture
def api_url():
    return os.environ.get('api_url')


def test_get_courses_check_status_code_equals_200(api_url):
    response = requests.get(api_url)
    assert response.status_code == 200