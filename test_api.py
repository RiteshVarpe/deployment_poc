import os
import requests


def get_config(config_key):
    """
    Read value for provided key from the environment variable
    :param config_key:
    :return:
    """
    try:
        env_key = os.environ[config_key]
    except Exception as ex:
        print(
            "Exception getting environment. Check your function has the environment set",
            str(ex))
        env_key = ""
    return env_key


env = get_config("stage")

if env == "stage":
    api_url = "https://u7wmksc2aa.execute-api.us-east-2.amazonaws.com/dev/courses"


def test_get_courses_check_status_code_equals_200():
    response = requests.get(api_url)
    assert response.status_code == 200