import time

import pytest
from selenium import webdriver
from utilities import getconfigure

@pytest.fixture(params=["chrome"],scope="function",autouse=True)
def init_driver(request):
    global driver
    if request.param=="chrome":
        driver = webdriver.Chrome()
    if request.param=="firefox":
        driver=webdriver.Firefox()


    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get(getconfigure.getconfigure("Basic info","url"))
    yield driver
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
