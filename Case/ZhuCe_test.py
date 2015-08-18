# encoding:utf-8
from Action import ZhuCe
import unittest
from appium import webdriver
from time import sleep
class ZhuCeTest(unittest.TestCase):

    # def testZhuce(self):
    #     # desired_caps={'platformName':'Android','platformVersion':'4.4','deviceName':'HUAWEI C8817E','appPackage':'com.dinghe.dingding.community','appActivity':'.SplashActivity'}
    #     desired_caps={'platformName':'Android','platformVersion':'4.4','deviceName':'SM-G3608','appPackage':'com.dinghe.dingding.community','appActivity':'.SplashActivity','resetKeyboard':True}
    #     self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    #
    #     sleep(5)




    def setUp(self):
        desired_caps={'platformName':'Android','platformVersion':'4.4','deviceName':'SM-G3608','appPackage':'com.dinghe.dingding.community','appActivity':'.SplashActivity','resetKeyboard':True}
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.s=ZhuCe.ZhuCe(self.driver)
        sleep(5)

    def testZhuce(self):
        pp=self.s
        pp.getoperateElementMethodAndData1()
        print 'wwg'

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()