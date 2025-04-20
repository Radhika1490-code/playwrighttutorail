import re

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.mark.luma
def test_runLuma(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://magento.softwaretestingboard.com/")
    page.get_by_role("link", name="Sign In").click()
    # page.pause()
    page.get_by_role("textbox", name="Email*").click()
    page.get_by_role("textbox", name="Email*").fill("radhika.kakani2@harman.com")
    page.get_by_role("textbox", name="Password* Password").click()
    page.get_by_role("textbox", name="Password* Password").fill("Test@123")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_load_state("networkidle")
    expect(page.locator("text=Home Page")).to_be_visible()
    page.hover("text=Women")
    page.hover("text=Tops")
    page.get_by_role("menuitem", name="Jackets").click()
    page.get_by_role("listitem").filter(has_text="Neve Studio Dance Jacket").locator("button").click()
    # page.wait_for_timeout(timeout=2000)
    # ---------------------
    context.close()
    browser.close()

