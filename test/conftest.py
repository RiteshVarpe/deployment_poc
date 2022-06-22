import os
import pytest

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


@pytest.fixture(scope="session", autouse=True)
def api_url():
    env = get_config("stage")
    api_url = ""

    if env == "stage":
        api_url = "https://u7wmksc2aa.execute-api.us-east-2.amazonaws.com/dev/courses"

    return api_url