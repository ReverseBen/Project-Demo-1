import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture(scope="session")
def user_ids():
    ids = []
    yield ids


@pytest.fixture(scope="session")
def user_api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="https://reqres.in"
    )
    yield request_context
    request_context.dispose()


def test_create_user(user_api_request_context: APIRequestContext, user_ids) -> None:
    payload = {
        "name": "John Doe",
        "job": "Developer"
    }

    response = user_api_request_context.post(url=f"/api/users", data=payload)
    assert response.ok

    json_response = response.json()
    print('\n'"Create User API Response:\n{}".format(json_response))
    assert json_response["name"] == payload.get("name")
    user_ids.append(json_response["id"])


def test_get_user(user_api_request_context: APIRequestContext) -> None:
    response = user_api_request_context.get(url=f"/api/users/2")
    assert response.status == 200

    json_response = response.json()
    print('\n'"Get User API Response:\n{}".format(json_response))
    assert json_response["data"]["id"] == 2


def test_update_user(user_api_request_context: APIRequestContext) -> None:
    payload = {
        "name": "Morpheus",
        "job": "Zion Resident"
    }

    response = user_api_request_context.put(url=f"/api/users/2", data=payload)
    assert response.status == 200

    json_response = response.json()
    print('\n'"Update User API Response:\n{}".format(json_response))
    assert json_response["name"] == payload.get("name")
