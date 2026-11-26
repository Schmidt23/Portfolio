from playwright.sync_api import  expect
import utils.helpers as helper

def test_admin_panel_visible( authenticated):
    page = authenticated.new_page()
    page.goto("/")
    expect(page).to_have_url("/web/index.php/dashboard/index")
    page.get_by_role("navigation").get_by_role("link", name= "Admin").click()
    expect(page).to_have_url("/web/index.php/admin/viewSystemUsers")
    expect(page.get_by_role("table")).to_be_visible()


def test_admin_column_user_row_exists( authenticated):
    page = authenticated.new_page()
    page.goto("/")
    page.get_by_role("navigation").get_by_role("link", name= "Admin").click()
    table = page.get_by_role("table")
    header_user_role = helper.get_table_header(table, "User Role")
    expect(header_user_role).to_be_visible()



