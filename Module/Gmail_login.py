import re
from playwright.sync_api import Playwright, sync_playwright, expect

class Login():
    def __init__(self, page):
        self.page = page

    def login(self):
        self.page.get_by_role("textbox", name="Email or phone").click()
        self.page.get_by_role("textbox", name="Email or phone").fill("radhikakabcd@gmail.com")
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("textbox", name="Enter your password").click()
        self.page.get_by_role("textbox", name="Enter your password").fill("test_runTest@123")
        self.page.get_by_role("button", name="Next").click()