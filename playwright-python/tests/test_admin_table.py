import pytest
from playwright.sync_api import Page, expect
import data.test_data as vars
from utils.helpers import get_user_row

def test_admin_panel_visible( authenticated):
    page = authenticated.new_page()
    page.goto("/")
    expect(page).to_have_url("/web/index.php/dashboard/index")
    page.get_by_role("navigation").get_by_role("link", name= "Admin").click()
    expect(page).to_have_url("/web/index.php/admin/viewSystemUsers")
    expect(page.get_by_role("table")).to_be_visible()


def test_admin_table_user_visible( authenticated):
    page = authenticated.new_page()
    page.goto("/")
    page.get_by_role("navigation").get_by_role("link", name= "Admin").click()
    table = page.get_by_role("table")
    # rows = table.get_by_role("row")
    # columns = table.get_by_role("column")
    row = get_user_row(table, "Admin")
    expect(row).to_contain_text("Enabled")



