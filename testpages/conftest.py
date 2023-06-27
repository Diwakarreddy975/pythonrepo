import time

import pytest
from selenium import webdriver
from utilities import getconfigure

@pytest.fixture()
def init_driver(request):
    global driver
    browser=getconfigure.getconfigure("Basic info","browser")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get(getconfigure.getconfigure("Basic info","url"))
    request.cls.driver=driver
    yield
    driver.quit()
    time.sleep(2)
# @pytest.fixture()
# def setup(module):
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#
# @pytest.fixture()
# def tear_down(module):
#     driver.quit()
