import time
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
import Utilities.CustomLogger as log
from pageObjects.BasePage import BasePage


class landingpage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickSearchField(self):
        self.clickElement('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View',"xpath")

    def clickFollowPlusBtn(self):
        self.clickElement('//android.widget.ImageView[@content-desc="No post to show Click here to follow others"]',"xpath")

    def clickMainPageBtn(self):
        self.clickElement('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[1]',"xpath")

    def clickBrandButton(self):
        self.clickElement('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[2]',"xpath")

    def clickMessageBtn(self):
        self.clickElement('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[3]',"xpath")

    def clickProfileBtn(self):
        self.clickElement('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[4]',"xpath")



