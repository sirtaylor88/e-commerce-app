import pytest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.mark.selenium
def test_create_new_admin_user(create_admin_user):
    """Test new admin should be created."""
    assert str(create_admin_user) == "admin"


@pytest.mark.selenium
def test_dashboard_admin_login(
    live_server, create_admin_user, chrome_browser_instance
):
    """Test admin should login successfully."""
    # https://pytest-django.readthedocs.io/en/latest/helpers.html#live-server
    browser = chrome_browser_instance
    browser.get(f"{live_server.url}/admin/login/")
    username_input = browser.find_element(By.NAME, "username")
    password_input = browser.find_element(By.NAME, "password")
    submit_button = browser.find_element(By.XPATH, '//input[@value="Log in"]')

    username_input.send_keys("admin")
    password_input.send_keys("qwerty")
    submit_button.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source
