import requests
import os
import pytest


@pytest.fixture
def api_url():
    return os.environ.get('api_url')


def test_get_courses_check_status_code_equals_200(api_url):
    response = requests.get(api_url)
    assert response.status_code == 200