import pytest
from playwright.sync_api import Playwright, Page, APIRequestContext, expect
from typing import Generator
import data.test_data as var

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:

    request_context = playwright.request.new_context(base_url="https://opensource-demo.orangehrmlive.com", storage_state="auth/state.json")
    yield request_context
    request_context.dispose()


def test_admin_api_responds(api_request_context: APIRequestContext):
    response = api_request_context.get(var.ADMIN_API)
    assert response.ok

def test_admin_api_contains_admin(api_request_context: APIRequestContext):
    response = api_request_context.get(var.ADMIN_API)
    data = response.json()
    assert any(user["userName"] == "Admin"
               for user in data["data"])


def test_admin_api_mocking_modification(authenticated):
    def handle(route:Route):
        response = route.fetch()
        data = response.json()
        data["data"][0]["userName"] = "Joker"

        route.fulfill(response=response, json=data)


    page = authenticated.new_page()
    page.route(var.ADMIN_API, handle)

    page.goto("/")
    page.get_by_role("navigation").get_by_role("link", name= "Admin").click()
    expect(page.get_by_text("Joker")).to_be_visible()
    page.screenshot(path="screenshotJoker.png")
    


def test_mock_api_interception(authenticated):
    def handle(route: Route):
        print("INTERCEPTED")
        json = {
            "data": [
                {
                    "id": 1,
                    "userName": "Admin",
                    "deleted": False,
                    "status": True,
                    "employee": {
                        "empNumber": 7,
                        "employeeId": "muser",
                        "firstName": "Bruce",
                        "middleName": "Batman",
                        "lastName": "Wayne",
                        "terminationId": None
                    },
                    "userRole": {
                        "id": 1,
                        "name": "Admin",
                        "displayName": "Admin"
                    }
                },
            ],
            "meta": {
                "total": 1
            },
            "rels": []
        }
        route.fulfill(json=json)

    page = authenticated.new_page()
    page.route(var.ADMIN_API, handle)

    page.goto("/")
    page.get_by_role("navigation").get_by_role("link", name= "Admin").click()
    expect(page.get_by_text("Bruce")).to_be_visible()
    page.screenshot(path="screenshotBatman.png")

