import pytest
from playwright.sync_api import Playwright, expect
from Module.Gmail_login import Login

@pytest.mark.smoke
def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&ifkv=AXH0vVsr-sLrNs5VG9u5ceMDMfFP3o5ZnPfWP4CYIcMYiiZwokKnUWpohHASWSES01XHGGGtoV538Q&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S35907864%3A1744715294899384")
    login = Login(page)
    login.login()

    # page.sleep(2)
    # page.get_by_role("button", name="Continue").click()
    # page.goto("https://gds.google.com/web/recoveryoptions?cardIndex=0&hl=en&authuser=0&gdsid=320223765&continue=https%3A%2F%2Faccounts.google.com%2FServiceLogin%3Fcontinue%3Dhttps%3A%2F%2Faccounts.google.com%2F%26hl%3Den%26authuser%3D0%26passive%3Dtrue%26sarp%3D1%26aodrpl%3D1%26checkedDomains%3Dyoutube%26checkConnection%3Dyoutube%3A536%26pstMsg%3D1&rapt=AEjHL4OiNNowwjhldK9wtfCxVH5sAMD4Rh0i039saaRDghWqU0aQDMAGRDYb8eYjFR0E630e45QW2aJ126WgHdYFO2ZNAB3GIA&ep=p&landing=true")
    # page.get_by_role("button", name="Cancel").click()
    # page.get_by_role("button", name="Skip").click()
    page.get_by_role("link", name="Personal info").click()
    # page.wait_for_load_state("networkidle")
    expect(page.locator("text=Basic Info")).to_be_visible()
    # ---------------------
    context.close()
    browser.close()

