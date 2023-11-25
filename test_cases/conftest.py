import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        print('launching chrome')
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        print('launching firefox')
        driver = webdriver.Firefox()
    elif browser == 'edge':
        print('launching edge')
        driver = webdriver.Edge()
    else:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)

    driver.get('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')
    driver.maximize_window()
    yield driver
    driver.quit()
    return driver



