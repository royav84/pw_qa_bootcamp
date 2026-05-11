# from playwright.sync_api import sync_playwright
from turtle import home
from config.settings import BASE_URL
from pages.home_page import HomePage
import pytest


def test_pw_smoke(page, app_base_url):
    page.goto(app_base_url + "/", wait_until="domcontentloaded")
    # assert False, "FORCE_FAIL_123"
    assert "playwright" in page.title().lower()