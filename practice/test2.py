#encoding:utf-8
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
# desired_caps['deviceName'] = 'Android Emulator'
desired_caps['deviceName'] = '127.0.0.1:4723'
desired_caps['appPackage'] = 'com.xebest'
desired_caps['appActivity'] = 'com.xebest.activity.SplashActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(6)
driver.find_element_by_id("com.xebest:id/login_input_name").send_keys("192519517@qq.com")
time.sleep(3)
driver.find_element_by_id("com.xebest:id/login_input_password").send_keys("wwg06157715")
time.sleep(3)
print driver.get_window_size()['width']
print driver.get_window_size()['height']
