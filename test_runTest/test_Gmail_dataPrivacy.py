import pytest
from playwright.sync_api import Playwright, expect
from Module.Gmail_login import Login


@pytest.mark.intg
def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/account/about/?hl=en-US")
    login=Login(page)
    login.login()

    page.get_by_role("link", name="Personal info").click()
    page.get_by_role("link", name="Security").click()
    page.wait_for_load_state("networkidle")
    # expect(page.locator("text=Security")).to_be_visible()
    expect(page.locator("text=Security")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


