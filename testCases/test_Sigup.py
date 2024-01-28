import time
import unittest
import pytest
from pageObjects.SignupPage import signuppage
import Utilities.CustomLogger as log


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):
    cl = log.customLogger()
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.sp = signuppage(self.driver)

    @pytest.mark.run(order=1)
    def test_SignUpUser_001(self):
        self.cl.info("Application Launched")
        log.allureLogs("Application Launched")
        self.sp.clickSignup()
        self.cl.info("Signup button Clicked")
        self.sp.clickShoppingbtn()
        self.cl.info("Shopping User button Clicked")
        self.sp.clickgetStarted()
        self.cl.info("Get Started button Clicked")
        self.sp.setFullname("Umair Khan")
        self.cl.info("Username Entered")
        self.sp.setEmail("umair1@yopmail.com")#self.sp.randomString())
        self.cl.info("Email Entered")
        self.sp.setAge("11/19/1999")
        self.cl.info("Age Entered")
        self.sp.setGender("M")
        self.cl.info("Gender Is Selected")
        self.sp.setPassword("Abcd@1234")
        self.cl.info("Password Entered")
        self.sp.setConfirmPassword("Abcd@1234")
        self.cl.info("Confirm Password Entered")
        self.sp.checkPolicy()
        self.cl.info("Accept Policy Checkbox Checked")
        self.sp.clkSignupbtn()
        self.cl.info("SignUp Button Clicked")
        element = self.sp.verify("test_SignUpUser_001")
        if element == True:
            self.sp.txtOTP()
            self.cl.info("OTP Entered")
            self.sp.btnVerify()
            self.cl.info("Verify Button Clicked")
            self.sp.validateSignUp("test_SignUpUser_001")
            self.cl.info("Test Passed")
            assert True
        else:
            time.sleep(2)
            self.sp.screenShot("test_SignUpUser_001")
            self.sp.takeScreenshot("test_SignUpUser_001")
            assert False
            self.cl.info("Test Failed")

