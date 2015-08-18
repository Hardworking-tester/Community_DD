# encoding:utf-8
from appium import webdriver
from time import sleep
class APPBasePage(object):
    def __init__(self,driver):
        self.driver=driver
        self.timeWait=2
        print self.driver


    def find_element(self,how,what):
        print how,what
        return self.driver.find_element(how,what)

    def click_element(self,located_element):

        located_element.click()
        sleep(self.timeWait)

    def send_data(self,located_element,send_data):
        print send_data
        located_element.send_keys(send_data)
        # if type(send_data)=='float':
        #     located_element.send_keys(int(send_data))
        # else:
        #     located_element.send_keys(send_data)
        # self.driver.hide_keyboard()
        sleep(self.timeWait)