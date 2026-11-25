import pytest
import os
from playwright.sync_api import Browser
import data.test_data as vars

STATE = "auth/state.json"


@pytest.fixture(scope="session")
def base_url():
    return "https://opensource-demo.orangehrmlive.com/"


@pytest.fixture(scope="session")
def authenticated(browser: Browser):
    if not os.path.exists(STATE):
        page = browser.new_page()

        page.goto("https://opensource-demo.orangehrmlive.com/")
        page.get_by_placeholder("Username").fill(vars.USERNAME)
        page.get_by_placeholder("Password").fill(vars.PASSWORD)
        page.get_by_role("button", name="Login").click()
        page.wait_for_url(
            "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        )
        page.context.storage_state(path=STATE)
        page.close()

    context = browser.new_context(
        storage_state=STATE, base_url="https://opensource-demo.orangehrmlive.com"
    )
    yield context

    context.close()
