import pytest

from pagePOM.loginpagePOM import loginpagePOM
from utilities.Base import Base
from utilities import getconfigure as GF
from utilities.get_loggers import log001

class Test_page():
    baseURL = GF.getconfigure("Basic info","url")
    login_page_title = GF.getconfigure("Basic info", "title_of_loginpage")
    home_page_title = GF.getconfigure("Basic info", "title_of_home_page")
    username_ = GF.getconfigure("data info", "user")
    psw_ = GF.getconfigure("data info", "pswd")
    username_invalid = GF.getconfigure("data info", "user_invalid")
    psw_invalid = GF.getconfigure("data info", "pswd_invalid")



    def test_validating_login_page_title(self,init_driver):
        logger=log001().generate_log()
        logger.info("driver initialised")

        self.driver=init_driver
        assert self.driver.title==self.login_page_title
        logger.info("validation of login page completed")

    def test_validating_login_functionality(self,init_driver):
        self.driver = init_driver
        logger = log001().generate_log()
        logger.info("validation of login functionality with valid credentials started")
        loginPOM=loginpagePOM(self.driver)
        loginPOM.Enter_username(self.username_)
        loginPOM.Enter_pswd(self.psw_)
        loginPOM.login_click()
        assert self.driver.title==self.home_page_title ,"failed to login"
        logger.info("validation of login functionality with valid credentials completed")

    def test_validating_login_Error_message_with_invalid_EmailCredentials_to(self,init_driver):
        self.driver=init_driver
        logger = log001().generate_log()
        logger.info("validation of login functionality with invalid email started")
        loginPOM = loginpagePOM(self.driver)
        loginPOM.Enter_username(self.username_invalid)
        loginPOM.Enter_pswd(self.psw_)
        loginPOM.get_screenshot()
        assert loginPOM.get_email_error_text()==GF.getconfigure("data info","Email_error_text")
        logger.info("validation of login functionality with invalid email completed")

    def test_validating_login_Error_message_with_invalid_password(self,init_driver):
        self.driver=init_driver
        logger = log001().generate_log()
        logger.info("validation of login functionality with valid invalid password started")
        loginPOM = loginpagePOM(self.driver)
        loginPOM.Enter_username(self.username_)
        loginPOM.Enter_pswd(self.psw_invalid)
        loginPOM.login_click()
        print(loginPOM.get_login_error_text())
        loginPOM.get_screenshot()
        assert loginPOM.get_login_error_text()==loginPOM.get_login_error_text()
        logger.info("validation of login functionality with valid invalid password completed")


