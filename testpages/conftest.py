import time

import pytest
from selenium import webdriver
from utilities import getconfigure

@pytest.fixture(autouse=True)
def init_driver(get_option,request):
    global driver
    if get_option.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif get_option.__eq__("firefox"):
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get(getconfigure.getconfigure("Basic info","url"))
    request.cls.driver=driver
    yield
    driver.quit()
    time.sleep(2)

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def get_option(request):
    return request.config.getoption("--browser")

