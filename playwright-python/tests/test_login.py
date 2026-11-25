import pytest
from playwright.sync_api import Page, expect
import data.test_data as vars
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)

def test_valid_login(page, login_page):
    page.goto("/")
    login_page.login(vars.USERNAME, vars.PASSWORD)
    expect(page).to_have_url("/web/index.php/dashboard/index")

def test_invalid_login(page, login_page):
    page.goto("/")
    login_page.login("invalid", "invalid")
    expect(page.get_by_role("alert")).to_contain_text("Invalid credentials")
    expect(page).not_to_have_url("/web/index.php/dashboard/index")
    expect(page).to_have_url("web/index.php/auth/login")


@pytest.mark.parametrize(
"username, password, url",
[("Admin", "admin123", "/web/index.php/dashboard/index"), ("invalid", "invalid", "web/index.php/auth/login")],
ids=["valid", "not_valid"])
def test_as_ddt(page, login_page, username, password, url):
    page.goto("/")
    login_page.login(username, password)
    expect(page).to_have_url(url)