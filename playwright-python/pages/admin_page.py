from playwright.sync_api import Page


class AdminPage:
    def __init__(self, page: Page):
        self.page = page

    #saves having to type admin_page.page.<method>
    def __getattr__(self, name):
        return getattr(self.page, name)

    def navigate(self):
        self.page.goto("/")
        self.page.get_by_role("navigation"
                    ).get_by_role("link", name= "Admin"
                    ).click()
