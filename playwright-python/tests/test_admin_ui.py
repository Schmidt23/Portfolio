from playwright.sync_api import  expect
import utils.helpers as helper
import data.test_data as var

def test_admin_panel_visible(authenticated):
    page = authenticated.new_page()
    page.goto("/")
    expect(page).to_have_url("/web/index.php/dashboard/index")
    page.get_by_role("navigation").get_by_role("link", name= "Admin").click()
    expect(page).to_have_url("/web/index.php/admin/viewSystemUsers")
    expect(page.get_by_role("table")).to_be_visible()


def test_admin_column_user_row_exists(admin_page):
    """extra pretty with POM+fixture"""
    #works bc __getattr__
    table = admin_page.get_by_role("table")
    header_user_role = helper.get_table_header(table, "User Role")
    expect(header_user_role).to_be_visible()


def test_admin_panel_requests_user_api(authenticated):
    page = authenticated.new_page()
    page.goto("/")
    with page.expect_request(var.ADMIN_API) as call:
        page.get_by_role("navigation"
            ).get_by_role("link", name= "Admin"
            ).click()

    request = call.value
    assert request.method == "GET"


def test_admin_panel_api_response_ok(authenticated):
    page = authenticated.new_page()
    page.goto("/")
    with page.expect_response(var.ADMIN_API) as response_info:
        page.get_by_role("navigation"
            ).get_by_role("link", name= "Admin"
            ).click()

    response = response_info.value
    assert response.ok


