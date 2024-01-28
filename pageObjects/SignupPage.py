import time
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
import Utilities.CustomLogger as log
from pageObjects.BasePage import BasePage


class signuppage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def clickSignup(self):
        spbtn = self.waitForElement("10","index")
        spbtn.click()

    def clickShoppingbtn(self):
        shopbtn = self.waitForElement('2',"index")
        shopbtn.click()

    def clickgetStarted(self):
        GSbtn = self.waitForElement('4',"index")
        GSbtn.click()

    def setFullname(self,fullname):
        fname = self.waitForElement("4","index")
        fname.click()
        fname.send_keys(fullname)

    def setEmail(self,emailid):
        semail = self.waitForElement("Email address","text")
        semail.click()
        semail.send_keys(emailid)
        self.enterBtn()

    def setAge(self, userage):
        cl = log.customLogger()
        txtage = self.waitForElement("6","index")
        txtage.click()
        cl.info("Age Textbox Clicked")
        btnage = self.waitForElement('//android.widget.Button[@content-desc="Switch to input"]',"xpath")
        cl.info("Edit button clicked")
        btnage.click()
        # txtdate = self.waitForElement('//android.view.View[@content-desc="SELECT DATE Thu, Dec 8"]/android.widget.EditText"',"xpath")
        # txtdate.clear()
        # txtdate.send_keys(userage)
        # cl.info("Date Entered")
        okbtn = self.waitForElement('//android.widget.Button[@content-desc="OK"]',"xpath")
        okbtn.click()
        cl.info("OK Button Clicked")

    def setGender(self,sex):
        btnGen = self.waitForElement("7","index")
        btnGen.click()
        time.sleep(2)
        if sex == "M":
            ddGenM = self.waitForElement('//android.view.View[@content-desc="Male"]',"xpath")
            ddGenM.click()
        else:
            ddGenF = self.waitForElement('//android.view.View[@content-desc="Female"]',"xpath")
            ddGenF.click()

    def setPassword(self,password):
        btnpass = self.waitForElement("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.widget.EditText[1]","xpath")
        btnpass.click()
        btnpass.send_keys(password)
        time.sleep(5)

    def setConfirmPassword(self,cpassword):
        btnpass1 = self.waitForElement("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.widget.EditText[2]","xpath")
        btnpass1.click()
        btnpass1.send_keys(cpassword)
        self.enterBtn()

    def checkPolicy(self):
        self.waitForElement("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.widget.CheckBox","xpath").click()

    def clkSignupbtn(self):
        btn = self.waitForElement('//android.widget.Button[@content-desc="Sign up"]',"xpath")
        btn.click()

    def txtOTP(self,otp):
        otptxt = self.waitForElement('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]',"xpath")
        otptxt.click()
        self.driver.press_keycode(0o7);
        self.driver.press_keycode(0o7);
        self.driver.press_keycode(0o7);
        self.driver.press_keycode(0o7);

    def btnVerify(self):
        self.waitForElement('//android.widget.Button[@content-desc="Verify Account"]',"xpath").click()

    def verify(self,SSname):
        try:
            ver = self.driver.find_element(By.XPATH,'//android.view.View[@content-desc="Account Verification"]')
            ver.is_enabled()
            return True
        except NoSuchElementException as exc:
            self.takeScreenshot(SSname)
            return False


    def validateSignUp(self,testName):
        try:
            sigin = self.driver.find_element(By.XPATH,'//android.view.View[@content-desc="Sign in"]')
            sigin.is_enabled()
            assert True
        except NoSuchElementException as exc:
            self.screenShot(testName)
            assert False