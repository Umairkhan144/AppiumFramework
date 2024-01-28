from appium.webdriver import Remote
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder

# Example

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = ''
desired_caps['automationName'] = 'flutter'
desired_caps['deviceName'] = 'Android Emulator'
#desired_caps['deviceName'] = 'bc53eae9d272'
desired_caps['app'] = ('C:\\Users\\Umair\\Test_App\\flutter_application_1\\build\\app\\outputs\\flutter-apk\\app-release.apk')
# desired_caps['appPackage'] = 'com.code2lead.kwad'
# desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

finder = FlutterFinder()

text_finder = finder.by_text('You have pushed the button this many times:')
text_element = FlutterElement(driver, text_finder)
print(text_element.text)

tooltip_finder = finder.by_tooltip("Increment")
driver.execute_script('flutter:waitFor', tooltip_finder, 100)

floating_button_element = FlutterElement(driver, tooltip_finder)
floating_button_element.click()

counter_finder = finder.by_value_key("counter")
counter_element = FlutterElement(driver, counter_finder)
print(counter_element.text)