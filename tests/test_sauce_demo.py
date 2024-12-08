import allure
from playwright.sync_api import sync_playwright

login_url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"


@allure.title("Testing login ")
@allure.description("Testing the application login")
@allure.tag("Alpha")
def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(login_url)
        page.locator("#user-name").fill(username)
        page.locator("#password").fill(password)
        page.locator("text=Login").click()