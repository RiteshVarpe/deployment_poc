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



def test_get_courses_check_status_code_equals_200():
    env = get_config("stage")
    print(env)
    response = requests.get("https://u7wmksc2aa.execute-api.us-east-2.amazonaws.com/dev/courses")
    assert response.status_code == 200