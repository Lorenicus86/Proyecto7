import requests
import configuration
import data
from data import headers
from data import user_body

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=headers)

authToken = post_new_user(user_body).json()["authToken"]

def post_new_client_kit(kit_body):
    auth_token =auth_token_user
    headers_with_auth = data.headers.copy()
    headers_with_auth ["Authorization"] = f'Bearer{auth_token}'
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                        json=kit_body,
                        headers=headers_with_auth)
    return response


