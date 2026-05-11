import pytest
from config.settings import HEADLESS, BASE_URL, BROWSER
from pages.home_page import HomePage

@pytest.fixture(scope="session")
def browser_name():
    # chromium / firefox / webkit
    return BROWSER

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {"headless": HEADLESS}

@pytest.fixture(scope="session")
def context_options():
    # מאפשר page.goto("/") במקום URL מלא
    return {"base_url": BASE_URL}

@pytest.fixture(scope="session")
def app_base_url():
    return BASE_URL

@pytest.fixture()
def home_page(page, app_base_url):
    home_page = HomePage(page)
    home_page.open(app_base_url)
    return home_page


