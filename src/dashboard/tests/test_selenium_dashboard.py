import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.selenium
def test_dashboard_admin_login(
    live_server, custom_django_db_setup, chrome_browser_instance
):
    """Test admin should login successfully."""
    # https://pytest-django.readthedocs.io/en/latest/helpers.html#live-server
    browser = chrome_browser_instance
    browser.get(f"{live_server.url}/admin/login/")
    username_input = browser.find_element(By.NAME, "username")
    password_input = browser.find_element(By.NAME, "password")
    submit_button = browser.find_element(By.XPATH, '//input[@value="Log in"]')

    username_input.send_keys("admin")
    password_input.send_keys("qwerty88$%$%$%")
    submit_button.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source
