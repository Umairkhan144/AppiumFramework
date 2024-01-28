import time

from appium import webdriver

class Driver:
    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = ''
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['deviceName'] = 'Android Emulator'
        #desired_caps['deviceName'] = 'bc53eae9d272'
        desired_caps['app'] = ('C:\\Users\\Umair\\PycharmProjects\\LinkFront\\ApplicationsAPK\\linkfront-v2.1.4 (1).apk')
        # desired_caps['appPackage'] = 'com.code2lead.kwad'
        # desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        time.sleep(10)
        return driver
