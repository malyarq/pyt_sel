import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language == None:
        raise pytest.UsageError("--language should be entered")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    print(f"Open browser with {language} language..")
    browser.implicitly_wait(5)
    yield browser
    time.sleep(30)
    print("\nquit browser..")
    browser.quit()