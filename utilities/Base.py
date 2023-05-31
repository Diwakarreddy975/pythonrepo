import configparser
import random
import logging
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:

    def __init__(self,driver):
        self.driver=driver
        self.driver = driver

    def wait(self,by_locator,time,value):
        waits=WebDriverWait(self.driver,time)
        waits.until(EC.visibility_of_element_located(by_locator))

    def screenshot(self):
        self.driver.save_screenshot("C:\\Users\\91789\\PycharmProjects\\pytestBy_naveen\\Reports\\screenshots\\"+'screenshot'+str(random.randrange(1000))+'.png')





