from selenium.webdriver.common.by import By

from utilities.Base import Base


class loginpagePOM(Base):
    username_id="Email"
    pswd_id="Password"
    login_button_class="//button[@class='button-1 login-button']"
    Email_error_text="//span[@id='Email-error']"
    login_error_text="//div[@class='message-error validation-summary-errors']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    def getTitle(self):
        return self.driver.title
    def Enter_username(self,username):
        usd=self.driver.find_element(By.ID,self.username_id)
        usd.clear()
        usd.send_keys(username)

    def Enter_pswd(self,pswd):
        psd=self.driver.find_element(By.ID,self.pswd_id)
        psd.clear()
        psd.send_keys(pswd)

    def login_click(self):
        self.driver.find_element(By.XPATH,self.login_button_class).click()

    def get_email_error_text(self):
        return self.driver.find_element(By.XPATH,self.Email_error_text).text

    def get_login_error_text(self):
        return self.driver.find_element(By.XPATH,self.login_error_text).text
    def get_screenshot(self):
        self.screenshot()







