import unittest
import pytest
from pageObjects.LoginPage import loginpage
from pageObjects.LandingPage import landingpage
import Utilities.CustomLogger as log


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):

    cl = log.customLogger()
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = loginpage(self.driver)
        self.lp = landingpage(self.driver)
        # self.cl = customLogger()

    @pytest.mark.run(order=4)
    def test_LoginUser_001(self):
        self.cl.info("001")
        self.cl.info("Application Launched")
        self.cf.setEmail("test1@yopmail.com")
        self.cl.info("Email Entered")
        self.cf.setPassword("Abcd@1234")
        self.cl.info("Password Entered")
        self.cf.clickLogin()
        self.cl.info("Login Button Clicked")
        self.cf.validateSignIn()
        # self.lp.clickSearchField()
        # self.lp.backBtn()
        # self.lp.backBtn()
        # self.lp.clickFollowPlusBtn()
        # self.lp.backBtn()
        # self.lp.backBtn()
        # self.lp.clickBrandButton()
        # self.lp.clickMessageBtn()
        # self.lp.clickProfileBtn()
        # self.lp.clickMainPageBtn()

    @pytest.mark.run(order=3)
    def test_LoginUser_002(self):
        self.cl.info("002")
        self.cl.info("Application Launched")
        self.cf.setEmail("umair1@yopmail.com")
        self.cl.info("Email Entered")
        self.cf.setPassword("Abcd@1234")
        self.cl.info("Password Entered")
        self.cf.clickLogin()
        self.cl.info("Login Button Clicked")
        self.cf.InvalidateSignIn()

    @pytest.mark.run(order=2)
    def test_LoginUser_003(self):
        self.cl.info("003")
        self.cl.info("Application Launched")
        self.cf.setEmail("umair@yopmail.com")
        self.cl.info("Email Entered")
        self.cf.setPassword("Abcd@12345")
        self.cl.info("Password Entered")
        self.cf.clickLogin()
        self.cl.info("Login Button Clicked")
        self.cf.InvalidateSignIn()

    @pytest.mark.run(order=1)
    def test_LoginUser_004(self):
        self.cl.info("004")
        self.cl.info("Application Launched")
        self.cf.setEmail("umair1@yopmail.com")
        self.cl.info("Email Entered")
        self.cf.setPassword("Abcd@12345")
        self.cl.info("Password Entered")
        self.cf.clickLogin()
        self.cl.info("Login Button Clicked")
        self.cf.InvalidateSignIn()



