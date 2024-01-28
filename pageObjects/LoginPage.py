import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObjects.BasePage import BasePage
from Utilities.readProperties import ReadConfig

class loginpage(BasePage):

    emailtxt = ReadConfig.getEmailLV()
    passtxt = ReadConfig.getPassLV()
    loginbtn = ReadConfig.getLoginBtnLV()
    LPLogo = ReadConfig.getLPLogo()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def setEmail(self,username):
        self.sendText(username, self.emailtxt, "class")
        # txtemail = self.driver.find_element(By.CLASS_NAME,self.emailtxt)
        # txtemail.click()
        # txtemail.clear()
        # time.sleep(2)
        # txtemail.send_keys(username)

    def setPassword(self,password):
        self.sendText(password,self.passtxt,"class")
        # txtpass = self.driver.find_element(By.CLASS_NAME, self.passtxt)
        # txtpass.click()
        # txtpass.clear()
        # time.sleep(2)
        # txtpass.send_keys(password)

    def clickLogin(self):
        self.clickElement(self.loginbtn,"class")
        # self.driver.find_element(By.CLASS_NAME,self.loginbtn).click()
        # time.sleep(10)

    def validateSignIn(self):
        siginin = self.waitForElement(self.LPLogo,'xpath')
            #self.driver.find_element(By.XPATH,self.LPLogo)
        if siginin.is_enabled():
            assert True
        else:
            assert False

    def InvalidateSignIn(self):
        siginin = self.driver.find_element(By.ANDROID_UIAUTOMATOR,'UiSelector().description("Sign in")')
        print(siginin.is_enabled())
        if siginin.is_enabled():
            assert True
        else:
            assert False