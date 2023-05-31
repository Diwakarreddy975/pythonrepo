# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# def setup_module(module):
#     global driver
#     driver=webdriver.Firefox()
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#
# def teardown_module(module):
#     driver.quit()
#
# @pytest.mark.parametrize("username,pswd",[("7893332489","edcvbhjh"),("09876543","cghjkjhgc")])
# def test_03( username, pswd):
#     driver.get("https://www.facebook.com/login/")
#     driver.find_element(By.ID, "email").send_keys(username)
#     driver.find_element(By.ID, "pass").send_keys(pswd)

