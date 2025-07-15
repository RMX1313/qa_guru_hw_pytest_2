from selene import browser
import pytest


@pytest.fixture(autouse=True)
def open_browser():
    browser.open('https://duckduckgo.com')
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    browser.quit()