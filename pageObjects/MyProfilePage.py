import time
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from pageObjects.BasePage import BasePage
from Utilities.readProperties import ReadConfig

class myProfilePage(BasePage):

    SettingBtn = ReadConfig.getSettingBtn()
    logout = ReadConfig.getLogout()
    logoutBtn = ReadConfig.getLogoutBtn()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def clickSettingBtn(self):
        self.clickElement(self.SettingBtn,"xpath")

    def clickLogout(self):
        self.clickElement(self.logout,"xpath")

    def confirmLogout(self):
        self.clickElement(self.logoutBtn,"xpath")