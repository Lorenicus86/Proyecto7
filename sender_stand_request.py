import requests
import configuration
import data
from data import user_body
from data import headers

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=headers)
    response.raise_for_status()
    return response.json()

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())

authToken = post_new_user(user_body).json()["authToken"]


header_kit={
    "Content-Type":"application/json",
    "Authorization": f'Bearer {authToken}'
}


def post_user_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                        json=kit_body,
                        headers=header_kit)

response = post_user_kit(data.kit_body)
print(response.status_code)
print(response.json())
