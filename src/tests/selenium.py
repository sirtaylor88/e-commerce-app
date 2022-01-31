import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from chromedriver_py import binary_path


@pytest.fixture(scope="function")
def chrome_browser_instance(request):
    """Provide a selenium webdriver instance"""
    options = Options()
    options.headless = False
    browser = webdriver.Chrome(service=Service(binary_path), options=options)
    yield browser
    browser.close()