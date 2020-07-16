import json

import requests

from api_tests.errors.custom_errors import AuthorizationError


def _read_config(file, tag):
    with open(file) as json_file:
        as_dict = json.load(json_file)[tag]
        return as_dict


def get_authorization():
    headers = {}
    app_data = _read_config("config.json", "auth")

    request_body = {"username": app_data["username"],
                    "password": app_data["password"]}

    response = requests.post(
        url=app_data["url"],
        json=request_body
    )

    if response.status_code == 200:
        headers = {"Authorization": "Bearer {}".format(response.json()["token"])}
        return headers
    else:
        raise AuthorizationError
